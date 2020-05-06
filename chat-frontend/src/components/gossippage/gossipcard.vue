<template>
<div class='col-md-4 offset-md-1 px-3 mt-3' @click="goToRoom()" id="gossipcard">
   
 
    <div id="content" class=" ">
     {{data.name}}
    </div>
    <div  id="description" class=" container-fluid d-flex justify-content-around text-secondary mb-1 m-0 p-0">
         
           <span v-if="data.description" class="w-50">{{data.description}}</span>
             <span v-if="data.created_by" id="started" class="text-right w-50 "> Created by : <code>{{data.created_by}} </code> 
             </span>
        
        </div>
   
    <!-- <div v-if="data.users" class="" >
      
        Online users : 
        <span class="mx-1 w-50" v-for="user in data.users" :key="user"><img height="25px" width="25px" src="@/assets/profile-icon.png"></span>
    
    </div> -->

    <div v-if="data.count" id="reaction" class="d-flex py-1">
       <span class=" " id="counter"> + {{data.count}} </span>
           <span class="ml-auto" id="count" @click="!counted?data.count++:data.count--; counted = !counted" :class="{'text-success' : counted}" > +1 </span>
    </div>

</div>
</template>

<script>
export default {
    props:{
        data : Object
    },
    
    data :function(){
        return{
            counted :false,
          
        }
    },
    methods : {
        goToRoom(){
            this.$store.commit('updateChatRoom',this.data)
            console.log('Chatroom updated'+this.data.name)
            this.$router.push({name:'Homepage'})
        }
    }
}
</script>

<style lang="scss" scoped>



#gossipcard 
{
   z-index:1;
   background-color: rgba(161, 255, 206,.1);
   border-radius: 55px 5px 15px 0px;
   box-shadow: rgba(116, 214, 162, 0.4) 5px 2px 18px;
   font-family: 'Comic Neue';
   min-height:100px;
}

#gossipcard:hover {
        font-size: 105%;
        cursor: pointer;
         box-shadow: rgba(116, 214, 162, 1) 5px 5px 5px;
         padding-bottom: 15px !important;
   
}
span{
white-space: nowrap; 
  overflow: hidden;
  text-overflow: ellipsis;
}

#description{
    line-height: 1;
    font-style: italic;
    font-size: 90%;
}

#started {
 
    font-style:italic;
    code {
        font-size: 110%;
        font-style : normal;
    }
}

#content {
   font-size:2em;
    height:auto;

}

#counter {
    font-weight: bolder;
}
#count:hover {
    cursor:pointer;
}
</style>