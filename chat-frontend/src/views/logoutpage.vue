<template>
   <div id="logoutpage" class="px-2  container-fluid">
       <HEADER class=""/>
      <div class="text-right "><a href="/"> <code>Login</code></a> </div>
    <div  id="thankyou" class="container text-left mt-3 p-0 mx-0">
       Thanks <br> for using our <br> Chat App!
    </div>

   <div class="container text-left mt-3 border border-dark  p-1">
        <h2>Have some great ideas?</h2>
        <h3 class="my-2">Let's do it together!</h3>
        <p style="font-size:1.2em;">
            We get inspired. <br> We learn. <br> We develop!
        </p>

        <span class="mt-2" style="font-size:1.2em;">
            Click <code><a href="https://github.com/PS-Division-BITS/Chat" target="_blank"> here </a> </code> to contact us! 
        </span>

       
    </div>
    
     <div class="mt-5 pt-3 text-left">
            Click <a href="https://github.com/PS-Division-BITS/Chat/issues/new"><code>here</code></a> to report issues in this progressive webapp!
        </div>
    <FOOTER/>
</div>  
</template>

<script>
import HEADER from '../components/header.vue'
import FOOTER from '../components/footer.vue'
export default {
    components : {
        HEADER,
        FOOTER
    },
    data : function(){
        return {
            key : this.$store.state.user.key,
        }
    },
    mounted: function(){
        
        localStorage.clear();
        
        this.$store.state.user.username="null";
        console.log('logout key : '+this.key)
        sessionStorage.clear();
        var params = new URLSearchParams()
        params.append('token',this.key)
        this.$axios({
                method : 'post',
                url : this.$store.state.URLS.logout,
                data : params
            })
            .then(response=>{
                console.log('logout Successful' + response.data)
            })
            .catch(error=>{
                console.log(error)
             
            })  

    }
}
</script>

<style lang="scss" scoped>

#logoutpage{
    
    height:auto;
    position:absolute;
    min-height: 100%;
background: #FFEEEE;  /* fallback for old browsers */
background: -webkit-linear-gradient(to right, #DDEFBB, #FFEEEE);  /* Chrome 10-25, Safari 5.1-6 */
background: linear-gradient(to right, #DDEFBB, #FFEEEE); /* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */

 div {
       font-family: 'Comic Neue', cursive;
  }
}
#thankyou 
{
    font-size: 2em;
}
</style>