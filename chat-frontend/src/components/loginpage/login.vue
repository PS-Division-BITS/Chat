<template>
    <div id="login">
        <form @submit.prevent="onSubmit">
           
        <div class="m-0 mb-2 p-0" v-if="this.error">     <code>  Under Construction!{{errorMessage}}</code></div>
        <input  class="form-control" v-model="username" placeholder="Enter your Nick ~Verified User" type="text" id="username" required/>
        <input  class="form-control" v-model="password" placeholder="Password goes here!" type="password" id="password" required autocomplete="true"/>
        <button type="submit" class="btn mt-4 btn-outline-primary"  disabled > Login</button> 

      </form>
     <p class="text-right mt-3" style="font-size:80%">Click <code> <a href="#"> here  </a></code> to verify your account!</p>
    </div>
</template>

<script>
export default {
    
    data : function(){
        return {
            username:"",
            password:"",
            error:true,
            errorMessage:"",
            }
    },


    // mounted: function() {
    //     if(localStorage.user){
    //         console.log('redirecting.... user = '+JSON.parse(localStorage.user).username+"XX")
    //         this.$store.commit("updateUser",JSON.parse((localStorage.user)));
    //         this.$router.push({name : 'Homepage'})
    //     }    
    // },

    methods :{

         onSubmit(){   
            this.error=false;
         
            const params = new URLSearchParams();
            params.append('username',this.username)
            params.append('password',this.password)
            this.$axios({
                method : 'post',
               // url : this.$store.state.URLS.login,
                data : params
            })
            .then(response=>{
                response=response.data;
             
                if(!response.error)
                {
                    // var username = response.user.username;
                    // var key = response.user.key;
                    
                //     var user = {"username":username,"key":key, verified:true}
                //   //  console.log('USER = %s key = %s ',username,key)
                //     localStorage.user=JSON.stringify(user);
                //    // console.log('saved in Local storage as '+JSON.stringify(user))
                //     this.$store.commit('updateUser',user)
                //   //  console.log('store user : '+this.$store.state.user)
                //     this.$router.push('/chat')
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