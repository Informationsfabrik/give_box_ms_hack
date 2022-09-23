<script>
    import { Button } from 'svelte-materialify';
    import { setContext } from 'svelte';
    import { writable, get } from 'svelte/store';
    import Router, {location, push, pop, replace} from "svelte-spa-router";
    
    export let snackbar = false;
    export let description_object;
    let redirect_url = "/box?" + description_object?.id;

    export async function load() {
      return {
          status: 302,
          redirect: redirect_url
      }
  }
 

</script>

<short-description>
{#if description_object}
    <h1>{description_object.name}</h1>
    <div>Adresse: {description_object?.address}</div>
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