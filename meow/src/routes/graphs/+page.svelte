<script>
	export let data;
	console.log(data);
	
	import { time } from '$lib/stores/store';

	const formatter = new Intl.DateTimeFormat('en', {
		hour12: true,
		hour: 'numeric',
		minute: '2-digit',
		second: '2-digit'
	});
</script>

<svelte:head>
	<title>Graphs</title>
	<meta name="description" content="Graphs" />
</svelte:head>

<section class= "flex flex-col justify-items-center align-middle">

	<h1 class="mt-5">C.A.T.S.</h1>
	<h1 class="mb-5">Camera Assisted Tracking System</h1>
	<span class="flex justify-center">
		<div class="box">
			<h1>Graphs</h1>

		</div>

		<div class="box">
			<h1>The time is {formatter.format($time)}</h1>
		</div>	
	</span>
	<!-- <span class="flex justify-center">
		<div class="box">
			<h2>Words</h2>
		</div>

		<div class="box">

			<h2>Words</h2>

		</div>	
	</span> -->

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

</style>
