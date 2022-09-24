<script lang="ts">
    export let box;
</script>

<a class="box" href="/box/{box.id}" onClick="return false;">
    <!--class:selected="{selected_id === id}"-->
    <div class="icon">
        <img src="/regal.svg" alt="Regal" />
    </div>
    <div class="entry">
        <h3>{box.title}</h3>
        <address>{box.street} {box.house_number} {box.zip_code} {box.city}</address>
        <span>offen: {box.opening_hours}</span>
        <ul class="tags">
            {#each Object.entries(box.content) as [key, value]}
                {#if value === true}
                    <li>{key}</li>
                {/if}
            {/each}
        </ul>
    </div>
</a>

<style lang="scss">
* {
    font-size: 13px;
    line-height: 140%;
}
.box {
    background: #FFFFFF;
    border: 1px solid #F1F1F1;
    box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.04);
    border-radius: 5px;
    padding: 8px;
    display: flex;
    flex-direction: row;
    align-items: center;
    margin-bottom:15px;

    * {
        color: #33384B;
    }
}
.box:hover {
    text-decoration: none;
}
.box.selected {
    border-left: 4px solid #394a3e;
}
.icon {
    box-sizing: border-box;
    padding: 10px;
    height: 100px;
    width: 100px;
    margin-right: 10px;
    display: flex;
    align-items: center;
    justify-content: center;
}
h3 {
    font-weight: 700;
    font-size: 15px;
    color: #33384B;
    display: block;
    margin-top: 4px;
}
address {
    font-weight: 400;
    color: #5A5D68;
    display: block;
    font-style: normal;
}
ul {
    list-style: none;
    margin: 8px 0;
    padding: 0;
}
li {
    font-weight: 700;
    background: #F2F2F2;
    border-radius: 5px;
    color: #444;
    padding: 3px 6px;
    margin-right: 4px;
    display: inline-block;
}
</style>