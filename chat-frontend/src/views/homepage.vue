<template>
<div id="homepage" class="m-0 p-0 bg-light container-fluid">
  
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
  position:fixed;
  height:100%;
}
</style>