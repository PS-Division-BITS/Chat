<template>
    <div class="m-0 p-1 bg-light container-fluid" id="gossippage">
        
        <NAVBAR/>
    <div class="row container-fluid">
        <GOSSIPCARD
            v-for="data in gossips"
            :key="data.id"
            :data = data
         class="mt-2" />
    </div>


    </div>
</template>

<script>
import NAVBAR from '../components/navbar.vue'
import GOSSIPCARD from '../components/gossippage/gossipcard.vue'
export default {
    data:function(){
        return {
            gossips :[{'creator' : 'xyz','content' :'Only Single Girls come to A mess','count':45},{'creator' : 'ABC','content' :'Maths department is the horniest!','count':99}]
        }
    },
    components : {
        NAVBAR,
        GOSSIPCARD
    }

}
</script>

<style lang="scss" scoped>
#gossippage 
{
    position:fixed;
    height:100%;
    overflow-x: scroll;
}

</style>