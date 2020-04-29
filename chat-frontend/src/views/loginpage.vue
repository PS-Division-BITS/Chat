<template>
  <div class="bg-light container-fluid" id="loginpage">
    <HEADER /> 
      <div style="font-size:1.2em" class="row mt-5 d-flex justify-content-around">

     <span @click="toggle=false" class="rounded p-2"  style="cursor:pointer;" :class="!toggle?'selected':'text-secondary'">  Login as Guest</span>
      <span style="cursor:pointer;"  class="rounded p-2" :class="toggle?'selected':'text-secondary'" @click="toggle=true">Login</span>
      </div>

  <transition name="flip">
    <GUEST v-if="!toggle" class="flip mt-5 mb-2"/>
  
    <LOGIN v-if="toggle" class="flip mt-5"/>
  </transition>
    <RANDOM style="position:absolute; left:12%; bottom:20%;" class="text-center mt-5"/>
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
      toggle:false,
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


.selected{
  text-transform: uppercase;
  font-weight: bold;
  border-bottom: 2px solid black ;
  

}

.flip-enter, .flip-leave-to {
  opacity : 0;
  transform: rotateY(90deg);
}
.flip-leave, .flip-enter-to {
 opacity: 1;
  transform: rotateX(45deg);
}



.flip-enter-active, .flip-leave-active {
  transition: all .8s;
 
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