<script>
	import { Avatar, Checkbox, Helper, Input, Label, Button } from "flowbite-svelte";
	import { isAuthenticated, user } from '$lib/stores/store'

	const userInfo = JSON.parse(JSON.stringify($user))

</script>

<svelte:head>
	<title>Profile</title>
	<meta name="description" content="CATS demo app" />
</svelte:head>

<section>
	<h1 class="py-4">Profile</h1>
	<div class="grid grid-cols-2 gap-4 pt-4">
		<div class="flex flex-col justify-items-center align-middle gap-4">
			<Avatar src={userInfo.picture} size="lg" class="mb-4"/>
			<p class="font-bold text-xl">{userInfo.name}</p>
			<p class="text-base">{userInfo.sub}</p>
		</div>
		<div class="flex flex-col justify-items-center align-middle gap-2">
			<form id="general">
			<div class="border rounded-lg py-3 px-6 bg-white">
				<div class="py-3">
					<p class="font-semibold text-gray-900">General Information</p>
					<Helper id="helper-checkbox-text">The following information is not displayed to the public</Helper>
				</div>
					<div class="grid gap-6 py-3">
					<div>
						<Label for="first_name" class="mb-2">First name</Label>
						<Input type="text" id="first_name" value={userInfo.given_name} placeholder="John" class="border-2 border-inherit" required />
					</div>
					<div>
						<Label for="last_name" class="mb-2">Last name</Label>
						<Input type="text" id="last_name" value={userInfo.family_name} placeholder="Doe" class="border-2 border-inherit" required />
					</div>
					
					<div class="mb-2">
						<Label for="email" class="mb-2">Email address</Label>
						<Input type="email" id="email" value={userInfo.email} placeholder="john.doe@company.com" class="border-2 border-inherit" required />
					</div>
					<div>
						<Label for="phone" class="mb-2">Password</Label>
						<Input type="password" id="password" placeholder="•••••••••" class="border-2 border-inherit" disabled />
					</div>
					<div>
						<Label for="phone" class="mb-2">Phone number</Label>
						<Input type="tel" id="phone" placeholder="123-456-7890" pattern="[0-9]{3}-[0-9]{3}-[0-9]{4}" class="border-2 border-inherit" />
					</div>
					</div>
				</div>
			</form>
			<div class="border rounded-lg py-3 px-6 bg-white">
				<div class="mb-3">
					<p class="font-semibold text-gray-900">Site Preferences</p>
					<Helper id="helper-checkbox-text">Choose which sites appear on your home page</Helper>
				</div>
				<div class="py-3">
				<ul class="w-48 p-3bg-white rounded-lg border border-gray-200 divide-y divide-gray-200">
					<li><Checkbox class="p-3">Site 3</Checkbox></li>
					<li><Checkbox class="p-3">Site 4</Checkbox></li>
					<li><Checkbox class="p-3">Site 5</Checkbox></li>
					<li><Checkbox class="p-3">Site 6</Checkbox></li>
					<li><Checkbox class="p-3">Site 7</Checkbox></li>
					<li><Checkbox class="p-3">Site 8</Checkbox></li>
					<li><Checkbox class="p-3">Site 9</Checkbox></li>
				</ul>
			</div>
			</div>
			<div class="py-6 self-center">
				<Button type="submit" class="w-48" form="general">Save Changes</Button>
			</div>
			</div>
		</div>
</section>
