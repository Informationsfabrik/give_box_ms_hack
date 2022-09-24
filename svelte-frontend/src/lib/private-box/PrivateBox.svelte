<script lang="ts">
	import { ENV_OBJ } from '$lib/env'
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

	export let closeModal;
	let errorOccured = false;
	let erroMsg = "";

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

		box = 100;

		box = await fetch(ENV_OBJ.API_URL + '/giveboxes/', {
			method: 'POST',
			body: JSON.stringify(dict),
			headers: {'mode':'no-cors', 'content-type': 'application/json'}
		}).then(res => {
			if(!res.ok) {
				return res.text().then(text => { throw new Error(text) })
			}
			else {
				return res.json();
			}    
		})
		.catch(err => {
			errorOccured = true;
			erroMsg = err
			console.log('caught it!',err);
		});
		/*
		if (response.ok) {
			box = await response.json();
		} else {
			errorOccured = true;
			erroMsg = await response.text()
		}
		*/
		
	}

</script>

{#if box===100 && !errorOccured}
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
{:else if errorOccured}
	<h1>Error Occured!</h1>
	<div>{erroMsg}</div>
	<a on:click={() => closeModal()}>Back</a>
{:else if box !== 100}
	<h1>Thank you</h1>
	<a on:click={() => closeModal()}>Back</a>
{/if}

<style>
	Input, button{
		display:block;
		margin:10px;
	}
</style>
