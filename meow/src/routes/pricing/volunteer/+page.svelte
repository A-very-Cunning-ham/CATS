<script>
	import { Card, Button } from 'flowbite-svelte';
</script>

<svelte:head>
	<title>Pricing</title>
	<meta name="description" content="Pricing" />
</svelte:head>

<section>
    <h1 class="font-semibold py-6">Pricing Options</h1>
	<br/>
	<div class="flex flex-row justify-center gap-5">
		<Card padding="xl">
			<h5 class="mb-4 text-xl font-medium text-gray-500 dark:text-gray-400">Basic plan</h5>
			<div class="flex items-baseline text-gray-900 dark:text-white">
				<span class="text-3xl font-semibold">$</span>
				<span class="text-5xl font-extrabold tracking-tight">350</span>
				<span class="ml-1 text-xl font-normal text-gray-500 dark:text-gray-400">/month</span>
			</div>
			<ul class="my-7 space-y-4">
				<li class="flex space-x-2">
					<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6 text-blue-600 dark:text-blue-500"><path stroke-linecap="round" stroke-linejoin="round" d="M9 12.75L11.25 15 15 9.75M21 12a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>
					<span class="text-base font-normal leading-tight text-gray-500 dark:text-gray-400">5 cameras</span>
				</li>
				<li class="flex space-x-2">
					<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6 text-blue-600 dark:text-blue-500"><path stroke-linecap="round" stroke-linejoin="round" d="M9 12.75L11.25 15 15 9.75M21 12a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>
					<span class="text-base font-normal leading-tight text-gray-500 dark:text-gray-400">Hardware Installation</span>
				</li>
				<li class="flex space-x-2">
					<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6 text-blue-600 dark:text-blue-500"><path stroke-linecap="round" stroke-linejoin="round" d="M9 12.75L11.25 15 15 9.75M21 12a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>
				  <span class="text-base font-normal leading-tight text-gray-500 dark:text-gray-400">Snapshot Capture and Download</span>
			  	</li>
				<li class="flex space-x-2">
					  <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6 text-blue-600 dark:text-blue-500"><path stroke-linecap="round" stroke-linejoin="round" d="M9 12.75L11.25 15 15 9.75M21 12a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>
					<span class="text-base font-normal leading-tight text-gray-500 dark:text-gray-400">Email & Mobile Alerts</span>
				</li>
				<li class="flex space-x-2 line-through decoration-gray-500">
					  <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6 text-blue-600 dark:text-blue-500"><path stroke-linecap="round" stroke-linejoin="round" d="M9 12.75L11.25 15 15 9.75M21 12a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>
					<span class="text-base font-normal leading-tight text-gray-500">Video History for up to 180 Days</span>
				</li>
				<li class="flex space-x-2 line-through decoration-gray-500">
					  <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6 text-blue-600 dark:text-blue-500"><path stroke-linecap="round" stroke-linejoin="round" d="M9 12.75L11.25 15 15 9.75M21 12a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>
					<span class="text-base font-normal leading-tight text-gray-500">Extended Warranty for all Cameras</span>
				</li>
				<li class="flex space-x-2 line-through decoration-gray-500">
					  <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6 text-blue-600 dark:text-blue-500"><path stroke-linecap="round" stroke-linejoin="round" d="M9 12.75L11.25 15 15 9.75M21 12a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>
					<span class="text-base font-normal leading-tight text-gray-500">10% off select CATS merchandise</span>
				</li>
				<li class="flex space-x-2 line-through decoration-gray-500">
					  <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6 text-blue-600 dark:text-blue-500"><path stroke-linecap="round" stroke-linejoin="round" d="M9 12.75L11.25 15 15 9.75M21 12a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>
					<span class="text-base font-normal leading-tight text-gray-500">24×7 phone & email support</span>
				</li>
			</ul>
			<Button class="w-full" href="/">Choose plan</Button>
		  </Card>

		  <Card padding="xl">
			<h5 class="mb-4 text-xl font-medium text-gray-500 dark:text-gray-400">Standard plan</h5>
			<div class="flex items-baseline text-gray-900 dark:text-white">
				<span class="text-3xl font-semibold">$</span>
				<span class="text-5xl font-extrabold tracking-tight">835</span>
				<span class="ml-1 text-xl font-normal text-gray-500 dark:text-gray-400">/month</span>
			</div>
			<!-- List -->
			<ul class="my-7 space-y-4">
				<li class="flex space-x-2">
					<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6 text-blue-600 dark:text-blue-500"><path stroke-linecap="round" stroke-linejoin="round" d="M9 12.75L11.25 15 15 9.75M21 12a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>
					<span class="text-base font-normal leading-tight text-gray-500 dark:text-gray-400">10 cameras</span>
				</li>
				<li class="flex space-x-2">
					<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6 text-blue-600 dark:text-blue-500"><path stroke-linecap="round" stroke-linejoin="round" d="M9 12.75L11.25 15 15 9.75M21 12a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>
					<span class="text-base font-normal leading-tight text-gray-500 dark:text-gray-400">Hardware Installation</span>
				</li>
				<li class="flex space-x-2">
					<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6 text-blue-600 dark:text-blue-500"><path stroke-linecap="round" stroke-linejoin="round" d="M9 12.75L11.25 15 15 9.75M21 12a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>
				  <span class="text-base font-normal leading-tight text-gray-500 dark:text-gray-400">Snapshot Capture and Download</span>
			  	</li>
				<li class="flex space-x-2">
					  <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6 text-blue-600 dark:text-blue-500"><path stroke-linecap="round" stroke-linejoin="round" d="M9 12.75L11.25 15 15 9.75M21 12a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>
					<span class="text-base font-normal leading-tight text-gray-500 dark:text-gray-400">Email & Mobile Alerts</span>
				</li>
				<li class="flex space-x-2 decoration-gray-500">
					  <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6 text-blue-600 dark:text-blue-500"><path stroke-linecap="round" stroke-linejoin="round" d="M9 12.75L11.25 15 15 9.75M21 12a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>
					<span class="text-base font-normal leading-tight text-gray-500">Video History for up to 180 Days</span>
				</li>
				<li class="flex space-x-2 decoration-gray-500">
					  <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6 text-blue-600 dark:text-blue-500"><path stroke-linecap="round" stroke-linejoin="round" d="M9 12.75L11.25 15 15 9.75M21 12a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>
					<span class="text-base font-normal leading-tight text-gray-500">Extended Warranty for all Cameras</span>
				</li>
				<li class="flex space-x-2 line-through decoration-gray-500">
					  <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6 text-blue-600 dark:text-blue-500"><path stroke-linecap="round" stroke-linejoin="round" d="M9 12.75L11.25 15 15 9.75M21 12a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>
					<span class="text-base font-normal leading-tight text-gray-500">10% off select CATS merchandise</span>
				</li>
				<li class="flex space-x-2 line-through decoration-gray-500">
					  <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6 text-blue-600 dark:text-blue-500"><path stroke-linecap="round" stroke-linejoin="round" d="M9 12.75L11.25 15 15 9.75M21 12a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>
					<span class="text-base font-normal leading-tight text-gray-500">24×7 phone & email support</span>
				</li>
			</ul>
			<Button class="w-full" href="/">Choose plan</Button>
		  </Card>

		  <Card padding="xl">
			<h5 class="mb-4 text-xl font-medium text-gray-500 dark:text-gray-400">Premium plan</h5>
			<div class="flex items-baseline text-gray-900 dark:text-white">
				<span class="text-3xl font-semibold">$</span>
				<span class="text-5xl font-extrabold tracking-tight">1149</span>
				<span class="ml-1 text-xl font-normal text-gray-500 dark:text-gray-400">/month</span>
			</div>
			<!-- List -->
			<ul class="my-7 space-y-4">
				<li class="flex space-x-2">
					<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6 text-blue-600 dark:text-blue-500"><path stroke-linecap="round" stroke-linejoin="round" d="M9 12.75L11.25 15 15 9.75M21 12a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>
					<span class="text-base font-normal leading-tight text-gray-500 dark:text-gray-400">Up to 20 cameras</span>
				</li>
				<li class="flex space-x-2">
					<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6 text-blue-600 dark:text-blue-500"><path stroke-linecap="round" stroke-linejoin="round" d="M9 12.75L11.25 15 15 9.75M21 12a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>
					<span class="text-base font-normal leading-tight text-gray-500 dark:text-gray-400">Hardware Installation</span>
				</li>
				<li class="flex space-x-2">
					<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6 text-blue-600 dark:text-blue-500"><path stroke-linecap="round" stroke-linejoin="round" d="M9 12.75L11.25 15 15 9.75M21 12a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>
				  <span class="text-base font-normal leading-tight text-gray-500 dark:text-gray-400">Snapshot Capture and Download</span>
			  	</li>
				<li class="flex space-x-2">
					  <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6 text-blue-600 dark:text-blue-500"><path stroke-linecap="round" stroke-linejoin="round" d="M9 12.75L11.25 15 15 9.75M21 12a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>
					<span class="text-base font-normal leading-tight text-gray-500 dark:text-gray-400">Email & Mobile Alerts</span>
				</li>
				<li class="flex space-x-2 decoration-gray-500">
					  <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6 text-blue-600 dark:text-blue-500"><path stroke-linecap="round" stroke-linejoin="round" d="M9 12.75L11.25 15 15 9.75M21 12a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>
					<span class="text-base font-normal leading-tight text-gray-500">Video History for up to 180 Days</span>
				</li>
				<li class="flex space-x-2 decoration-gray-500">
					  <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6 text-blue-600 dark:text-blue-500"><path stroke-linecap="round" stroke-linejoin="round" d="M9 12.75L11.25 15 15 9.75M21 12a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>
					<span class="text-base font-normal leading-tight text-gray-500">Extended Warranty for all Cameras</span>
				</li>
				<li class="flex space-x-2 decoration-gray-500">
					  <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6 text-blue-600 dark:text-blue-500"><path stroke-linecap="round" stroke-linejoin="round" d="M9 12.75L11.25 15 15 9.75M21 12a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>
					<span class="text-base font-normal leading-tight text-gray-500">10% off select CATS merchandise</span>
				</li>
				<li class="flex space-x-2 decoration-gray-500">
					  <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6 text-blue-600 dark:text-blue-500"><path stroke-linecap="round" stroke-linejoin="round" d="M9 12.75L11.25 15 15 9.75M21 12a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>
					<span class="text-base font-normal leading-tight text-gray-500">24×7 phone & email support</span>
				</li>
			</ul>
			<Button class="w-full" href="/">Choose plan</Button>
		  </Card>
	</div>
</section>