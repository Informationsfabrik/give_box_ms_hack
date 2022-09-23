<script>
    import { onMount, onDestroy } from 'svelte';
    import { browser } from '$app/environment';
    let leaflet;

    let mapElement;
    let map;
    let loc = [51.961940, 7.626057];

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
        });
    }


    onDestroy(async () => {
        if(map) {
            console.log('Unloading Leaflet map.');
            map.remove();
        }
    });
</script>


<main>
    <div bind:this={mapElement}></div>
    <button on:click={() => addMarker()}>bla</button>
</main>

<style>
    @import 'leaflet/dist/leaflet.css';
    main div {
        height: 800px;
    }
</style>
