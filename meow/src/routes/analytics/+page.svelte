<script lang='ts'>
	import { Table, TableBody, TableBodyCell, TableBodyRow, TableHead, TableHeadCell } from 'flowbite-svelte';
	import type { PageData } from './$types';
	import { user } from '$lib/stores/store';
	import { Button } from 'flowbite-svelte'; 
	import Chart from 'svelte-frappe-charts';
	import { DateInput } from 'date-picker-svelte';
	export let data: PageData
	import { ExportToCsv } from 'export-to-csv';
	import { restart, dateFromObjectId } from '../Utilities';
	
	const userInfo = JSON.parse(JSON.stringify($user))

	let dateRanger1 = new Date(new Date().setDate(new Date().getDate() - 7))
	dateRanger1.setHours(0,0,0)
	let dateRanger2 = new Date()
	dateRanger2.setHours(23,59,59)

	$: ({images} = data)

	let images_perm = data

	const datesAreOnSameDay = (first, second) =>
		first.getFullYear() === second.getFullYear() &&
		first.getMonth() === second.getMonth() &&
		first.getDate() === second.getDate();
	
	let days: Date[] = []

	for (let i: number = 0; i < images_perm.images.length; i++) {
		images_perm.images[i].date = new Date(dateFromObjectId(images_perm.images[i]._id))
		days.push(images_perm.images[i].date)
	}

	days.reverse()

	let start_date = dateRanger1
	
	console.log("Days with cats: ")
	console.log(days)

	let days_graph: Date[] = []

	while (start_date <= dateRanger2) {
		days_graph.push(new Date(start_date))
		start_date.setDate(start_date.getDate() + 1)
	}

	let days_graph_string: String[] = []
	
	for(let x: number = 0; x < days_graph.length; x++){
		days_graph_string.push(days_graph[x].toLocaleString().split(',')[0])
	}

	console.log("Days on graph")

	console.log(days_graph)

	let cat_days = [new Array(days_graph.length).fill(0), days_graph]

	for(let i: number = 0; i < cat_days[0].length; i++){
		for(let j: number = 0; j < days.length; j++){
			if(datesAreOnSameDay(days[j], cat_days[1][i])){
				cat_days[0][i] += 1
			}
		}
	}

	console.log(cat_days)
	
	//console.log(images_perm.images)
	let chartRef;

	const onExport = () => chartRef.exportChart();

	let data1 = {
		axisOptions: {
			xAxisMode: 'tick' // default: 'span'
		},
		labels: days_graph_string,
		datasets: [
			{
			values: cat_days[0]
			}
		]
	};

	function updateRange() {
		console.log("Updating range")
		console.log(dateRanger1)
		console.log(dateRanger2)

		let start_date = dateRanger1
	
		console.log("Days with cats: ")
		console.log(days)

		let days_graph: Date[] = []

		while (start_date <= dateRanger2) {
			days_graph.push(new Date(start_date))
			start_date.setDate(start_date.getDate() + 1)
		}

		let days_graph_string: String[] = []
		
		for(let x: number = 0; x < days_graph.length; x++){
			days_graph_string.push(days_graph[x].toLocaleString().split(',')[0])
		}

		console.log("Days on graph")

		console.log(days_graph)

		let cat_days = [new Array(days_graph.length).fill(0), days_graph]

		for(let i: number = 0; i < cat_days[0].length; i++){
			for(let j: number = 0; j < days.length; j++){
				if(datesAreOnSameDay(days[j], cat_days[1][i])){
					cat_days[0][i] += 1
				}
			}
		}

		console.log(cat_days)
		
		//console.log(images_perm.images)
		let chartRef;

		const onExport = () => chartRef.exportChart();

		data1 = {
		axisOptions: {
			xAxisMode: 'tick' // default: 'span'
		},
		labels: days_graph_string,
		datasets: [
			{
			values: cat_days[0]
			}
		]
		};
		
	}

	function export_csv() {
		const csvExporter = new ExportToCsv({
			filename: 'Cats' + new Date(),
			fieldSeparator: ',',
			quoteStrings: '"',
			decimalSeparator: '.',
			showLabels: true,
			showTitle: true,
			title: 'Cats',
			useTextFile: false,
			useBom: true,
			useKeysAsHeaders: true,
		});

		csvExporter.generateCsv(data1);
	}
</script>

<svelte:head>
	<title>Analytics</title>
	<meta name="description" content="Analytics" />
</svelte:head>

<section class= "flex flex-col justify-center mb-12">

	<h1 class="py-5">Welcome Back, {userInfo.given_name}!</h1>
	<Button class="w-32 self-center no-underline" on:click={restart}>Load New Data</Button>
	<span class="flex flex-col justify-center items-center py-6">
		<p class="font-semibold text-2xl">
			Site {images_perm.images[0].camera}
		</p>
		<p class="text-xl">
			Cats detected (per day)
		</p>
		Start Date <DateInput bind:value={dateRanger1} />
		End Date <DateInput bind:value={dateRanger2} />
		<br>
		<Button class="w-32 self-center no-underline" on:click={updateRange}>Update Range</Button>
	</span>

		<Chart data={data1} type="bar" bind:this={chartRef}/>
	<span class="flex flex-col justify-center items-center py-6">
		<Button class="w-16" on:click={onExport}>Export Graph</Button>
	</span>
</section>

<section class="mb-12">
	
<div class="flex flex-col justify-between align-middle">
    <div>
		<h1>Details</h1>
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
				<TableBodyCell><a href="/your-cats/cat-details">Snapshot</a></TableBodyCell>
			  </TableBodyRow>
			  <TableBodyRow>
				<TableBodyCell>03-05-2023</TableBodyCell>
				<TableBodyCell>Site 1</TableBodyCell>
				<TableBodyCell>12</TableBodyCell>
				<TableBodyCell>08/12</TableBodyCell>
				<TableBodyCell>07/12</TableBodyCell>
				<TableBodyCell><a href="/your-cats/cat-details">Snapshot</a></TableBodyCell>
			  </TableBodyRow>
			  <TableBodyRow>
				<TableBodyCell>03-04-2023</TableBodyCell>
				<TableBodyCell>Site 1</TableBodyCell>
				<TableBodyCell>10</TableBodyCell>
				<TableBodyCell>07/10</TableBodyCell>
				<TableBodyCell>05/10</TableBodyCell>
				<TableBodyCell><a href="/your-cats/cat-details">Snapshot</a></TableBodyCell>
			  </TableBodyRow>
			  <TableBodyRow>
				<TableBodyCell>03-03-2023</TableBodyCell>
				<TableBodyCell>Site 1</TableBodyCell>
				<TableBodyCell>11</TableBodyCell>
				<TableBodyCell>07/11</TableBodyCell>
				<TableBodyCell>06/11</TableBodyCell>
				<TableBodyCell><a href="/your-cats/cat-details">Snapshot</a></TableBodyCell>
			  </TableBodyRow>
			  <TableBodyRow>
				<TableBodyCell>03-02-2023</TableBodyCell>
				<TableBodyCell>Site 1</TableBodyCell>
				<TableBodyCell>12</TableBodyCell>
				<TableBodyCell>05/12</TableBodyCell>
				<TableBodyCell>05/12</TableBodyCell>
				<TableBodyCell><a href="/your-cats/cat-details">Snapshot</a></TableBodyCell>
			  </TableBodyRow>
			  <TableBodyRow>
				<TableBodyCell>03-01-2023</TableBodyCell>
				<TableBodyCell>Site 1</TableBodyCell>
				<TableBodyCell>07</TableBodyCell>
				<TableBodyCell>05/07</TableBodyCell>
				<TableBodyCell>03/07</TableBodyCell>
				<TableBodyCell><a href="/your-cats/cat-details">Snapshot</a></TableBodyCell>
			  </TableBodyRow>
			  <TableBodyRow>
				<TableBodyCell>02-28-2023</TableBodyCell>
				<TableBodyCell>Site 1</TableBodyCell>
				<TableBodyCell>10</TableBodyCell>
				<TableBodyCell>04/10</TableBodyCell>
				<TableBodyCell>04/10</TableBodyCell>
				<TableBodyCell><a href="/your-cats/cat-details">Snapshot</a></TableBodyCell>
			  </TableBodyRow>
			  <TableBodyRow>
				<TableBodyCell>02-27-2023</TableBodyCell>
				<TableBodyCell>Site 1</TableBodyCell>
				<TableBodyCell>09</TableBodyCell>
				<TableBodyCell>03/09</TableBodyCell>
				<TableBodyCell>04/09</TableBodyCell>
				<TableBodyCell><a href="/your-cats/cat-details">Snapshot</a></TableBodyCell>
			  </TableBodyRow>
			</TableBody>
		  </Table>
	</div>
</div>
</section>

<style>
	.box {
		width: 300px;
		background-color: white;
		border: 1px solid rgb(170, 170, 170);
		border-radius: 20px;
		box-shadow: 2px 2px 8px rgba(0,0,0,0.1);
		padding: 3em;
		margin: 4px 4px 4px 4px;
	}

	.chart {
		width: 100%;
		max-width: 500px;
		margin: 0 auto;
	}

	svg {
		position: relative;
		width: 100%;
		height: 200px;
	}

	.tick {
		font-family: Helvetica, Arial;
		font-size: .6em;
		font-weight: 200;
	}

	.tick line {
		stroke: #e2e2e2;
		stroke-dasharray: 2;
	}

	.tick text {
		fill: #000000;
		text-anchor: start;
	}

	.tick.tick-0 line {
		stroke-dasharray: 0;
	}

	.x-axis .tick text {
		text-anchor: middle;
	}

	.bars rect {
		fill: #a11;
		stroke: none;
		opacity: 0.65;
	}

</style>