<script>
    import { Button } from 'svelte-materialify';
    import { setContext } from 'svelte';
    import { writable, get } from 'svelte/store';
    
    export let snackbar = false;
    export let description_object;
 

</script>

<short-description>
{#if description_object}
    <h1>{description_object.name}</h1>
    <div>Adresse: {description_object?.address}</div>
    <div>Typ: {description_object?.is_temporary? "temporär": "dauerhaft"}</div>
    <div>Beschreibung: {description_object?.description}</div>
    <div>Öffnungszeiten: {description_object?.opening_hours}</div>
    <br>
    <Button>Mehr Info</Button>
{/if}

{#if !description_object}
	No info available
{/if}
</short-description>