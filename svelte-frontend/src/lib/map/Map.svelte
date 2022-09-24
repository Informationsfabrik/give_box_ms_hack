<script>
    import { onMount, onDestroy } from 'svelte';
    import { browser } from '$app/environment';
    import { Snackbar, Button, ClickOutside, MaterialApp  } from 'svelte-materialify';
    import ShortDescription from "$lib/short_description/ShortDescription.svelte";
    let leaflet;
    
    let mapElement;
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

    onMount(async () => {
        if(browser) {
            leaflet = (await import('leaflet')).default;

            map = leaflet.map(mapElement).setView([51.961940, 7.626057], 16);

            leaflet.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
                attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
            }).addTo(map);
        }
    });


    function addMarker() {
        loc = [loc[0] + 0.001, loc[1] + 0.001]
        leaflet.marker(loc).addTo(map).on('click', function(e) {
            console.log(e.latlng);
            console.log(e);
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
