<script>
	import { Table, TableBody, TableBodyCell, TableBodyRow, TableHead, TableHeadCell, Checkbox, TableSearch } from 'flowbite-svelte';
</script>

<svelte:head>
	<title>Analytics</title>
	<meta name="description" content="Analytics" />
</svelte:head>

<div class="flex flex-col justify-between align-middle">
    <div>
		<h1>Analytics</h1>
		<br/>
		<Table>
			<TableHead>
			  <TableHeadCell>Cat ID</TableHeadCell>
			  <TableHeadCell>Date Last Seen</TableHeadCell>
			  <TableHeadCell>Location</TableHeadCell>
			  <TableHeadCell>Age</TableHeadCell>
			  <TableHeadCell></TableHeadCell>
			</TableHead>
			<TableBody >
			  <TableBodyRow>
				<TableBodyCell>#37395462839471</TableBodyCell>
				<TableBodyCell>02-13-2023</TableBodyCell>
				<TableBodyCell>Site 53</TableBodyCell>
				<TableBodyCell>Adult</TableBodyCell>
				<TableBodyCell><a href="/analytics/cat-details">View More Data</a></TableBodyCell>
			  </TableBodyRow>
			  <TableBodyRow>
				<TableBodyCell>#59027495937438</TableBodyCell>
				<TableBodyCell>02-11-2023</TableBodyCell>
				<TableBodyCell>Site 51</TableBodyCell>
				<TableBodyCell>Adult</TableBodyCell>
				<TableBodyCell><a href="/analytics/cat-details">View More Data</a></TableBodyCell>
			  </TableBodyRow>
			  <TableBodyRow>
				<TableBodyCell>#12947202837584</TableBodyCell>
				<TableBodyCell>02-10-2023</TableBodyCell>
				<TableBodyCell>Site 78</TableBodyCell>
				<TableBodyCell>Kitten</TableBodyCell>
				<TableBodyCell><a href="/analytics/cat-details">View More Data</a></TableBodyCell>
			  </TableBodyRow>
			  <TableBodyRow>
				<TableBodyCell>#73629592798392</TableBodyCell>
				<TableBodyCell>02-10-2023</TableBodyCell>
				<TableBodyCell>Site 18</TableBodyCell>
				<TableBodyCell>Adolescent</TableBodyCell>
				<TableBodyCell><a href="/analytics/cat-details">View More Data</a></TableBodyCell>
			  </TableBodyRow>
			</TableBody>
		  </Table>
	</div>
</div>