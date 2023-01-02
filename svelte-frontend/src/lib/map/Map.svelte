<script>
    import { onMount, onDestroy } from 'svelte';
    import { browser } from '$app/environment';
    import { Snackbar, Button, ClickOutside, MaterialApp  } from 'svelte-materialify';
    import ShortDescription from "$lib/short_description/ShortDescription.svelte";
    import { ENV_OBJ } from '$lib/env'
    let leaflet;
    let mapElement;
    let boxes;
    let map;
    let loc = [51.961940, 7.626057];
    let snackbar_val = false;
    let descr_obj = {
        "id": 1,
        "name": "bla",
        "address": "blup",
        "is_temporary": true,
        "description": "lores ipsum",
        "opening_hours": "11- 20"
    }

    const getBoxes = async () => {
		var response = await fetch(ENV_OBJ.API_URL +'/giveboxes', { headers: {'mode':'no-cors'}});
		var result = await response.json();
		return result;
	}

    onMount(async () => {
        if(browser) {
            leaflet = (await import('leaflet')).default;

            map = leaflet.map(mapElement).setView([51.961940, 7.626057], 13);

            leaflet.tileLayer('https://a.tile.openstreetmap.fr/hot/{z}/{x}/{y}.png', {
                attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
            }).addTo(map);

            let result = await getBoxes();
            result.forEach(function (value) {
                addMarker(value);
            });
        }
    });


    function addMarker(marker) {
        loc = [marker.latitude, marker.longitude]
        leaflet.marker(loc).addTo(map).on('click', async (e) => {
            let response = await fetch(ENV_OBJ.API_URL +'/giveboxes/' + marker.id, { headers: {'mode':'no-cors'}});
            var result = await response.json();
            descr_obj = result;
            snackbar_val = true;
        });
    }

    onDestroy(async () => {
        if(map) {
            console.log('Unloading Leaflet map.');
            map.remove();
        }
    });

    function clickOutside() {
        snackbar_val = false;
    }

</script>

    <map>
        <div bind:this={mapElement} id="map"></div>
        <button on:click={() => addMarker()}>bla</button>
        <div 
        use:ClickOutside 
        on:clickOutside={clickOutside}
        >
            <Snackbar 
                timeout={false} 
                class="flex-column" 
                style="width: 100%; height: 40%;" 
                bind:active={snackbar_val}
                bottom center>
                <ShortDescription snackbar={snackbar_val} description_object={descr_obj}/>
              </Snackbar>

        </div>
        </map>

<style>
    @import 'leaflet/dist/leaflet.css';
    map div {
        height: 100%;
        width: 100%;
        z-index: 1;
    }
</style>
