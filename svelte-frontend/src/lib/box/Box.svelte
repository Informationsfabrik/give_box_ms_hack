<script>import { ENV_OBJ } from '$lib/env'
   export let boxId;
   let image_response;

   const getBox = async () => {
      var response = await fetch(ENV_OBJ.API_URL + '/giveboxes/' + boxId, { headers: {'mode':'no-cors'}});
      image_response = await fetch(ENV_OBJ.API_URL + '/titleimages/' + boxId, { headers: {'mode':'no-cors'}});
      image_response = await image_response.json();
      image_response = image_response.data
      return await response.json();
   }

   let boxPromise = getBox();

</script><h1>Box {boxId}</h1>{#await boxPromise then box2}
   <img src="{image_response}" alt="IMAGE" /><table>{#each Object.entries(box2) as [key, value], index}
         <tr><td>{key}</td><td>{value}</td></tr>{/each}
   </table><!--   <img src="https://api.givebox-ms.de/giveboxes/image/{boxId}" alt="image of a givebox" />-->{/await}
<style></style>

