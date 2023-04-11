<script lang='ts'>
	import { Table, TableBody, TableBodyCell, TableBodyRow, TableHead, TableHeadCell, Checkbox, TableSearch } from 'flowbite-svelte';
	import type { PageData } from './$types';
	export let data: PageData
	import { invalidateAll } from '$app/navigation';
	import { Button } from 'flowbite-svelte';
	
	var dateFromObjectId = function (objectId) {
		return new Date(parseInt(objectId.substring(0, 8), 16) * 1000).toLocaleString('en-US', { timeZone: 'UTC' });
	};

	$: ({images} = data)

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
			<p>Camera 1</p>
			<div></div>
			
		</div>
		<Button class="w-32 self-center no-underline" on:click={restart}>Load New Data</Button>
		<br/>
		<Table>
			<TableHead>
			  <TableHeadCell>Name/ID</TableHeadCell>
			  <TableHeadCell>Date Last Seen</TableHeadCell>
			  <TableHeadCell>Total Times Seen</TableHeadCell>
			  <TableHeadCell>Ear Tipped</TableHeadCell>	
			  <TableHeadCell></TableHeadCell>		
			</TableHead>
			<TableBody >
			{#each images as image}
				<TableBodyRow>
				<TableBodyCell>{image._id}</TableBodyCell>
				<TableBodyCell>{dateFromObjectId(image._id)}</TableBodyCell>
				<TableBodyCell></TableBodyCell>
				<TableBodyCell></TableBodyCell>
				<TableBodyCell><a href="/your-cats/cat-details">Details</a></TableBodyCell>
			  </TableBodyRow>
			  {/each}
			</TableBody>
		  </Table>
	</div>
</div>