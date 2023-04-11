<script lang='ts'>
	import {onMount} from 'svelte';
	import { isAuthenticated, user } from '$lib/stores/store';
	import { Button, Card, Checkbox, Dropdown, Modal, Search, Label, Input, Select, Helper } from 'flowbite-svelte';
	import Video from './Video.svelte';
	import type { Action, Actions, PageData } from './$types';
	export let data: PageData
	import { invalidateAll } from '$app/navigation';
	
	var dateFromObjectId = function (objectId) {
		return new Date(parseInt(objectId.substring(0, 8), 16) * 1000).toLocaleString('en-US', { timeZone: 'UTC' });
	};

	$: ({images} = data)

	let detectedCats = 1;
	let recognized = 0;
	let unrecognized = 1;

	let open = false;

	let newCatModal = false;

	let imagesrc;

	let selected;
	let options = [
		{value:"Y", name:"Yes"},
		{value:"N", name:"No"},
		{value:"-", name:"Unsure"},
	]

	function restart() {
		//unique = {} // every {} is unique, {} === {} evaluates to false
		invalidateAll();
	}

	async function addNewCat(e){
		const formData = new FormData(e.target);

		const data = {};
		
		for (let field of formData) {
			const [key, value] = field;
			data[key] = value;
		}
		
		const result = await images.insertOne(e)
		return result
	}
  
</script>

<svelte:head>
	<title>Home</title>
	<meta name="description" content="CATS demo app" />
</svelte:head>

{#if $isAuthenticated}

<section class= "flex flex-col self-center">
	<h1 class="mt-5">C.A.T.S.</h1>
	<h1 class="mb-5">Camera Assisted Tracking System</h1>

	<div class="flex flex-col items-center mb-5">	
		<h5 class="mb-6 text-2xl font-bold tracking-tight text-gray-900">Live Video Feed</h5>
		<Video/>
	</div>
	<div class="flex flex-col items-center">	
		<h5 class="mb-6 text-2xl font-bold tracking-tight text-gray-900">Recent Events</h5>
		<Button class="w-32 self-center no-underline" on:click={restart}>Load New Images</Button>
		<div>
			___________________________
		</div>
		<div id="list">
			<ul class="grid grid-cols-2 gap-6">
			{#each images as image}
			{#if image['type'] == 'image'}
			<li>
				<Card class="flex flex-col gap-6 justify-between self-center content-center p-6 bg-white border border-gray-200 rounded-lg shadow hover:bg-gray-100 hover:no-underline min-h-full">
				<img src="{image.path}" alt="Cat!" class="object-cover max-h-64"/>
				<div>
					<h6 class="font-bold">Time Detected: </h6>
					<h6>{dateFromObjectId(image._id)}</h6>
					<div class="flex gap-2">
					<h6 class="font-bold"> Detected Object: </h6>
					<h6> {image['object-detected']} </h6>
					</div>
				</div>
				<Button on:click={() => {imagesrc=image.path; open = true}}>Review Image</Button>
				<Modal title="Manual Tagging" size="xl" imageFromData={imagesrc} bind:open={open}>
					<div class="flex gap-4">
						<img src={imagesrc} alt="Cat!" class="object-cover max-h-64"/>
						<div class="flex flex-col gap-4">
							<p>Detected Cats: {detectedCats}</p>
							<p>Recognized: {recognized}</p>
							<p>Unrecognized: {unrecognized}</p>
							<Button class="max-w-min">Tag</Button>
							<Dropdown placement="right" class="p-3 space-y-1 text-sm overflow-y-auto h-48">
								<div slot="header" class="p-3">
									<Search size="md"/>
								</div>
								{#each images as image}
								{#if image['type'] == 'cat'}
								<li class="rounded p-2 hover:bg-gray-100 dark:hover:bg-gray-600">
								  <Checkbox>{image.name}</Checkbox>
								</li>
								{/if}
								{/each}
								<a slot="footer" on:click={()=>newCatModal=true} class="flex items-center p-3 -mb-1 text-sm font-medium text-green-600 bg-gray-50 hover:bg-gray-100 dark:bg-gray-700 dark:hover:bg-gray-600 dark:text-red-500 hover:underline">
									<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-5 h-5 mr-1"><path stroke-linecap="round" stroke-linejoin="round" d="M19 7.5v3m0 0v3m0-3h3m-3 0h-3m-2.25-4.125a3.375 3.375 0 11-6.75 0 3.375 3.375 0 016.75 0zM4 19.235v-.11a6.375 6.375 0 0112.75 0v.109A12.318 12.318 0 0110.374 21c-2.331 0-4.512-.645-6.374-1.766z" /></svg>
									Add New Cat
								</a>
							</Dropdown>
						</div>	
					</div>
	
					<svelte:fragment slot='footer'>
						<Button on:click={()=> open=false}>Save Changes</Button>
						<Button color="alternative" on:click={()=> open=false}>Discard Changes</Button>
					</svelte:fragment>
				</Modal>	
				</Card>
			</li>
			{/if}
			{/each}
			</ul>
			<Modal title="New Cat Registration" bind:open={newCatModal} autoclose size="lg">
				<form class="flex flex-col space-y-6" on:submit|preventDefault>
					<!-- <h3 class="text-xl font-medium text-gray-900 dark:text-white p-0">Sign in to our platform</h3> -->
					<Label class="space-y-2 text-xl">
						<span>Name</span>
						<Input name="name" placeholder="Oreo" value="" required />
					</Label>
					
					<div class="flex gap-6 justify-between">
						<Label class="space-y-2 text-xl">
							<span>Age</span>
							<Input type="number" name="age" value="" placeholder="24"/>
							<Helper class="text-sm">Approximate age in months</Helper>
						</Label>
						<Label class="space-y-2 text-xl">
							<span>Weight</span>
							<Input type="number" name="weight" value="" placeholder="5" />
							<Helper class="text-sm">Weight in lbs</Helper>
						</Label>
						<Label class="space-y-2 text-xl">
							<span>Eartipped?</span>
							<Select class="mt-2 border-none" items={options} bind:value={selected} required/></Label>
					</div>
					<Button type="submit" on:click={()=> newCatModal=false}>Submit</Button>
					<div class="text-sm font-medium text-gray-500 dark:text-gray-300">
						Leave fields blank if unsure.
					</div>
				  </form>
			</Modal>
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
