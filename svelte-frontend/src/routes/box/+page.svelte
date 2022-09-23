<script lang="ts">
    import Box from "$lib/box/Box.svelte";
    import { page } from '$app/stores';
    import {navigate} from "svelte-routing";


    let boxId:any;
    let box_is_nan:boolean = false;
    if (($page.url.search.length > 1) && ($page.url.search.includes('?'))) {
        boxId = $page.url.search.replace('?', '');
        boxId = Number(boxId);

        box_is_nan = isNaN(boxId);
        if(box_is_nan) {
            // TODO fix
            navigate('/')
        }
    }

</script>

{#if !box_is_nan}
    <Box boxId="{boxId}"/>
{/if}