<template>
  <div id="app">
    <img id="logo" alt="Vue logo" src="./assets/logo.png">
    <search-and-results />
  </div>
</template>

<script>
import SearchAndResults from './components/organisms/SearchAndResults.vue';

import axios from 'axios';

// Fix CORS issues
axios.defaults.headers.common['Access-Control-Allow-Origin'] = '*';

export default {
  name: 'App',
  components: {
    SearchAndResults
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

#logo {
  width: 200px;
  margin: 20px;
}
</style>
