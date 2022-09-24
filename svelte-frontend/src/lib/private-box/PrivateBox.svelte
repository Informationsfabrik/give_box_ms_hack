<script>
	import ImageUpload from '$lib/imageupload/ImageUpload.svelte';
	// longitude = Column(Float)
	// latitude = Column(Float)
	// address = Column(Integer, ForeignKey("Addresses.id"), nullable = False)
	// opening_hours = Column(String)
	// is_temporary = Column(Boolean)
	// description = Column(String)
	// last_confirmation_date = Column(DateTime)
	// maintainer = relationship("User", secondary=user_givebox_association,back_populates="giveboxes")
	// image_link = Column(String)
	// tags = Column(JSON)
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
	</div>
</form>
