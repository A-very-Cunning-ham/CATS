<script lang='ts'>
	import { ButtonGroup, Table, TableBody, TableBodyCell, TableBodyRow, TableHead, TableHeadCell, Dropzone, Checkbox, TableSearch } from 'flowbite-svelte';
	import type { PageData } from './$types';
	import { scaleBand } from 'd3-scale';
	import { user } from '$lib/stores/store';
	import { Input, Button, Datepicker } from 'flowbite-svelte'; 
	import Chart from 'svelte-frappe-charts';
	import { invalidateAll } from '$app/navigation';
	import { DateInput } from 'date-picker-svelte';
	export let data: PageData
	import { ExportToCsv } from 'export-to-csv';

	function restart() {
		invalidateAll();
	}
	
	const userInfo = JSON.parse(JSON.stringify($user))

	let dateRanger1 = new Date(new Date().setDate(new Date().getDate() - 7))
	dateRanger1.setHours(0,0,0)
	let dateRanger2 = new Date()
	dateRanger2.setHours(23,59,59)

	$: ({images} = data)

	let images_perm = data

	var dateFromObjectId = function (objectId) {
		return new Date(parseInt(objectId.substring(0, 8), 16) * 1000);
	};

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
	<span class="flex flex-col justify-center items-center py-6">
		<p class="font-semibold text-2xl">
			Site {images_perm.images[0].camera}
		</p>
		<p class="text-xl">
			Cats detected (per day)
		</p>
	</span>

		<Chart data={data1} type="bar" bind:this={chartRef}/>
		<div class="flex gap-4 py-6 self-center">	
			<div>
			Start Date <DateInput bind:value={dateRanger1} />
			</div>
			<div>
			End Date <DateInput bind:value={dateRanger2} />
			</div>
		</div>
		<Button class="self-center no-underline" on:click={updateRange}>Update Range</Button>
	
	<span class="flex justify-center py-6">
		<ButtonGroup class="space-x-px">
		<Button class="self-center no-underline" color="blue" on:click={restart}>Load New Data</Button>
		<Button class="" color="blue" on:click={onExport}>Export Graph</Button>
		<Button class="" color="blue" on:click={export_csv}>Export CSV</Button>
		</ButtonGroup>
	</span>

		<!-- <div class="chart" bind:clientWidth={width} bind:clientHeight={height}>
			<svg>
				 y axis 
				<g class="axis y-axis">
					{#each yTicks as tick}
						<g class="tick tick-{tick}" transform="translate(0, {yScale(tick)})">
							<line x2="100%"></line>
							<text y="-4">{tick} {tick === 20 ? ' per 1,000 population' : ''}</text>
						</g>
					{/each}
				</g>
		
				 x axis 
				<g class="axis x-axis">
					{#each points as point, i}
						<g class="tick" transform="translate({xScale(i)},{height})">
							<text x="{barWidth/2}" y="-4">{width > 380 ? point.date : formatMobile(point.date)}</text>
						</g>
					{/each}
				</g>
		
				<g class='bars'>
					{#each points as point, i}
						<rect
							x="{xScale(i) + 2}"
							y="{yScale(point.cats)}"
							width="{barWidth - 4}"
							height="{yScale(0) - yScale(point.cats)}"
						></rect>
					{/each}
				</g>
			</svg>
		</div> -->
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

<!-- <section>
	<div>
		<h1>Upload Trail Cam Footage</h1>
		<br/>
		<Dropzone>
			<svg aria-hidden="true" class="mb-3 w-10 h-10 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12"></path></svg>
  			<p class="mb-2 text-sm text-gray-500 dark:text-gray-400"><span class="font-semibold">Click to upload</span> or drag and drop</p>
  			<p class="text-xs text-gray-500 dark:text-gray-400">SVG, PNG, JPG or GIF (MAX. 800x400px)</p>
		</Dropzone>
	</div>
</section> -->

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