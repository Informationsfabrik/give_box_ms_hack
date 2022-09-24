<script>
	export let boxId;
	
	const getBox = async () => {
		var response = await fetch('http://localhost:8081/giveboxes/' + boxId, { headers: {'mode':'no-cors'}});
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
{/await}
<style>
</style>
