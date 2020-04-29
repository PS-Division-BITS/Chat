<template>
    <div id="appname" class="h1 pt-3 text-center" :class="this.variant">
      Chat.Bpgc 
    </div>
</template>


<script>

export default {
  props:{
    variant: {type: String, default :"text-dark"}
  }
    
}
</script>


<style lang="scss" scoped>

#appname {
 font-family: 'Comic Neue', cursive;
}

</style>