<script lang="ts">
	import type { PageData } from './$types';
	export let data: PageData

	$: ({images} = data)

	var dateFromObjectId = function (objectId) {
		return new Date(parseInt(objectId.substring(0, 8), 16) * 1000);
	};
	
</script>

<ul>
	{#each images as image}
	<li>
		<!-- <img src="{image.path}" alt="Cat!" /> -->
		<img src="{image.path}" alt="Cat!" class="max-w-md"/>
		<h6 class="font-bold">Date from Object ID: </h6>{dateFromObjectId(image._id)}
		<h6> Detected Object: {image['object-detected']} </h6>
		<br/>
	</li>
	{/each}
</ul>