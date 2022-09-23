<script>
	import { onMount } from 'svelte';
	let box;
	export let boxId;

	// onMount(async () => {
	//     box = await fetch('http://127.0.0.1:8081/box/' + boxId)
	//         .then((res) => res.json());
	// });
	box = {
		longitude: 0.2,
		latitude: 0.1,
		street: 'Steinfurter Str. 80',
		number: false,
		oeffnungszeiten: '12:00-18:00',
		bezeichnung: 'BLABLIBLU'
	};
</script>

<h1>Box {boxId}</h1>

{#if box}
	<div>
		<p>{box}</p>
		<p>{box.latitude}</p>
		<p>{box.street}</p>
		<p>{box.number}</p>
		<p>{box.oeffnungszeiten}</p>
		<p>{box.bezeichnung}</p>
	</div>
    <div>
        <p>Kommentare</p>
        <div>
            
        </div>
    </div>
{/if}

<style>
</style>
