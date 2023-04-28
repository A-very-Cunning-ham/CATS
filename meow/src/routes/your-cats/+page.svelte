<script lang='ts'>
	import { Button, Helper, Label, Input, Modal, Table, TableBody, TableBodyCell, TableBodyRow, TableHead, TableHeadCell, Checkbox, TableSearch, Select } from 'flowbite-svelte';
	import { cat } from '$lib/stores/store.js'
	import type { PageData } from './$types';
	
	export let data: PageData

	import { invalidateAll } from '$app/navigation';
	
	var dateFromObjectId = function (objectId) {
		return new Date(parseInt(objectId.toString().substring(0, 8), 16) * 1000).toLocaleString('en-US', { timeZone: 'UTC' });
	};

	$: ({images} = data)

	let newCatModal = false;
	let editing = false;

	function restart() {
		//unique = {} // every {} is unique, {} === {} evaluates to false
		invalidateAll();
	}
    
</script>

<svelte:head>
	<title>Your Cats</title>
	<meta name="description" content="Analytics" />
</svelte:head>

<div class="flex flex-col justify-between align-middle">
    <div>
		<h1>Your Cats</h1>
		<div class="flex justify-center self-center">
			<!--<p>Site {images[0].camera}</p>-->
			<div></div>
			
		</div>
		<Button class="mb-3 p-6 self-center no-underline" on:click={restart}>Load New Data</Button>
		
		<br/>
		{#if !editing}
		<Table hoverable shadow>
			<TableHead>
			  <TableHeadCell>Name/ID</TableHeadCell>
			  <TableHeadCell>Date Last Seen</TableHeadCell>
			  <TableHeadCell>Age (in Months)</TableHeadCell>
			  <TableHeadCell>Weight (in Pounds)</TableHeadCell>
			  <TableHeadCell>Ear Tipped</TableHeadCell>	
			  <TableHeadCell></TableHeadCell>		
			</TableHead>
			<TableBody >
			{#each images as image}
				<TableBodyRow>
				<TableBodyCell>{image.name}</TableBodyCell>
				
				{#if image.events[0]}
					<TableBodyCell>{dateFromObjectId(image.events[0])}</TableBodyCell>
				{:else}
					<TableBodyCell>-</TableBodyCell>
				{/if}

				<TableBodyCell>{image.age}</TableBodyCell>
				<TableBodyCell>{image.weight}</TableBodyCell>
				<TableBodyCell>{image.neutered}</TableBodyCell>
				<TableBodyCell><a href="/your-cats/cat-details" on:click={()=> cat.set(image)}>Details</a></TableBodyCell>
			  </TableBodyRow>
			  {/each}
			</TableBody>
		</Table>
		<div class="flex gap-3 justify-end py-6">
			<Button outline color="red" on:click={()=> editing=true}>Edit List</Button>
		</div>
		{:else}


		<Table hoverable shadow striped>
			<TableHead>
				<TableHeadCell></TableHeadCell>
				<TableHeadCell>Name/ID</TableHeadCell>
				<TableHeadCell>Date Last Seen</TableHeadCell>
				<TableHeadCell>Age (in Months)</TableHeadCell>
				<TableHeadCell>Weight (in Pounds)</TableHeadCell>
				<TableHeadCell>Ear Tipped</TableHeadCell>	
				<TableHeadCell></TableHeadCell>		
			</TableHead>
			<TableBody >
			{#each images as image}
				<TableBodyRow>
				<TableBodyCell><Checkbox /></TableBodyCell>
				<TableBodyCell>{image.name}</TableBodyCell>
				<!-- <TableBodyCell>{dateFromObjectId(image.events[0])}</TableBodyCell> -->
				{#if image.events[0]}
				<TableBodyCell>{dateFromObjectId(image.events[0])}</TableBodyCell>
			{:else}
				<TableBodyCell>-</TableBodyCell>
			{/if}
				<TableBodyCell>{image.age}</TableBodyCell>
				<TableBodyCell>{image.weight}</TableBodyCell>
				<TableBodyCell>{image.neutered}</TableBodyCell>
				<!-- <TableBodyCell><a href="/your-cats/cat-details" on:click={()=>cat.set(image)}>Details</a></TableBodyCell> -->
				<TableBodyCell>
					<form method="POST" action="?/delete">
						<input type="hidden" name="id" hidden value={image._id} />
						<button class="btn text-red-700 btn-error btn-xs">Delete</button>
					</form>
				</TableBodyCell>
			</TableBodyRow>
			{/each}
			</TableBody>
		</Table>


		<div class="flex gap-3 justify-end py-6">
			<Button color="green" outline on:click={()=> newCatModal=true} ><svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-5 h-5 mr-1"><path stroke-linecap="round" stroke-linejoin="round" d="M19 7.5v3m0 0v3m0-3h3m-3 0h-3m-2.25-4.125a3.375 3.375 0 11-6.75 0 3.375 3.375 0 016.75 0zM4 19.235v-.11a6.375 6.375 0 0112.75 0v.109A12.318 12.318 0 0110.374 21c-2.331 0-4.512-.645-6.374-1.766z" /></svg>Add New Cat</Button>
			<Modal title="New Cat Registration"  open={newCatModal} >
				<form class="flex flex-col space-y-6" method="POST" action="?/create">
					<label class="space-y-2 text-xl">
						<span>Name</span>
						<input name="name" placeholder="Oreo" required class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"/>
					</label>
					
					<div class="flex gap-6 justify-between">
						<label class="space-y-2 text-xl">
							<span>Age</span>
							<input type="number" name="age" placeholder="24" class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"/>
							<Helper class="text-sm">Approximate age in months</Helper>
						</label>
						<label class="space-y-2 text-xl">
							<span>Weight</span>
							<input type="number" name="weight" placeholder="5" class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"/>
							<Helper class="text-sm">Weight in lbs</Helper>
						</label>
						<label class="space-y-2 text-xl">
							<span>Eartipped?</span>
							<select class="block shadow appearance-none w-full border border-gray-200 text-gray-700 py-2 px-3 rounded leading-tight focus:outline-none focus:bg-white focus:border-gray-500" name="neutered" required>
								<option value="Y">Yes</option>
								<option value="N">No</option>	
								<option value="Undefined">Unsure</option>	
							</select>
							<input type="hidden">
						</label>
					</div>
					<button class="shadow bg-blue-500 focus:shadow-outline focus:outline-none text-white font-bold py-2 px-4 rounded">Submit</button>
					<div class="text-sm font-medium text-gray-500 dark:text-gray-300">
						Leave fields blank if unsure.
					</div>
				</form>
			</Modal>

			<Button color="red" on:click={()=> editing=false}>Confirm Changes</Button>
		</div>
		{/if}
	</div>
</div>