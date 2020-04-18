<template>
    <div  id="form" class="mx-auto container ">
      <form @submit.prevent="onSubmit">
        <div class="m-0 mb-5 p-0" v-if="error">     <code>{{errorMessage}}</code></div>
        <input class="form-control" v-model="nick" placeholder="Enter your Nick" type="text" id="nickname" required/>
        <button type="submit" class="btn mt-4 btn-outline-primary"  > Get Set Go</button>
      </form>
    </div>
</template>

<script>

export default {
    data : function(){
        return {
            nick:"",
            error:false,
            errorMessage:""
            
        }
    },
    mounted: function() {
        if(localStorage.user){
            this.$store.commit("updateUser",JSON.parse(localStorage.user));
            this.$router.push({name : 'Homepage'})
        }    
    },
    
    methods:{
        onSubmit(){   
        
            this.$axios.get(this.$store.state.AUTHBASEURL+'users/?username='+this.nick)
            .then(response=>{
                response=response.data;

                if(!response.error)
                {
                    localStorage.user = JSON.parse(response.user)
                    this.$store.commit('updateUser',response.user)
                    this.$router.push('/chat')
                }
                else
                {
                    this.error=true;
                    this.errorMessage=response.message;
                }

            })
            .catch(error=>{
                console.log('ERROR :',error)
                        /* has to be moved to try block */ 
                 
              
              
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