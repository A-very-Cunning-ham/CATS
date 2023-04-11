<script>
	import { Card, Button } from 'flowbite-svelte';
	import icon1 from '$lib/images/icons/users.png';
	import icon2 from '$lib/images/icons/home.png';
	import icon3 from '$lib/images/icons/id-card.png';
</script>

<svelte:head>
	<title>Pricing</title>
	<meta name="description" content="Pricing" />
</svelte:head>

<section>
    <h1 class="font-semibold p-6">Pricing</h1>
	<h1 class="mt-10">Tell us more about yourself</h1>
	<h1>I am a...</h1>

	<div class="flex flex-row justify-center gap-5 p-10">
		<Card padding="xl" class="flex-1 hover:no-underline" href="/pricing/volunteer">
			<div class="flex flex-col items-center">
				<img src={icon1} class="w-10 h-10 object-contain" alt="persons"/>
				<h5 class="text-xl font-medium text-gray-500 dark:text-gray-400">Volunteer</h5>
			</div>
		</Card>
		<Card padding="xl" class="flex-1 hover:no-underline" href="/pricing/TNR">
			<div class="flex flex-col items-center">
				<img src={icon2} class="w-10 h-10 object-contain" alt="persons"/>
				<h5 class="text-xl font-medium text-gray-500 dark:text-gray-400">TNR Program</h5>
			</div>
		</Card>
		<Card padding="xl" class="flex-1 hover:no-underline" href="/pricing/gov">
			<div class="flex flex-col items-center">
				<img src={icon3} class="w-10 h-10 object-contain" alt="persons"/>
				<h5 class="text-xl font-medium text-gray-500 dark:text-gray-400">Local Goverment</h5>
			</div>
		</Card>
	</div>
</section>