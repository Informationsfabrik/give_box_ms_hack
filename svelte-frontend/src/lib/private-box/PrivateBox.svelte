<script>
	import ImageUpload from '$lib/imageupload/ImageUpload.svelte';
</script>

<h1>Private Box veröffentlichen</h1>
<h3>Bitte stelle die benötigten Informationen für deine Box bereit.</h3>
<hr />
<form>
	<div>
		<label for="boxname"><b>Box-Name</b></label>
        <br>
		<input
			type="text"
			placeholder="Gebe deinen Box-Namen ein."
			name="boxname"
			id="boxname"
			required
		/>
	</div>
	<div>
		<label for="box-beschreibung"><b>Box-Beschreibung</b></label>
        <br>
		<input
			type="text"
			placeholder="Beschreibe deine Box und deren Inhalte"
			name="box-beschreibung"
			id="box-beschreibung"
			required
		/>
	</div>
	<div>
		<label for="box-kategorie"><b>Box-Kategorie</b></label>

		<select name="box-kategorie" id="box-kategorie" form="box-kategorie" required>
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
		<p>Durch hinzufügen deiner Box stimmst du unseren Bedingungen zu.<a href="#">AGB's</a>.</p>
		<button type="submit" class="private-box-creation">Private Box erstellen</button>
	</div>
</form>
