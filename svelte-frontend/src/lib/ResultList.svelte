<script lang="ts">
    import ResultBox from '$lib/ResultBox.svelte';
    import { beforeUpdate, afterUpdate } from 'svelte';

    export let boxList;
    console.log("ResultList log:");
    console.log(boxList);

    beforeUpdate(() => {
		console.log(boxList)
	});
    
    
</script>

<div class="boxes">
    {#each Object.entries(boxList) as [key, value], index}
        <ResultBox box={value} />
    {/each}
</div>

<style lang="scss">
    .boxes {
        height: calc(100vh - 220px);
        overflow: scroll;
        margin-right: -25px;
        padding-right: 25px;
    }
</style>