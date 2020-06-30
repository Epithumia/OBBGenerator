<template>
  <div id="app">
    <div>
      <o-b-b-generator />
    </div>
    <footer class="footer">
      With icons made by&nbsp;<a href="https://www.flaticon.com/authors/pixel-perfect">Pixel perfect</a>&nbsp;from&nbsp;<a href="http://www.flaticon.com/" target="_blank" rel="noopener noreferrer">www.flaticon.com</a>
    </footer>
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
/* Sticky footer styles
-------------------------------------------------- */
html {
  position: relative;
  min-height: 100%;
}
body {
  margin-bottom: 60px; /* Margin bottom by footer height */
}
.footer {
  position: absolute;
  bottom: 0;
  width: 100%;
  height: 60px; /* Set the fixed height of the footer here */
  line-height: 60px; /* Vertically center the text there */
  background-color: #f5f5f5;
}
</style>
