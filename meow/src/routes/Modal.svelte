<script>
    import { Modal, Button } from 'flowbite-svelte'
    export let imageFromData
    export let open
</script>

<Modal title="New Event" bind:open={open} autoclose>
    <div class="flex gap-4">
        <img src={imageFromData} alt="Cat!" class="object-cover max-h-64"/>	
    </div>
    <svelte:fragment slot='footer'>
        <Button>I accept</Button>
        <Button color="alternative">Decline</Button>
    </svelte:fragment>
</Modal>