<script lang='ts'>
	import { time } from '$lib/stores/store';
	import {onMount} from 'svelte';
	import Gallery from 'svelte-image-gallery';
	import { isAuthenticated, user } from '$lib/stores/store';

	// import type { PageData } from './$types';

	// export let data: PageData

	// $: ({images} = data)

	// var dateFromObjectId = function (objectId) {
	// return new Date(parseInt(objectId.substring(0, 8), 16) * 1000);
	// };

</script>

<svelte:head>
	<title>Home</title>
	<meta name="description" content="CATS demo app" />
</svelte:head>

<section class= "flex flex-col justify-items-center align-middle self-center">
	<h1 class="mt-5">C.A.T.S.</h1>
	<h1 class="mb-5">Camera Assisted Tracking System</h1>
	
	{#if $isAuthenticated}
	<div class="block self-center content-center max-w-lg p-6 bg-white border border-gray-200 rounded-lg shadow hover:bg-gray-100">	
		<h5 class="mb-2 text-2xl font-bold tracking-tight text-gray-900">Recent Events</h5>
		<div>
			<!-- <ul>
			{#each images as image}
			<li> -->
				<!-- <img src="{image.path}" alt="Cat!" /> -->
				<!-- <img src="{"./images/"+image.filename}" alt="Cat!" class="max-w-md"/>
				<h6 class="font-bold">Date from Object ID: </h6>{dateFromObjectId(image._id)}
				<h6> Detected Object: {image['object-detected']} </h6>
				<br/>
			</li>
			{/each}
			</ul> -->
		</div> 
	</div>
	{/if}
	
</section>

<style>

</style>
