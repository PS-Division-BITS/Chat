<template>
  <div class="bg-light container-fluid" id="loginpage">
    <HEADER /> 
    <LOGIN class="mt-5 "/>
    <RANDOM class="mt-5"/>
    <FOOTER class=""/>
  </div>
</template>

<script>

import HEADER from '../components/header.vue'
import LOGIN from '../components/loginpage/login.vue'
import RANDOM from '../components/loginpage/random.vue'
import FOOTER from '../components/footer.vue'

import anime from 'animejs/lib/anime.es.js';
anime({
  targets: 'div',
  translateX: 0,
  rotate: '8turn',
  backgroundColor: '#FFF',
  duration: 1500
});

export default {
  name: 'LoginPage',
  components: {
    HEADER,
    LOGIN,
    RANDOM,
    FOOTER
  }
}
</script>

<style lang="scss">

#loginpage {
  position:fixed;
  height:100%;
}

</style>