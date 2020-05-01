<template>
  <div id="app" class="m-0 p-0">
      <transition name="error">
       <div  class="table-danger" v-if="error" @click=' this.$state.commit("error",false,"")' id="error">
          {{errorMessage}} <span  style="position:absolute; right:15px;" class=" ml-auto"> <a href="#">&#10005;</a> </span>
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
        error:this.$store.state.error,
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
