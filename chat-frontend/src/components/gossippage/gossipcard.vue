<template>
<div class='col-md-4 offset-md-1 px-3 mt-3' @click="goToRoom()" id="gossipcard">
   
 
    <div id="content" class="text-left h3 ">
     {{data.name}}
    </div>
    <div v-if="data.description" id="description" class="text-left text-secondary mb-1 m-0 p-0">
          <span>{{data.description}}</span>
        </div>
     <div v-if="data.creator" id="started" class="text-left "> Created by : <code>{{data.creator}} </code> 
    </div>
    
    <div v-if="data.count" id="reaction" class="d-flex py-1">
       <span class=" p-1 text-left" id="counter"> + {{data.count}} </span>
           <span class="p-1 ml-auto" id="count" @click="!counted?data.count++:data.count--; counted = !counted" :class="{'text-success' : counted}" > +1 </span>
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
   border-radius: 15px 80px 5px 15px;
   box-shadow: rgba(116, 214, 162, 0.4) 5px 2px 18px;
   font-family: 'Comic Neue';
}

#gossipcard:hover {
        font-size: 110%;
        cursor: pointer;
         box-shadow: rgba(116, 214, 162, 1) 5px 5px 5px;
   
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
    line-height: 150%;
    height:auto;
}

#counter {
    font-weight: bolder;
}
#count:hover {
    cursor:pointer;
}
</style>