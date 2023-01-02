<script lang="ts">
    import { ENV_OBJ } from '$lib/env'
    import Header from '$lib/header/Header.svelte';
    //import Footer from '$lib/footer/Footer.svelte';
    import { onMount } from 'svelte';
    import Map from '$lib/map/Map.svelte';
    import ResultList from '$lib/ResultList.svelte';
    import '../app.css';

    let search = "";
    let search_results = [];
    let search_city = "Münster";

    let boxes: any = [];

    let color_class: string;

    function searcher (e: any) {
        let v = e.target.value;
    }

    onMount(async () => {
        const res = await getBoxes();
        console.log("onMount log:")
        console.log(res)
        boxes = res;
    });

    const getBoxes = async () => {
        var response = await fetch(ENV_OBJ.API_URL + '/giveboxes', { headers: {'mode':'no-cors'}});
        var result = await response.json();
        console.log("getBoxes log:");
        console.log(result);
        return result;
    }
</script>

<!-- <Header /> -->


<div class="main-wrapper">
    <div class="boxes-section">
        <div class="navbar">
            <div class="logo-section">
                <div class="logo">
                    <img src="/logo.svg" style="width:128px; height:40px;" alt="Givebox Logo" />
                    <button class="add-box">
                        <img src="/add-box.svg" alt="add-box" />
                        neue Box eintragen
                    </button>
                </div>
            </div>
            <div class="menu">
                <img src="/menu.svg" alt="menu" />
            </div>
        </div>
        <div class="filter-bar">
            <div class="bar">
                <input class="filter-input" type="text" bind:value={search} on:keyup={(e) => searcher(e)} placeholder="Stichwort"/>
                <button class="filter">
                    <img src="/filter.svg" alt="filter" />
                    Filter
                </button>
            </div>
        </div>

        {#await getBoxes() then boxes}
            <ResultList boxList={boxes} />
        {/await}
    </div>

    {#await getBoxes() then boxes}
        <div class="map-section">
            <Map boxList={boxes} />
        </div>
    {/await}
</div>

<!-- <main>
    <section class="menu" class:color_class={color_class} style:background={search == "Buch" ? "#0f0" : "transparent"}>
        <div>
            <header>givebox</header>
            <button class="main">neuer eintrag</button>
        </div>
        <div class="flex-row">
            <input type="text" bind:value={search} on:keyup={(e) => searcher(e)} />
            <button>Filter</button>
        </div>
        <h2>{search_results.length} Ergebnisse für {search}</h2>
        <search_results />
    </section>
    <section class="map" style="outline:5px solid #0f0"><Map /></section>
</main> -->

<!-- <Footer /> -->

<style lang="scss">

    button {
        background: #FFFFFF;
        border: 1px solid #F1F1F1;
        box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.04);
        border-radius: 3px;
        color: #53586B;
        display: flex;
        align-items: center;
        gap: 8px;
        font-weight: 500;
    }

    .add-box {
        margin-right: 20px;
    }

    .main-wrapper {
        background: #fff;
        min-height: 100vh;
        display: flex;

        .boxes-section {
            padding: 30px;
            padding-top: 5px;
            min-width: 500px;
        }

        .navbar {
            display: flex;
            align-items: center;
            padding-bottom: 20px;
            border-bottom: solid 1px;
            border-color: #F6F6F6;
            margin-bottom: 30px;
            margin-top: 20px;
            .logo {
                display: flex;
                justify-content: space-between;
            }

            .logo-section {
                flex-grow: 1;
            }

            .menu {
                margin-top: 5px;
                margin-right: 15px;
                cursor: pointer;
            }

            .filter {
                background: #FFFFFF;
                border: 1px solid #F1F1F1;
                box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.04);
                border-radius: 3px;
                color: #53586B;
                display: flex;
                align-items: center;
                gap: 8px;

                &:hover {
                    
                }
            }
        }

        .filter-bar {
            margin-bottom: 30px;

            .bar {
                display: flex;
            }

            .filter-input {
                background: #F8F8F8;
                border-radius: 3px;
                height: 36px;
                flex-grow: 1;
                margin-right: 20px;
                background-image: url(/ico-search.svg);
                background-repeat: no-repeat;
                background-position-x: 18px;
                background-position-y: 11px;
                padding-left: 50px;
            }
        }
    }
</style>
