<script>
    import { Html5Qrcode } from "html5-qrcode";
    import { onMount } from "svelte";

    let scanning = false;

    let html5Qrcode;

    onMount(init);

    function init() {
        html5Qrcode = new Html5Qrcode("reader");
    }

    function start() {
        html5Qrcode.start(
            { facingMode: "environment" },
            {
                fps: 10,
                qrbox: { width: 250, height: 250 },
            },
            onScanSuccess,
            onScanFailure
        );
        scanning = true;
    }

    async function stop() {
        await html5Qrcode.stop();
        scanning = false;
    }

    function onScanSuccess(decodedText, decodedResult) {
        alert(`Code matched = ${decodedText}`);
        console.log(decodedResult);
    }

    function onScanFailure(error) {
        console.warn(`Code scan error = ${error}`);
    }
</script>

<qr_code>
    {#if scanning}
        <button on:click={stop}>stop</button>
    {:else}
        <button on:click={start}>start</button>
    {/if}
    <reader id="reader" />
</qr_code>

<style>
    qr_code {
        display: flex;
        flex-direction: column;
    }
    reader {
        width: 100%;
        background-color: black;
    }
</style>
