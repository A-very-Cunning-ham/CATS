<script>
	import { page } from '$app/stores';
	import logo from '$lib/images/meow.png';
	import github from '$lib/images/github.svg';
	import login from '$lib/images/login-icon.png';
	import login2 from '$lib/images/login-icon-2.png';
</script>

<header>
	<div class="corner">
		<!-- target and rel elements open link in new tab -->
		<a href="https://tenor.com/view/rickroll-roll-rick-never-gonna-give-you-up-never-gonna-gif-22954713" target="_blank" rel="noreferrer noopener">
			<img src={logo} alt="meow-cat" />
		</a>
	</div>

	<nav>
		<svg viewBox="0 0 2 3" aria-hidden="true">
			<path d="M0,0 L1,2 C1.5,3 1.5,3 2,3 L2,0 Z" />
		</svg>
		<ul>
			<li aria-current={$page.url.pathname === '/' ? 'page' : undefined}>
				<a href="/">Home</a>
			</li>
			<li aria-current={$page.url.pathname === '/landing' ? 'page' : undefined}>
				<a href="/landing">Landing</a>
			</li>
			<li aria-current={$page.url.pathname === '/analytics' ? 'page' : undefined}>
				<a href="/analytics">Analytics</a>
			</li>
			<li aria-current={$page.url.pathname === '/about' ? 'page' : undefined}>
				<a href="/about">About</a>
			</li>
		</ul>
		<svg viewBox="0 0 2 3" aria-hidden="true">
			<path d="M0,0 L0,3 C0.5,3 0.5,3 1,2 L2,0 Z" />
		</svg>
	</nav>

	<div class="corner" style="display: flex-end">
		<!-- target and rel elements open link in new tab -->
		<a href="https://github.com/A-very-Cunning-ham/CATS/tree/main" target="_blank" rel="noreferrer noopener"> 
			<img src={github} alt="GitHub" />
		</a>
		<button>
			<img src={login} alt="Login"/>
		</button>
	</div>
</header>

<style>
	header {
		display: flex;
		justify-content: space-between;
	}

	.corner {
		width: 3em;
		height: 3em;
	}

	.corner a {
		display: flex;
		align-items: center;
		justify-content: center;
		width: 100%;
		height: 100%;
	}

	.corner img {
		width: 2em;
		height: 2em;
		object-fit: contain;
	}

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
	button {
		border: none;
		cursor: pointer;
		appearance: none;
		background-color: inherit;
	}
</style>
