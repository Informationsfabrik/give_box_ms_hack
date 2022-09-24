<script lang="ts">
	let longitude;
	let latitude;
	let is_temporary = true;
	let description;
	let address_id = 999;
	let opening_hours;
	let extern_link = "";
	let maintenance_needed = false;
	let maintainer_info = "hmm";
	let last_confirmation_date = "2020-01-01 00:00:00";
	let image_id = 2;
	let street;
	let house_number;
	let zip_code;
	let city;
	let maintainer = [];


	let book = false;
	let clothes = false;
	let electronics = false;
	let toys = false;
	let others = "";

	let box = 100;


	async function submit() {

		var dict = {
			"longitude": Number(longitude),
			"latitude": Number(latitude),
			"is_temporary": is_temporary,
			"description": description,
			"address_id": address_id,
			"opening_hours": opening_hours,
			"extern_link": extern_link,
			"content": {
				"book": book,
				"clothes": clothes,
				"electronics": electronics,
				"toys": toys,
				"others": others,
			},
			"maintenance_needed": maintenance_needed,
			"maintainer_info": maintainer_info,
			"last_confirmation_date": last_confirmation_date,
			"image_id": Number(image_id),
			"street": street,
			"house_number": Number(house_number),
			"zip_code": Number(zip_code),
			"city": city,
			"maintainer":maintainer
		}

		box = await fetch('http://127.0.0.1:8081/giveboxes', {
			method: 'POST',
			body: JSON.stringify(dict),
			headers: {'mode':'no-cors', 'content-type': 'application/json'}
		}).then((res) => res.json())
	}

</script>

{#if box===100}
<form>
	<input bind:value="{longitude}" placeholder="Longitude">
	<input bind:value="{latitude}" placeholder="Latitude">
	<input bind:value="{description}" placeholder="Beschreibung">
	<input bind:value="{opening_hours}" placeholder="Öffnungszeiten">
	<input bind:value="{street}" placeholder="Staße">
	<input bind:value="{house_number}" placeholder="Hausnummer">
	<input bind:value="{zip_code}" placeholder="Postleitzahl">
	<input bind:value="{city}" placeholder="Stadt">

	<label>Bücher<input type="checkbox" on:change={(e) => {book =e.target.checked}}></label>
	<label>Kleidung<input type="checkbox" on:change={ (e) => {clothes =e.target.checked}}></label>
	<label>Elektronik<input type="checkbox" on:change={(e) => {electronics =e.target.checked}}></label>
	<label>Spielzeug<input type="checkbox" on:change={ (e) => {toys =e.target.checked}}></label>
	<input bind:value="{others}" placeholder="Sonstiges">

</form>
<button on:click={submit}>Submit</button>
{:else if box === 200}
	<h1>Thank you</h1>
	<a href="/">Back</a>
{/if}

<style>
	Input, button{
		display:block;
		margin:10px;
	}
</style>
