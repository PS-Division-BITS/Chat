<template>
    <div class="m-0 p-1 bg-light container-fluid" id="gossippage">
        
        <NAVBAR/>
    <div class="row container-fluid">
        <GOSSIPCARD
            v-for="data in rooms"
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
            rooms :[{'creator' : 'xyz','name' :'AH3 Hostel','count':45, uri:'/das/'},{'creator' : 'ABC','name' :'Matheletes','count':99}]
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
                url : this.$store.state.general.getRooms+'?token='+token
                
            })
            .then(response=>{
                    response = response.data;
                    this.rooms=response;
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