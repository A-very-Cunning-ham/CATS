<script lang='ts'>
	import { Table, TableBody, TableBodyCell, TableBodyRow, TableHead, TableHeadCell, Checkbox, TableSearch } from 'flowbite-svelte';
	import type { PageData } from './$types';
	export let data: PageData
	
	var dateFromObjectId = function (objectId) {
	return new Date(parseInt(objectId.substring(0, 8), 16) * 1000).toLocaleString('en-US', { timeZone: 'UTC' });
	};

	$: ({images} = data)
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
		</div>
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
				<TableBodyCell>04-06-2023</TableBodyCell>
				<TableBodyCell>08</TableBodyCell>
				<TableBodyCell>Y</TableBodyCell>
				<TableBodyCell><a href="/your-cats/cat-details">Details</a></TableBodyCell>
			  </TableBodyRow>
			  {/each}
			</TableBody>
		  </Table>
	</div>
</div>