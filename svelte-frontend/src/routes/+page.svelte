<script lang="ts">
    import HelloWorldComponent from '$lib/HelloWorldComponent.svelte';
</script>

<!-- Tab Beschreibung -->
<svelte:head>
    <title>GiveBox</title>
    <meta name="description" content="BlaBliBlub" />
</svelte:head>

<section>
    <h1>Welcome</h1>
    <HelloWorldComponent/>
    <a href="/todos">todos</a>
</section>

<style>
    section {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        flex: 1;
    }

    h1 {
        width: 100%;
    }
</style>