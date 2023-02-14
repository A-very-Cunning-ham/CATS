<script>
	
	import { time } from '../store.js';
	import {onMount} from 'svelte';
	import Gallery from 'svelte-image-gallery'
	import { MongoClient } from "mongodb"
	import { URI } from '@env'

	const client = new MongoClient(URI)

	function handleImage(e) {
		console.log(e.detail.src)
	}

	const formatter = new Intl.DateTimeFormat('en', {
		hour12: true,
		hour: 'numeric',
		minute: '2-digit',
		second: '2-digit'
	});

	let url = ''
	let todos = []

	const getTodos = async () => {
		const response = await fetch(url)
		const data = await response.json()
		todos = data
	}

	onMount(() => {getTodos()})

	//const load = url => fetch(url).then(res => res.json());
	//const apiURL = ''
	//{#await load(apiURL) then data}
</script>

<svelte:head>
	<title>Home</title>
	<meta name="description" content="CATS demo app" />
</svelte:head>

<section class= "flex flex-col justify-items-center align-middle">
	<h1 class="mt-5">C.A.T.S</h1>
	<h1 class="mb-5">Camera Assisted Tracking System</h1>
	<span>
		<div class="box">
			
			<pre>
				<div>
					<Gallery on:click={handleImage}>
						{#each todos as todo }
							<img src="{todo.path}" alt="Cat!" />
						{/each}
					</Gallery>
				</div>  
			</pre>
		</div>

		<div class="box">
			<h1>The time is {formatter.format($time)}</h1>
		</div>	
	</span>
	<h1>
		Home Page<br />Miau
	</h1>

</section>

<style>

</style>
