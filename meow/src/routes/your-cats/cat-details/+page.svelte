<script lang='ts'>
	import { Avatar, Card, Button } from "flowbite-svelte";
	import { cat } from '$lib/stores/store.js';

	let catInfo
	cat.subscribe(value => {
		catInfo = value;
	})

	let editing = false;

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
		<div class="flex flex-col justify-self-center justify-items-center align-middle gap-4">
			{#if catInfo.events}
			<Avatar src="../{catInfo.events[0]}" size="lg" class="mb-4"/>
			{:else}
			<Avatar size="lg" class="mb-4"/>
			{/if}
			<p class="font-bold text-xl">{catInfo.name}</p>
			<p class="text-xl">Recent Captures:</p>
			<div class="flex flex-col gap-2">
			{#if catInfo.events}
				{#each catInfo.events as image}
				<img src="../{image}" alt="Cat!" class="w-64"/>
				{/each}
			{/if}
			</div>
		</div>
		{#if !editing}
		<div class="flex flex-col justify-self-center justify-items-center align-middle gap-3 w-full">
			<Card>
				<p class="font-bold text-xl">General Information</p>
				<p class="text-xl">Age: {catInfo.age}</p>
				<p class="text-xl">Weight: {catInfo.weight}</p>
				<p class="text-xl">Neutered: {catInfo.neutered}</p>
			</Card>
			<Card class="min-h-[25%] flex flex-col gap-1">
				<p class="font-bold text-xl">Notes</p>
				{#if catInfo.notes}
					{#each catInfo.notes as note}
					<Card>{note}</Card>
					{/each}
				{/if}
			</Card>
			<div><Button on:click={()=> editing=true}>Edit</Button></div>
		</div>
		{:else}
		<div class="flex flex-col justify-self-center justify-items-center align-middle gap-3 w-full">
			<form id="edit-list" method="POST" action="?/edit" class="flex flex-col gap-3">
			<Card>
				<p class="font-bold text-xl">General Information</p>
				<label class="py-2 text-xl">
					Age
					<input name="age" value={catInfo.age} class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight">
				</label>
				<label class="py-2 text-xl">
					Weight
					<input name="weight" value={catInfo.weight} class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight">
				</label>
				<label class="py-2 text-xl">
					Neutered
					<select class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight" name="neutered" required value={catInfo.neutered}>
						<option value="Y">Yes</option>
						<option value="N">No</option>	
						<option value="Undefined">Unsure</option>	
					</select>
				</label>
			</Card>
			<Card class="min-h-[25%]">
				<p class="font-bold text-xl">Notes</p>
				<div class="mb-3 mt-3">
					<input name="notes" type="text" placeholder="Placeholder" class="px-3 py-2 placeholder-slate-300 text-slate-600 relative bg-white bg-white rounded text-base border shadow focus:outline w-full"/>
				</div>
			</Card>
			<input type="hidden" name="id" hidden value={catInfo._id} />
			</form>
			<div>
				<button form="edit-list" type="submit" class="shadow bg-blue-700 focus:shadow-outline focus:outline-none text-white font-bold py-2 px-4 rounded">Save Changes</button>
			</div>
			
		</div>
		{/if}
	</div>
</section>
