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
		<div class="flex justify-center self-center">
			<p>Camera 1</p>
		</div>
		<br/>
		<Table>
			<TableHead>
			  <TableHeadCell>Date</TableHeadCell>
			  <TableHeadCell>Location</TableHeadCell>
			  <TableHeadCell>Total Visits</TableHeadCell>
			  <TableHeadCell>Face Recognized</TableHeadCell>
			  <TableHeadCell>Ear Tipped</TableHeadCell>	
			  <TableHeadCell></TableHeadCell>		
			</TableHead>
			<TableBody >
			  <TableBodyRow>
				<TableBodyCell>03-06-2023</TableBodyCell>
				<TableBodyCell>Site 1</TableBodyCell>
				<TableBodyCell>08</TableBodyCell>
				<TableBodyCell>08/08</TableBodyCell>
				<TableBodyCell>07/08</TableBodyCell>
				<TableBodyCell><a href="/analytics/cat-details">Snapshot</a></TableBodyCell>
			  </TableBodyRow>
			  <TableBodyRow>
				<TableBodyCell>03-05-2023</TableBodyCell>
				<TableBodyCell>Site 1</TableBodyCell>
				<TableBodyCell>12</TableBodyCell>
				<TableBodyCell>08/12</TableBodyCell>
				<TableBodyCell>07/12</TableBodyCell>
				<TableBodyCell><a href="/analytics/cat-details">Snapshot</a></TableBodyCell>
			  </TableBodyRow>
			  <TableBodyRow>
				<TableBodyCell>03-04-2023</TableBodyCell>
				<TableBodyCell>Site 1</TableBodyCell>
				<TableBodyCell>10</TableBodyCell>
				<TableBodyCell>07/10</TableBodyCell>
				<TableBodyCell>05/10</TableBodyCell>
				<TableBodyCell><a href="/analytics/cat-details">Snapshot</a></TableBodyCell>
			  </TableBodyRow>
			  <TableBodyRow>
				<TableBodyCell>03-03-2023</TableBodyCell>
				<TableBodyCell>Site 1</TableBodyCell>
				<TableBodyCell>11</TableBodyCell>
				<TableBodyCell>07/11</TableBodyCell>
				<TableBodyCell>06/11</TableBodyCell>
				<TableBodyCell><a href="/analytics/cat-details">Snapshot</a></TableBodyCell>
			  </TableBodyRow>
			  <TableBodyRow>
				<TableBodyCell>03-02-2023</TableBodyCell>
				<TableBodyCell>Site 1</TableBodyCell>
				<TableBodyCell>12</TableBodyCell>
				<TableBodyCell>05/12</TableBodyCell>
				<TableBodyCell>05/12</TableBodyCell>
				<TableBodyCell><a href="/analytics/cat-details">Snapshot</a></TableBodyCell>
			  </TableBodyRow>
			  <TableBodyRow>
				<TableBodyCell>03-01-2023</TableBodyCell>
				<TableBodyCell>Site 1</TableBodyCell>
				<TableBodyCell>07</TableBodyCell>
				<TableBodyCell>05/07</TableBodyCell>
				<TableBodyCell>03/07</TableBodyCell>
				<TableBodyCell><a href="/analytics/cat-details">Snapshot</a></TableBodyCell>
			  </TableBodyRow>
			  <TableBodyRow>
				<TableBodyCell>02-28-2023</TableBodyCell>
				<TableBodyCell>Site 1</TableBodyCell>
				<TableBodyCell>10</TableBodyCell>
				<TableBodyCell>04/10</TableBodyCell>
				<TableBodyCell>04/10</TableBodyCell>
				<TableBodyCell><a href="/analytics/cat-details">Snapshot</a></TableBodyCell>
			  </TableBodyRow>
			  <TableBodyRow>
				<TableBodyCell>02-27-2023</TableBodyCell>
				<TableBodyCell>Site 1</TableBodyCell>
				<TableBodyCell>09</TableBodyCell>
				<TableBodyCell>03/09</TableBodyCell>
				<TableBodyCell>04/09</TableBodyCell>
				<TableBodyCell><a href="/analytics/cat-details">Snapshot</a></TableBodyCell>
			  </TableBodyRow>
			</TableBody>
		  </Table>
	</div>
</div>