<script>
	import { page } from '$app/stores';
	import github from '$lib/images/github.svg';
	import auth from '$lib/services/authService'
	import { isAuthenticated, user } from '$lib/stores/store'

	//prints out user profile and metadata in console for testing purposes
	function checkStatus() {
		isAuthenticated.set(true)
		// const userInfo = JSON.parse(JSON.stringify($user))
		
		// console.log("User authenticated: " + JSON.stringify($isAuthenticated))
		// console.log("UserId: " + userInfo.name)
		// console.log("User info: " + JSON.stringify($user))
	}

</script>

<footer class="flex justify-between items-center p-3">
	<div class="corner">
		<a href="https://github.com/A-very-Cunning-ham/CATS/tree/main" target="_blank" rel="noreferrer noopener" class="flex items-center justify-center w-full h-full"> 
			<img src={github} alt="GitHub" class="object-contain" />
		</a>
	</div>

	<div class="px-3">
			<button type="button" class="btn-primary" 
			on:click={checkStatus}>User Status</button>
	</div>
</footer>

<style>
    .corner {
        width: 3em;
		height: 3em;
	}

	.corner img {
		width: 2em;
		height: 2em;
		object-fit: contain;
	}

    @media (min-width: 480px) {
		footer {
			padding: 12px 0;
		}
	}
</style>
