<script>
	import { page } from '$app/stores';
	import logo from '$lib/images/meow.png';
	import profile from '$lib/images/profile.png';
	import { Dropdown, DropdownItem, Toast } from 'flowbite-svelte'
	import auth from '$lib/services/authService'
	import { isAuthenticated, user } from '$lib/stores/store'
	import { onMount } from 'svelte'
	import notif from '$lib/images/icons/notif.png'
	
	let auth0Client = {}
	
	onMount(async () => {
		auth0Client = await auth.createClient()
		isAuthenticated.set(await auth0Client.isAuthenticated())
		user.set(await auth0Client.getUser())
	})

	function login() {
		auth.loginWithPopup(auth0Client)		
	}

	function logout() {
		auth.logout(auth0Client)
	}

</script>

<header class="flex justify-between">
	<div class="flex justify-between">
		<div class="w-12 h-12">
			<!-- target and rel elements open link in new tab -->
			<a href="/" class="flex items-center justify-center w-full h-full">
				<img src={logo} alt="meow-cat" class="w-8 h-8 object-contain"/>
			</a>
		</div>
		<div class="p-2">
			<button type="button" class="btn-invis" disabled>Log In</button>
		</div>
	</div>
	{#if $isAuthenticated}
	<nav>
		<svg viewBox="0 0 2 3" aria-hidden="true">
			<path d="M0,0 L1,2 C1.5,3 1.5,3 2,3 L2,0 Z" />
		</svg>
		<ul>
			<li aria-current={$page.url.pathname === '/' ? 'page' : undefined}>
				<a href="/">Overview</a>
			</li>
			<li aria-current={$page.url.pathname === '/analytics' ? 'page' : undefined}>
				<a href="/analytics">Analytics</a>
			</li>
			<li aria-current={$page.url.pathname === '/your-cats' ? 'page' : undefined}>
				<a href="/your-cats">Cats</a>
			</li>
		</ul>
		<svg viewBox="0 0 2 3" aria-hidden="true">
			<path d="M0,0 L0,3 C0.5,3 0.5,3 1,2 L2,0 Z" />
		</svg>
	</nav>
	{:else}
	<nav>
		<svg viewBox="0 0 2 3" aria-hidden="true">
			<path d="M0,0 L1,2 C1.5,3 1.5,3 2,3 L2,0 Z" />
		</svg>
		<ul>
			<li aria-current={$page.url.pathname === '/' ? 'page' : undefined}>
				<a href="/">Home</a>
				
			</li>
			<li aria-current={$page.url.pathname === '/pricing' ? 'page' : undefined}>
				<a href="/pricing">Pricing</a>
			</li>
			<li aria-current={$page.url.pathname === '/about' ? 'page' : undefined}>
				<a href="/about">About</a>
			</li>
		</ul>
		<svg viewBox="0 0 2 3" aria-hidden="true">
			<path d="M0,0 L0,3 C0.5,3 0.5,3 1,2 L2,0 Z" />
		</svg>
	</nav>
	{/if}

	{#if !$isAuthenticated}
	<div class="flex justify-between">
		<div class="p-2 flex space-x-2 justify-center object-contain">
			<button id="login" type="button" class="btn-primary" on:click={login}>Log In</button>
		</div>
		
		<div class="w-12 h-12">
			<button id="profile-icon" style="display:none" class="flex items-center justify-center w-full h-full">
				<img src={profile} alt="Profile" class="w-8 h-8 object-contain"/>
			</button>
		</div>
	</div>
	{:else}
	<div class="flex justify-between">
		<div class="p-2">
			<button type="button" class="btn-invis" disabled>Log In</button>
		</div>
		<div class="w-12 h-12">
			<button class="flex items-center justify-center w-full h-full">
				<img src={notif} alt="bell" class="w-7 h-7 object-contain"/>
				<Dropdown class="w-full">
					<Toast>Dismissable User Notification.</Toast>
					<Toast>NEW CAT DETECTED</Toast>
					<Toast>Avery detected on Hudson</Toast>
					<Toast>Something happened.</Toast>
				</Dropdown>
		</button>
		</div>
		<div class="w-12 h-12">
			<button id="profile-icon" class="flex items-center justify-center w-full h-full">
				<img src={profile} alt="Profile" class="w-8 h-8 object-contain"/>
			</button>
			<Dropdown>
				<DropdownItem href="/profile" class="text-inherit no-underline hover:no-underline">Profile</DropdownItem>
				<DropdownItem>Settings</DropdownItem>
				<DropdownItem on:click={logout}>Log Out</DropdownItem>
			</Dropdown>
		</div>
	</div>
	{/if}	
</header>

<style>
	nav {
		display: flex;
		justify-content: center;
		--background: rgba(255, 255, 255, 0.7);
	}

	svg {
		width: 2em;
		height: 3em;
		display: block;
	}

	path {
		fill: var(--background);
	}

	ul {
		position: relative;
		padding: 0;
		margin: 0;
		height: 3em;
		display: flex;
		justify-content: center;
		align-items: center;
		list-style: none;
		background: var(--background);
		background-size: contain;
	}

	li {
		position: relative;
		height: 100%;
	}

	li[aria-current='page']::before {
		--size: 6px;
		content: '';
		width: 0;
		height: 0;
		position: absolute;
		top: 0;
		left: calc(50% - var(--size));
		border: var(--size) solid transparent;
		border-top: var(--size) solid var(--color-theme-1);
	}

	nav a {
		display: flex;
		height: 100%;
		align-items: center;
		padding: 0 0.5rem;
		color: var(--color-text);
		font-weight: 700;
		font-size: 0.8rem;
		text-transform: uppercase;
		letter-spacing: 0.1em;
		text-decoration: none;
		transition: color 0.2s linear;
	}

	a:hover {
		color: var(--color-theme-1);
	}
</style>
