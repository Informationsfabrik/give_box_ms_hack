<script>
	import { createEventDispatcher } from 'svelte';
	const dispatch = createEventDispatcher();
    import L from 'leaflet';
	import { getContext } from "svelte";

	export let lat = 0;
	export let lng = 0;

	let map = getContext('leafletMapInstance');

	L.marker([lat, lng]).addTo(map);
</script>

<style>
	button {
		width: 2rem
	}
</style>

<div>
	<button on:click={() => addValue(-1)}>
		-
	</button>
	<button on:click={() => addValue(1)}>
		+
	</button>	
</div>

<div style="width:100%;text-align:center;font-weight:600">
	{count}
</div>
