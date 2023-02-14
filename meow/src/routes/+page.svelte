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

<section>
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
	section {
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
		flex: 0.6;
	}

	h1 {
		width: 100%;
	}
	span {
		display: flex;
		width: 100%;
	}

	.box {
		width: 300px;
		border: 1px solid #aaa;
		border-radius: 20px;
		box-shadow: 2px 2px 8px rgba(0,0,0,0.1);
		padding: 5em;
		margin: 0 0 1em 0;
	}

</style>
