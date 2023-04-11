<script lang='ts'>
	import { Avatar, Card, Button } from "flowbite-svelte";
	import { cat } from '$lib/stores/store.js'

	let catInfo;

	cat.subscribe(value => {
		catInfo = value;
	})

</script>

<svelte:head>
	<title>Individual Cat Details</title>
	<meta name="description" content="Details" />
</svelte:head>

<section>
	<div>
	<h1 class="py-4">{catInfo.name}</h1>
	</div>
	<div class="grid grid-cols-2 gap-4 pt-4">
		<div class="flex flex-col justify-items-center align-middle gap-4">
			<Avatar src={catInfo.events[0].path} size="lg" class="mb-4"/>
			<p class="font-bold text-xl">{catInfo.name}</p>
		</div>
		<div class="flex flex-col justify-items-center align-middle gap-2">
			<Card>
				<p class="font-bold text-xl">General Information</p>
				<p class="text-xl">Age: {catInfo.age}</p>
				<p class="text-xl">Weight: {catInfo.weight}</p>
				<p class="text-xl">Neutered: {catInfo.neutered}</p>
			</Card>
		</div>
</section>
