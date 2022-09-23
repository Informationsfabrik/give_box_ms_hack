<script>
    import Box from "$lib/box/Box.svelte";
    import { page } from '$app/stores';
    import {navigate} from "svelte-routing";


    let box_id;
    if (($page.url.search.length > 1) && ($page.url.search.includes('?'))) {
        box_id = $page.url.search.replace('?', '');
        box_id = Number(box_id);

        if(isNaN(box_id)) {
            // TODO fix
            console.log("GG");
            navigate('/')
        }
    }

</script>

{#if box_id}
    <Box boxId="{box_id}"/>
{/if}