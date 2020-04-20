<template>
<div id="homepage" class="m-0 p-0  container-fluid">
  
    <NAVBAR/>
    <CHATWINDOW class=""/>
    
</div>    
</template>
<script>

import NAVBAR from '../components/navbar.vue'
import CHATWINDOW from '../components/chatwindow.vue'
import anime from 'animejs/lib/anime.es.js';
anime({
  targets: 'div',
  translateX: 0,
  rotate: '10turn',
  backgroundColor: '#FFF',
  duration: 1500
});

export default {
    name : "homepage",
    components:{
        NAVBAR,
        CHATWINDOW,
      
    }
}
</script>
<style lang="scss" scoped>

#homepage {
  background: #FFEEEE;  /* fallback for old browsers */
background: -webkit-linear-gradient(to right,grey, lightgrey);  /* Chrome 10-25, Safari 5.1-6 */
background: linear-gradient(to right,#78d1d2, #cde4ad); /* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */

  position:fixed;
  height:100%;
}
</style>