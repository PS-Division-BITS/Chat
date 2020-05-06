<template>
  <div id="app" class="m-0 p-0">
      <transition name="error">
       <div @click="$store.commit('error',false,'')" class="table-danger d-flex justify-content-around text-center" v-if="this.$store.state.error"  id="error">
         <div v-if="errorMessage"> {{$store.state.errorMessage}} </div> 
         <div v-else>Something's wrong</div>
         <div class="text-right ml-2 "> <span class="badge-danger badge"><a class="text-light" :href="this.$store.state.GITREPO+'issues/'" target="_blank"> Report Error </a></span></div>

       

          

        </div>
          
        </transition>
      
    <transition name="pages">
    <router-view/>
    </transition>
  </div>
</template>

<script>
export default {
  data : function(){
    return {
        error:false,
        errorMessage:this.$store.state.errorMessage,
    }
  }
}
</script>

<style lang="scss" scoped>
@import url('https://fonts.googleapis.com/css2?family=Comic+Neue&display=swap');

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  width  : 100%;
}
a{

  text-decoration: none;
  color:black;
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

.error-enter, .error-leave-to {
  transform: translateY(-15px);
}

.error-enter-active,.error-leave-active {
  transition: all .2s ease-in;
}

</style>
