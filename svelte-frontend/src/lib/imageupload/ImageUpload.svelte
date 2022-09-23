<script>
    let  avatar, fileinput;
    const onFileSelected =(e)=>{
        let image = e.target.files[0];
        let reader = new FileReader();
        reader.readAsDataURL(image);
        reader.onload = e => {
            avatar = e.target.result
        };
    }
</script>

<div id="app">
    <h1>Upload Image</h1>

    {#if avatar}
        <img class="avatar" src="{avatar}" alt="d" />
    {:else}
        <p>No image uploaded</p>
    {/if}
    <button class="upload" on:click={()=>{fileinput.click();}}> Image upload </button>
    <input style="display:none" type="file" accept=".jpg, .jpeg, .png" on:change={(e)=>onFileSelected(e)} bind:this={fileinput} >
</div>

<style>
    #app{
        display:flex;
        align-items:center;
        justify-content:center;
        flex-flow:column;
    }

    .upload{
        display:flex;
        cursor:pointer;
    }
    .avatar{
        display:flex;
        height:200px;
        width:200px;
    }
</style>

