<template>
  <div class="bg-light container-fluid" id="loginpage">
    <HEADER /> 
    <GUEST v-if="toggle" class="fade mt-5 pt-3 mb-2"/>
    <LOGIN v-if="toggle" class="fade mt-5"/>
    <RANDOM class="mt-5"/>
    <FOOTER class=""/>
  </div>
</template>

<script>

import HEADER from '../components/header.vue'
import GUEST from '../components/loginpage/guestUser.vue'
import LOGIN from '../components/loginpage/login.vue'
import RANDOM from '../components/loginpage/random.vue'
import FOOTER from '../components/footer.vue'

// import anime from 'animejs/lib/anime.es.js';
// anime({
//   targets: 'div',
//   translateX: 0,
//   rotate: '8turn',
//   backgroundColor: '#FFF',
//   duration: 1500
// });

export default {
  name: 'LoginPage',
  components: {
    HEADER,
    GUEST,
    LOGIN,
    RANDOM,
    FOOTER
  },
  data: function(){
    return {
      toggle:true,
    }
  }
}
</script>

<style lang="scss">

#loginpage {
  position:fixed;
  height:100%;
    font-family: 'Comic Neue', cursive;
     
  background: #FFEEEE;  /* fallback for old browsers */
background: -webkit-linear-gradient(to right, #DDEFBB, #FFEEEE);  /* Chrome 10-25, Safari 5.1-6 */
background: linear-gradient(to right, #DDEFBB, #FFEEEE); /* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */

}

.fade{
 
 -webkit-animation: fadeinout .5s linear forwards;
    animation: fadeinout .5s linear forwards;
}

@-webkit-keyframes fadeinout {
  0%{ opacity: 0; }
  100% { opacity: 1; }
}

@keyframes fadeinout {
  0% { opacity: 0; }
  100% { opacity: 1; }
}
</style>