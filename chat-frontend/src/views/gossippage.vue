<template>

    <div class="m-0 p-1 bg-light container-fluid" id="gossippage">
        <sequential-entrance delay="500">
        <NAVBAR/>
    <div class="row container-fluid d-flex justify-content-lg-between">
        <GOSSIPCARD
            v-for="data in rooms"
            :key="data.id"
            :data = data
         class="mt-2" />
    </div>

</sequential-entrance>
    </div>

</template>

<script>
import NAVBAR from '../components/navbar.vue'
import GOSSIPCARD from '../components/gossippage/gossipcard.vue'
export default {
    data:function(){
        return {
            rooms :[],//[{'creator' : 'xyz',description:'Timepassdsadasdsadasdasdasdadasddadsad','name' :'AH3 Hostel','count':45, uri:'/das/',users:['1','2','3','4','5']},{'creator' : 'creator',description:"description",'name' :'name','count':'count', uri:'uri',users:'[dsadsaadadasda]'}]
        }
    },
    components : {
        NAVBAR,
        GOSSIPCARD
    },

    mounted()
    {     
        this.getRooms()
    },
    methods :{

        getRooms(){
           
           var token = this.$store.state.user.key;
            this.$axios({
                method : 'get',
                url : this.$store.state.URLS.general.getRooms+'?token='+token
                
            })
            .then(response=>{
                    response = response.data;
                    var res;
                    for (res in response)
                      this.rooms.push(response[res]);
                    console.log(response,"rooms")
            })
            .catch(error=>{
                console.log(error)
              
            })  
        }

    }
}
</script>

<style lang="scss" scoped>
#gossippage 
{
    background: #A1FFCE;  /* fallback for old browsers */
    background: -webkit-linear-gradient(to right, #FAFFD1, #A1FFCE);  /* Chrome 10-25, Safari 5.1-6 */
    background: linear-gradient(to right, #FAFFD1, rgb(161, 255, 206)); /* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */

    position:fixed;
    height:100%;
    overflow-x: scroll;
}

</style>