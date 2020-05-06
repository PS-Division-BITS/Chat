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
                   
                     <div @click="$emit('emitUsername',user.username)" class="username badge badge-primary text-left p-2">{{user.username}} </div>
                     
                       <!-- <hr  class="m-0 p-0"> -->
                      <div class="text-left text-secondary" v-if="user.status">dsd {{user.status}}</div>         
                </div>
            </div>
        </div>


        <div id="statistics" class="container-fluid py-3">
            Weird Stats
            <div class="text-secondary mt-5">
               <span> There's not enough data to show you some weird stats</span>
            </div>
        </div>
</div>
</template>
<script>
export default {
    props:{
        userList:Array

    },
    data: function(){
        return {
            stat :""
        }
    },
    methods :{
        emitUsername(username){
            console.log(username)
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
    height:50%;
    overflow-y:scroll;
 
}
</style>