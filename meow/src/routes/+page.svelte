<script>
	import { time } from '../store.js';
	import {onMount} from 'svelte';
	import Gallery from 'svelte-image-gallery'
	// import { MongoClient } from "mongodb"
	
	// function handleImage(e) {
	// 	console.log(e.detail.src)
	// }

</script>

<svelte:head>
	<title>Home</title>
	<meta name="description" content="CATS demo app" />
</svelte:head>

<section class= "flex flex-col justify-items-center align-middle">
	<h1 class="mt-5">C.A.T.S</h1>
	<h1 class="mb-5">Camera Assisted Tracking System</h1>
	<div class="box">
			
		<!-- <pre> -->
			<div>
				<!-- <Gallery on:click={handleImage}>
					{#each todos as todo }
						<img src="{todo.path}" alt="Cat!" />
					{/each}
				</Gallery> -->
			</div>  
		<!-- </pre> -->
	</div>
</section>

<style>

</style>
