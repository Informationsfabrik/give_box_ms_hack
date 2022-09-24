<script>
    import { Button } from 'svelte-materialify';
    import { setContext } from 'svelte';
    import { writable, get } from 'svelte/store';
    import Router, {location, push, pop, replace} from "svelte-spa-router";
    
    export let snackbar = false;
    export let description_object;
    let redirect_url = "/box?" + description_object?.id;

 /*
 id: Optional[int]
    longitude: float
    latitude: float
    is_temporary: Optional[bool]
    description: Optional[str]
    opening_hours: Optional[str]
    is_temporary: Optional[bool]
    extern_link: Optional[str]
    content: Optional[Content]
 */

</script>


<short-description>
{#if description_object}
    <h1>{description_object?.description}</h1>
    <div>Typ: {description_object?.is_temporary? "temporär": "dauerhaft"}</div>
    <div>Beschreibung: {description_object?.description}</div>
    <div>Öffnungszeiten: {description_object?.opening_hours}</div>
    <br>
    <a href={redirect_url}><Button>Mehr Info</Button></a>
    
{/if}

{#if !description_object}
	No info available
{/if}
</short-description>