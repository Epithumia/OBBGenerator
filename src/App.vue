<template>
  <div id="app">
    <div>
      <o-b-b-generator />
    </div>
  </div>
</template>

<script>
import OBBGenerator from './components/OBBGenerator'

export default {
  name: 'App',
  components: {
    OBBGenerator
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
</style>
