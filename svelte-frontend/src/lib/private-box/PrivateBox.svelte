<script lang="ts">
	import { ENV_OBJ } from '$lib/env'
	// import ImageUpload from "$lib/imageupload/ImageUpload.svelte";
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
	let image;

	let avatar;
	let fileinput;
	const onFileSelected =(e)=>{
		let image = e.target.files[0];
		let reader = new FileReader();
		reader.readAsDataURL(image);
		reader.onload = e => {
			avatar = e.target.result
		};
	}

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

		var image_dict = {
			"box_id": Number(box),
			"is_title_image": true,
			"data" : avatar
		}
		image = await fetch(ENV_OBJ.API_URL + '/images', {
			method: 'POST',
			body: JSON.stringify(image_dict),
			headers: {'mode':'no-cors', 'content-type': 'application/json'}
		}).then((res) => res.json())
		
	}

</script>

<h1>Private Box veröffentlichen</h1>
<h3>Bitte stelle die benötigten Informationen für deine Box bereit.</h3>
<hr />
<form>
	<div>
		<label for="longitude"><b>Longitude</b></label>
        <br>
		<input
			type="text"
			placeholder="Gebe deinen Box longitude ein."
			name="longitude"
			id="longitude"
			required
		/>
	</div>
	<div>
		<label for="latitude"><b>Longitude</b></label>
		<br>
		<input
				type="text"
				placeholder="Gebe deinen Box latitude ein."
				name="latitude"
				id="latitude"
				required
		/>
	</div>
	<div>
		<label for="address"><b>Adresse</b></label>
		<br>
		<input
				type="text"
				placeholder="Gib deine Adresse ein."
				name="address"
				id="address"
				required
		/>
	</div>
	<div>
		<label for="opening_hours"><b>opening_hours</b></label>
		<br>
		<input
				type="text"
				placeholder="Gib deine opening_hours ein."
				name="opening_hours"
				id="opening_hours"
				required
		/>
	</div>
	<div>
		<label for="is_temporary"><b>is_temporary</b></label>
		<br>
		<input
				type="text"
				placeholder="Gib deine is_temporary ein."
				name="is_temporary"
				id="is_temporary"
				required
		/>
	</div>
	<div>
		<label for="description"><b>description</b></label>
        <br>
		<input
			type="text"
			placeholder="Beschreibe deine Box und deren Inhalte"
			name="description"
			id="description"
			required
		/>
	</div>
	<div>
		<label for="last_confirmation_date"><b>last_confirmation_date</b></label>
		<br>
		<input
				type="text"
				placeholder="last_confirmation_date"
				name="last_confirmation_date"
				id="last_confirmation_date"
				required
		/>
	</div>
	<div>
		<label for="image_link"><b>image_link</b></label>
		<br>
		<input
				type="text"
				placeholder="image_link"
				name="image_link"
				id="image_link"
				required
		/>
	</div>
	<div>
		<label for="tags"><b>tags</b></label>

		<select name="tags" id="tags" form="tags" required>
			<option value="bücher">Bücher</option>
			<option value="spielzeug">Spielzeug</option>
			<option value="kleidung">Kleidung</option>
			<option value="deko">Deko</option>
			<option value="möbel">Möbel</option>
			<option value="sonstiges">Sonstiges</option>
		</select>
	</div>
    <ImageUpload />
	<div>
		<p>Durch hinzufügen deiner Box stimmst du unseren Bedingungen zu. <a href="#">AGB's</a>.</p>
		<button type="submit" class="private-box-creation">Private Box erstellen</button>
</form>

<style>
	Input, button{
		display:block;
		margin:10px;
	}
	#app{
		display:flex;
		align-items:center;
		justify-content:center;
		flex-flow:column;
	}

	.upload{
		display:flex;
		cursor:pointer;
	}
	.avatar{
		display:flex;
		height:200px;
		width:200px;
	}
</style>
