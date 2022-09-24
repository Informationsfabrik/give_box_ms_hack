<script>
	export let boxId;
	
	const getBox = async () => {
<<<<<<< HEAD
		var response = await fetch('https://api.givebox-ms.de/giveboxes/' + boxId, { headers: {'mode':'no-cors'}});
=======
		var response = await fetch('http://localhost:8081/giveboxes/' + boxId, { headers: {'mode':'no-cors'}});
>>>>>>> feature/map-marker
		var result = await response.json();
		return result;
	}

	let boxPromise = getBox();

</script>

<h1>Box {boxId}</h1>

{#await boxPromise then box2}
	<table>
		{#each Object.entries(box2) as [key, value], index}
			<tr>
				<td>{key}</td>
				<td>{value}</td>
			</tr>
		{/each}
	</table>
	<img src="https://api.givebox-ms.de/giveboxes/image/{boxId}" alt="image of a givebox" />
{/await}
<style>
</style>
