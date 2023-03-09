<script lang='ts'>
	import {onMount} from 'svelte';
	import { isAuthenticated, user } from '$lib/stores/store';
	import { Button, Card, Carousel, CarouselTransition } from 'flowbite-svelte';

	import type { PageData } from './$types';

	export let data: PageData

	var dateFromObjectId = function (objectId) {
	return new Date(parseInt(objectId.substring(0, 8), 16) * 1000);
	};

	$: ({images} = data)

</script>

<svelte:head>
	<title>Home</title>
	<meta name="description" content="CATS demo app" />
</svelte:head>

{#if $isAuthenticated}

<section class= "flex flex-col self-center">
	<h1 class="mt-5">C.A.T.S.</h1>
	<h1 class="mb-5">Camera Assisted Tracking System</h1>
	
	<div class="block self-center content-center max-w-lg p-6 bg-white border border-gray-200 rounded-lg shadow hover:bg-gray-100">	
		<h5 class="mb-2 text-2xl font-bold tracking-tight text-gray-900">Recent Events</h5>
		<div id="list">
			<ul>
			{#each images as image}
			<li>
				<!-- <img src="{image.path}" alt="Cat!" /> -->
				<img src="{image.path}" alt="Cat!" class="max-w-md"/>
				<h6 class="font-bold">Date from Object ID: </h6>{dateFromObjectId(image._id)}
				<h6> Detected Object: {image['object-detected']} </h6>
				<br/>
			</li>
			{/each}
			</ul>
		</div> 
	</div>
	
	
</section>

{:else}
<section class= "flex flex-col justify-items-center align-middle self-center py-10">
	<h1 class="mt-5">C.A.T.S.</h1>
	<h1 class="mb-5">Camera Assisted Tracking System</h1>
	
	<Button class="w-32 self-center no-underline" href="/pricing">Get Started</Button>
	
</section>

<section>
	<div class="grid grid-cols-3 gap-4 pt-4">
		<div>
		<Card>
			<!-- <img src="https://github.com/A-very-Cunning-ham/CATS/blob/05a2d3bb2812f50ffc184626686bd4ec054c6349/meow/src/lib/images/cats/cat1.jpg" alt="cat"/> -->
			<h5 class="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white">What We Do</h5>
			<p class="mb-3 font-normal text-gray-700 dark:text-gray-400 leading-tight">
				Trap-Neuter-Return (TNR) is the humane approach to addressing community cat populations. In a TNR program, stray cats are humanely trapped, spayed or neutered, vaccinated, eartipped, and then returned to their outdoor home. However, TNR is labor intensive and expensive, with workers having to manually find and trap large populations of cats that are elusive by nature. We at CATS hope to solve that.			</p>
			<Button color="dark" class="w-40 mt-2" href="https://www.alleycat.org/our-work/trap-neuter-return/" target="_blank" rel="noreferrer noopener">
				Read more <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-5 h-5 ml-2"><path stroke-linecap="round" stroke-linejoin="round" d="M13.5 4.5L21 12m0 0l-7.5 7.5M21 12H3" /></svg>
			</Button>
		</Card>
		</div>
		<div>
		<Card>
			<h5 class="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white">How We Do It</h5>
			<p class="font-normal text-gray-700 dark:text-gray-400 leading-tight">
				Our solution is an AI tracking camera system that intelligently identifies and provides insights on stray cat populations in a given community. This automated tracking will reduce costs dramatically and it simplifies the work of animal control shelters. An integrated User Interface on a website built by us will provide centralized tracking, data analysis and insights into key metrics.
			</p>
		</Card>
		</div>
		<div>
		<Card>
			<h5 class="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white">Value Proposition</h5>
			<p class="font-normal text-gray-700 dark:text-gray-400 leading-tight">
				By significantly reducing the amount of time spent in the field, C.A.T.S. allows humans to get back to making a real difference in their communities. Interviews that our team has conducted with real world TNR workers further validates these claims, revealing that there is no real alternative to our product, that this would make life much easier for the workers, and that it would create immediate value with data reporting for use in pitch presentations that lead to more funding. 
			</p>
		</Card>
		</div>
	</div>
</section>
{/if}

<style>

</style>
