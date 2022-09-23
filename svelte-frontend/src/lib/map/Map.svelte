<script>
    import { onMount, onDestroy } from 'svelte';
    import { browser } from '$app/environment';
    let leaflet;

    let mapElement;
    let map;

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
        leaflet.marker([51.961940, 7.626057]).addTo(map)
                .bindPopup('A pretty CSS3 popup.<br> Easily customizable.')
                .openPopup();
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
