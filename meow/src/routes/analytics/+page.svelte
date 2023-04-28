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

	var dateFromObjectId2 = function (objectId) {
		return new Date(parseInt(objectId.substring(0, 8), 16) * 1000).toLocaleString('en-US', { timeZone: 'UTC' });
	};
	
	const userInfo = JSON.parse(JSON.stringify($user))

	let dateRanger1 = new Date(new Date().setDate(new Date().getDate() - 7))
	dateRanger1.setHours(0,0,0)
	let dateRanger2 = new Date()
	dateRanger2.setHours(23,59,59)

	$: ({images} = data)

	let images_perm = data

	let images_perm2 = {images: []}

	let images_perm3 = {images: []}

	for (let i: number = 0; i < images_perm.images.length; i++) {
		if (images_perm.images[i].type == "cat") {
			images_perm2.images.push(images_perm.images[i])
		}
	}

	for (let i: number = 0; i < images_perm.images.length; i++) {
		if (images_perm.images[i].type == "image") {
			images_perm3.images.push(images_perm.images[i])
		}
	}
	
	console.log('images_perm2')
	console.log(images_perm2)

	for (let i: number = 0; i < images_perm3.images.length; i++) {
		images_perm3.images[i].catIDs[0] = 0
		images_perm3.images[i].catIDs[1] = 0
		images_perm3.images[i].catIDs[2] = "Y"
		for (let k: number = 0; k < images_perm3.images[i]['objects-found'].length; k++) {
			if (images_perm3.images[i]['objects-found'][k].class == "Cat Ear") {
				images_perm3.images[i].catIDs[0] = images_perm3.images[i].catIDs[0] + 1
			}
			if (images_perm3.images[i]['objects-found'][k].class == "Cat Face") {
				images_perm3.images[i].catIDs[1] = images_perm3.images[i].catIDs[1] + 1
			}
		}
		for (let j: number = 0; j < images_perm2.images.length; j++) {
			for (let k: number = 0; k < images_perm2.images[j].events.length; k++) {
				if (images_perm2.images[j].events[k] == images_perm3.images[i]._id) {
					images_perm3.images[i].catIDs[2] = "N"
				}
			}
		}
	}

	console.log('images_perm3')
	console.log(images_perm3)

	for (let i: number = 0; i < images_perm3.images.length; i++) {
		console.log('image perm 3')
		console.log(images_perm3.images[i].catIDs)
	}

	var dateFromObjectId = function (objectId) {
		return new Date(parseInt(objectId.substring(0, 8), 16) * 1000);
	};

	const datesAreOnSameDay = (first, second) =>
		first.getFullYear() === second.getFullYear() &&
		first.getMonth() === second.getMonth() &&
		first.getDate() === second.getDate();
	
	let days: Date[] = []

	for (let i: number = 0; i < images_perm3.images.length; i++) {
		images_perm3.images[i].date = new Date(dateFromObjectId(images_perm3.images[i]._id))
		days.push(images_perm3.images[i].date)
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
		<!--<Button class="" color="blue" on:click={export_csv}>Export CSV</Button>-->
		</ButtonGroup>
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
			  <TableHeadCell>Ears</TableHeadCell>
			  <TableHeadCell>Faces</TableHeadCell>
			  <TableHeadCell>Needs Review</TableHeadCell>
			  <TableHeadCell></TableHeadCell>		
			</TableHead>
			<TableBody >
			  {#each images_perm3.images as image}
			  <TableBodyRow>
				<TableBodyCell>{dateFromObjectId2(image._id)}</TableBodyCell>
				<TableBodyCell>{image.camera}</TableBodyCell>
				<TableBodyCell>{image.catIDs[0]}</TableBodyCell>
				<TableBodyCell>{image.catIDs[1]}</TableBodyCell>
				<TableBodyCell>{image.catIDs[2]}</TableBodyCell>
				<TableBodyCell><a href="/your-cats">Snapshot</a></TableBodyCell>
			  </TableBodyRow>
			  {/each}
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
