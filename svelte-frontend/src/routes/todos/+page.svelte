<script lang="ts">
    import { onMount } from 'svelte';
    let todoList;
    let title = '';

    onMount(async () => {
        todoList = await fetch('http://127.0.0.1:8081')
            .then((res) => res.json());
    });

    async function addToList () {
        const formData  = new FormData();
        formData.append('title', title);
        todoList = await fetch('http://127.0.0.1:8081/add', {
            method: 'Post',
            body: formData,
        }).then((res) => res.json())
    }

    async function deleteItem (id) {
        todoList = await fetch('http://127.0.0.1:8081/delete/' + id)
            .then((res) => res.json())
    }

    async function updateItem (id) {
        todoList = await fetch('http://127.0.0.1:8081/update/' + id)
            .then((res) => res.json())
    }
</script>

<section>
    <h1>TODO APP</h1>
    <div class="todo_item">
        <input bind:value={title} type="text" placeholder="new todo item..">
        <button on:click={addToList}>Add</button>
    </div>

    <br/>
    {#await todoList}
        <div>Waiting..</div>
        {:then res}
            {#if res !== undefined}
                {#each res.todo_list as item}
                    <div class="todo_item">
                        <div>
                            <input bind:checked={item.complete} type="checkbox" on:click={() => updateItem(item.id)} class="update">
                            <span class:checked={item.complete}>{item.title}</span>
                            <span on:click={() => deleteItem(item.id)} class="delete">❌</span>
                            <br/>
                        </div>
                    </div>
                {/each}
            {/if}
        {:catch error}
            <div>{error.message}</div>
    {/await}
</section>


<style>
    .todo_item{
        flex: 1;
        display: flex;
        flex-direction: column;
        padding: 1rem;
        width: 100%;
        max-width: 1024px;
        margin: 0 auto;
        box-sizing: border-box;
        text-align: center;
    }
    .delete, .update {
        cursor: pointer;
    }
    .checked {
        text-decoration: line-through;
    }
</style>