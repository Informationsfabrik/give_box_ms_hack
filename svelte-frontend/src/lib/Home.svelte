<script lang="ts">
    import Map from "$lib/map/Map.svelte";
    import MediaQuery from "$lib/media-query/MediaQuery.svelte";

    const getBoxes = async () => {
		var response = await fetch('https://api.givebox-ms.de/giveboxes', { headers: {'mode':'no-cors'}});
		var result = await response.json();
		return result;
	}

	let boxPromise = getBoxes();
</script>

<MediaQuery query="(min-width: 1281px)" let:matches>
	{#if matches}
	<div class="container">
        <div class="left">
            {#await boxPromise then box2}
                {#each box2 as box}
                <a href="/box?{box['id']}">
                <div class="box">
                    <h4>{box["description"]}</h4>
                    <p>{box["content"]}</p>
                </div>
            </a>
                {/each}
            {/await}
        </div>
        <div class="right">
            <Map></Map>
        </div>
    </div>
	{/if}
</MediaQuery>

<MediaQuery query="(min-width: 481px) and (max-width: 1280px)" let:matches>
	{#if matches}
    <div class="container-mobile">
        <div class="fill">
            <Map></Map>
        </div>
    </div>
	<div class="container-mobile">
        <div class="fill">
            {#await boxPromise then box2}
                {#each box2 as box}
                <a href="/box?{box['id']}">
                <div class="box">
                    <h4>{box["description"]}</h4>
                    <p>{box["content"]}</p>
                </div>
            </a>
                {/each}
            {/await}
        </div>
        
    </div>
	{/if}
</MediaQuery>

<MediaQuery query="(max-width: 480px)" let:matches>
	{#if matches}
    <div class="container-mobile">
        <div class="fill">
            <Map></Map>
        </div>
    </div>
	<div class="container-mobile">
        <div class="fill">
            {#await boxPromise then box2}
                {#each box2 as box}
                <a href="/box?{box['id']}">
                <div class="box">
                    <h4>{box["description"]}</h4>
                    <p>{box["content"]}</p>
                </div>
            </a>
                {/each}
            {/await}
        </div>
        
    </div>
	{/if}
</MediaQuery>



<style>
    .container {
        display: flex;
        flex-direction: row;
        align-items: stretch;
        width: 100%;
        height: 80vh;
    }

    .container-mobile {
        display: flex;
        flex-direction: row;
        align-items: stretch;
        width: 100%;
        height: 50vh;
    }

    .container>.left {
        flex: 1;
    }
    .container>.right {
        flex: 2;
    }
    .container-mobile >.fill {
        flex: 1;
        margin-bottom: 20px;
    }

    .box {
        color: black;
        box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
        transition: 0.3s;
        border-radius: 5px; /* 5px rounded corners */
        border-bottom: 30px;
        margin: 15px;
        padding: 5px;
    }
</style>
