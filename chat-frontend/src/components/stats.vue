<template>
<div id="wrapper">
     <div class="py-3" id="onlineUsers">
            <div class="">  Online users</div>
            <span class="text-secondary">Beta</span>
            <hr class="m-0 p-0">
            
            <div class="py-3 container-fluid d-flex flex-wrap">
                
                <div v-for="user in userList" :key="user.username" class=" my-1  mx-2"  >

                    <!-- <div class="img mt-2" style="float:left">
                        <img src="@/assets/paper-plane-solid.svg" class="img img-fluid" height="40px" width="40px">
                    </div> -->
                   
                     <div v-if="user.username!==username" @click="$emit('emitUsername',user.username)" class="username badge badge-primary text-left p-2" > {{user.username}}</div>
                                          <div v-else class="username badge badge-warning text-left p-2" > You</div>
                       <!-- <hr  class="m-0 p-0"> -->
                      <div class="text-left text-secondary" v-if="user.status">{{user.status}}</div>         
                </div>
            </div>
        </div>

            <hr >
        <div id="statistics" class="container-fluid py-3">
            Stats for Geeks
            <div class="text-secondary mt-5">
               <span v-if="attrs===[]"> There's not enough data to show you some weird stats</span>
               <span v-else v-for="p in attrs" :key="p.prop"> {{p.display}} :  {{values[p.prop]}}  <br></span>
               
            </div>
        </div>
</div>
</template>
<script>
export default {
    props:{
        userList:Array,
        username:String

    },
    data: function(){
        return {
            stat :"",
            attrs:[],
            values:{} 
            
        }
    },
    mounted : function(){
        this.getStats()
    },
    methods :{
        getStats(){
            this.$axios({
                method : 'get',
                url : this.$store.state.URLS.general.getStats
            })
            .then(response=>{
                    response = response.data; 
                    this.attrs=response.attrs;
                    this.values=response.values
                    console.log(response)
            })
            .catch(error=>{
                console.log(error)
               
              
            }) 
        }
    }

}
</script>
<style lang="scss" scoped>

#wrapper {
   
        background-color:rgba(234, 250, 250, 0.8);
      
    
}

#onlineUsers{
  
    height:40%;
    position:relative;
     font-family: 'Comic Neue', cursive;
     overflow-y:scroll;
    @media only screen and(min-width: 992px)
    {
           
        display: block;
    }

   .username {
     
   }
     .username:hover{
            cursor:pointer;   
            box-shadow: black 1px 1px 2px;
       }

 
}

#statistics {
    height:auto;
    overflow-y:scroll;
    font-weight: bold;
    background:rgba(175, 240, 240, 0.5);
    border-radius:45px 85px 45px 70px;
    padding-bottom:25px!important;
 
}
</style>