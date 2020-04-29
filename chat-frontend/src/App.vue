<template>
  <div id="app" class="m-0 p-0">
    <transition name="pages">
    <router-view/>
    </transition>
  </div>
</template>

<script>

</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Comic+Neue&display=swap');

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  width  : 100%;
}

.pages-enter, .pages-leave-to {
  opacity:0;
}
.pages-enter-to, .pages-leave {
  opacity :1;
}
.pages-enter-active , .pages-leave-active {
  transition: all .4s ease-in; 
}

</style>
