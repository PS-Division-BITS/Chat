<template>
<div class='col-md-4 offset-md-1 mt-3 border ' id="gossipcard">
    <div id="started" class="text-left py-1"> <code >{{data.creator}} </code> says  
    </div>
    <hr class="m-0 p-0">
    <div id="content" class="text-left py-3">
     {{data.content}}
    </div>

    <div id="reaction" class="d-flex py-1">
       <span class="border p-1 text-left" id="counter"> + {{count}} </span>

           <span class="p-1 ml-auto" id="count" @click="!counted?count++:count--; counted = !counted" :class="{'text-success' : counted}" > +1 </span>
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
            count : this.data.count
        }
    }
}
</script>

<style lang="scss" scoped>
#gossipcard 
{
   
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