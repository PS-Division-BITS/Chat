<template>
    <div  id="form" class="mx-auto container ">
      <form @submit.prevent="onSubmit" @submit="signup()">
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
          
            
        }
    },
    mounted: function() {
        if(localStorage.user){
            this.$store.commit("updateUser",JSON.parse(localStorage.user));
            this.$router.push({name : 'Homepage'})
        }    
    },
    
    methods:{
        signup(){   
        
            this.$axios.get(this.$store.state.AUTHBASEURL+'users/?username='+this.nick)
            .then(response=>{
                console.log('response successful : ',response)
                this.$store.state.username=this.username
            })
            .catch(error=>{
                console.log('ERROR :',error)
                        /* has to be moved to try block */ 
                   var success = true;
                var user = {username:'abc',key:'aaabbbccc'};
                if(success)
                {
                    localStorage.user = JSON.stringify(user)
                    this.$store.commit('updateUser',user)
                }
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