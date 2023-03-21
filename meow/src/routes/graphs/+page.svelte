<script lang='ts'>
	import type { PageData } from './$types';
	import { scaleBand } from 'd3-scale';
	import { user } from '$lib/stores/store';
	import Chart from 'svelte-frappe-charts';
	export let data: PageData
	
	const userInfo = JSON.parse(JSON.stringify($user))

	// let points: { date: string, cats: number }[] = []

	// let amounts = [1,2,5,3,0,2,1,5,6,0,3,0,1,3,2,4]

	// for(let x = 1; x < 11; x++){
	// 	points.push({date: 'Feb ' + x, cats: amounts[x] })
	// }

	// const xTicks = ['Feb 1 2023', 'Feb 2 2023', 'Feb 3 2023', 'Feb 4 2023', 'Feb 5 2023', 'Feb 6 2023', 'Feb 7 2023', 'Feb 8 2023', 'Feb 9 2023', 'Feb 10 2023', 'Feb 11 2023'];
	// const yTicks = [0, 1, 2, 3, 4, 5, 6];
	// const padding = { top: 20, right: 15, bottom: 20, left: 25 };

	// let width = 500;
	// let height = 200;

	// function formatMobile(tick) {
	// 	return "'" + tick.toString().slice(-2);
	// }

	// $: xScale = scaleLinear()
	// 	.domain([0, xTicks.length])
	// 	.range([padding.left, width - padding.right]);

	// $: yScale = scaleLinear()
	// 	.domain([0, Math.max.apply(null, yTicks)])
	// 	.range([height - padding.bottom, padding.top]);

	// $: innerWidth = width - (padding.left + padding.right);
	// $: barWidth = innerWidth / xTicks.length;

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

	let start_date = days[0]
	
	console.log("Days with cats: ")
	console.log(days)

	let days_graph: Date[] = []

	while (start_date <= days[days.length - 1]) {
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

</script>

<svelte:head>
	<title>Graphs</title>
	<meta name="description" content="Graphs" />
</svelte:head>

<section class= "flex flex-col justify-center">
<!-- 
	<h1 class="py-5">Welcome back, {userInfo.given_name}!</h1>
	<span class="flex flex-col justify-center items-center py-6">
		<p class="font-semibold text-2xl">
			Site 1
		</p>
		<p class="text-xl">
			Cats detected (per day)
		</p>
	</span>
	<span class="flex justify-center"> -->

		<Chart data={data1} type="bar" bind:this={chartRef}/>
		<button on:click={onExport}>
			|Export|
		  </button>

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
	<!-- </span> -->
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

	h2 {
		text-align: center;
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
