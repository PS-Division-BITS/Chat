<template>
    <div id="form" class="mx-auto container ">
        <input class="form-control" v-model="nick" placeholder="Enter your Nick" type="text" id="nickname" required/>
    <button class="btn mt-3 btn-outline-primary" @click="verify()" > Get Set Go</button>
    </div>
</template>

<script>
export default {
    data : function(){
        return {
            nick:""
        }
    },
    methods:{
        verify(){
          
            this.$store.nick = this.nick;
              console.log('verified');
        }
    }
}
</script>

<style lang="scss" scoped>


#form {
     font-family: 'Comic Neue', cursive;
}

input {
    background:none;
    border:none;
    border-bottom: 2px solid black;
}
input:focus {
    border:none;
}
</style>