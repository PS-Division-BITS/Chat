<template>
    <div id="form" class="mx-auto container ">
      
        <input class="form-control" v-model="nick" placeholder="Enter your Nick" type="text" id="nickname" required/>
        <button class="btn mt-4 btn-outline-primary" @click="signup()" > Get Set Go</button>
   
    </div>
</template>

<script>

export default {
    data : function(){
        return {
            nick:"",
            password:"",
        }
    },
    created: ()=> {
        if(localStorage.user){
            this.$store.commit("updateUsername",localStorage.user);
            this.$router.push('Homepage')
        }    
    },
    
    methods:{
        signup(){   
        
            this.$axios.post('http://localhost:8000/chat/auth/users/',{username:this.nick,password:this.password})
            .then(response=>{
                console.log('response',response)
            })
            .catch(error=>{
                console.log('error',error)
            })  
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
    background:none;
}
</style>