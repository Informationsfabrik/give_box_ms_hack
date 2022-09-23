<script>
  import {
    MaterialApp,
    AppBar,
    Divider,
    Button,
    NavigationDrawer,
    Overlay,
    List,
    ListItem,
  } from "svelte-materialify";
  import { mdiMenu } from "@mdi/js";
  import Home from "./routers/Home.svelte";
  import About from "./routers/About.svelte";
  import QRCode from "./routers/QRCode.svelte";
  import Router, {location, push, pop, replace} from "svelte-spa-router";
  import {wrap} from 'svelte-spa-router/wrap'

  let active = false;
  function toggleNavigation() {
    active = !active;
  }
</script>

<MaterialApp theme="dark">
  <AppBar>
    <div slot="icon">
      <Button fab depressed on:click={toggleNavigation}>bla</Button>
    </div>
  </AppBar>
    <NavigationDrawer style="position: relative; flex: 1;" {active}>
      <List>
        <ListItem on:click={ () => push('/')}>Home</ListItem>
        <ListItem on:click={ () => push('/about')}>About</ListItem>
        <ListItem on:click={ () => push('/qr-code')}>QR-Code</ListItem>
      </List>
    </NavigationDrawer>
    <Router routes={{
      '/': Home,
      '/about': About,
      '/qr-code': QRCode
    }} />
  <Overlay {active} absolute on:click={toggleNavigation} index={1} />
  
  <hr>
  /#{$location}
</MaterialApp>
