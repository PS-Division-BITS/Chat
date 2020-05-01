<template>
    
    <div id="matchpage" class=" container-fluid">
         <sequential-entrance delay="500">
        <NAVBAR :variant="'dark'"/>
        <div class="text-light text h2 m-1" style="font-style:italic; "> Find your match  </div>
       <div class="row d-flex justify-content-around">
        <SWIPERIGHT/>
        <MATCHED/>
        </div>
        
         </sequential-entrance>
    </div>
</template>


<script>
import NAVBAR from '../components/navbar'
import SWIPERIGHT from '../components/matchpage/swiperight'
import MATCHED from '../components/matchpage/matched'
export default {
    components :{
        NAVBAR,
        SWIPERIGHT,
        MATCHED
    }
}
</script>

<style lang="scss" scoped>

#matchpage {
    position: fixed;;
    width:100%;
    height:100%;
    margin:0;
    
    padding:0;
  font-family: 'Comic Neue', cursive;
    background: #FC5C7D;  /* fallback for old browsers */
background: -webkit-linear-gradient(to top, rgb(124, 145, 248), rgb(245, 107, 135));  /* Chrome 10-25, Safari 5.1-6 */
background: linear-gradient(to top, rgb(106, 130, 250), rgb(243, 85, 117)); /* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */

}

</style>