<script lang="ts">
    import Map from "$lib/map/Map.svelte";

    const getBoxes = async () => {
		var response = await fetch('https://api.givebox-ms.de/givebox', { headers: {'mode':'no-cors'}});
		var result = await response.json();
		return result;
	}

	let boxPromise = getBoxes();
</script>

<div class="container">
    <div>
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
    <div>
        <Map></Map>
    </div>
</div>

<style>
    .container{
        display: flex;
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
