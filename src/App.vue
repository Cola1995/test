<template>
  <div id="app">
   <Lheader/>
    <router-view/>
  </div>
</template>

<script>
import Lheader from './components/Lheader'
export default {
  name: 'App',
  components:{
    Lheader
  }
}
</script>

<style>
/* #app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
} */
</style>
