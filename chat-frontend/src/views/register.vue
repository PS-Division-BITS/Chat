<template>
<div class="container-fluid" id="registerpage">
    <transition name="headerT">
            <HEADER
                v-bind:variant="'text-light'"
            />
    </transition>

    <transition name="translate">
        <div v-if="pagemounted" class=" translate text-light  my-4 h3">
            Get Started!
          
        </div>
    </transition>
   

    <transition name="bounce-in">
          <span class="text-light"> Registration option comming soon!</span>
        <div v-if="false" class="form-container">
            <form>
                     <transition name="translate">
                        <div v-if="error" style="font-size:90%;font-style:italic;" class="text-light m-0 p-0 ">
                            {{errorMessage}}
                        </div>
                    </transition>
                         
                           <div class="input-group container-fluid m-0 p-0 ">
                            <input :disabled="this.usernameSubmitted" v-model="email" class="form-control text-light" placeholder="College email goes here...">
                             </div>
                           
                            <transition name="translate">
                             <div v-if="this.emailreg.test(this.email)" class="input-group container-fluid my-3 p-0 ">
                              <input :disabled="this.usernameSubmitted" v-model="username" class="form-control text-light" placeholder="Username here..."> 
                              <button :disabled="this.usernameSubmitted" class="btn btn-outline-light mx-2" @click="verifyUsername()">
                                    <span v-if="!this.loading">Verify</span>
                                    <span v-else> Verifying...<img  class="img img-fluid" height="15px" width="20px"  src="@/assets/loading.gif" /> </span>

                              </button>
                            
                                <!-- <span v-if="this.user" class="text-light p-1 mx-2" style="font-size:80%; font-style:italic;">
                                    Username already exists!
                                </span> -->

                             </div>
                            </transition>




                               <transition name="translate">
                             <div v-if="usernameSubmitted" class="input-group container-fluid my-3 p-0 ">
                                 <div>
                                 <input type='password' v-model="password1" class="form-control text-light" placeholder="Enter your password"> 
                                 </div>
                                 <div>
                                 <input type='password' v-model="password2" class="form-control text-light" placeholder="Password again..."> 
                                 </div>
                                 <div>
                                <span class="text-light" v-if="password2!=='' && password1 !== password2"> Passwords ain't matching bruh</span>
                                </div>
                             </div>
                            </transition>


                              <transition name="translate">
                             <div v-if="password1==password2 && password1!==''" class="input-group container-fluid my-3 p-0 ">
                                 <button  class="btn btn-outline-light">   Send Verification Code </button>
                             </div>
                            </transition>




                  
                    
            </form>
        </div>
    </transition>

<div class="text-center">
</div>


<FOOTER
 v-bind:variant="'text-light'" />
</div>
</template>



<script>
import FOOTER from '../components/footer'
import HEADER from '../components/header'
export default {
    name : "registerPage",
    components : {
        FOOTER,
        HEADER
    },
    data : function(){
        return {
            pagemounted:false,
            username:"",
            password1:"",
            password2:"",
            email:"",
            emailreg :  /^([a-zA-Z0-9_\-.]+)@([a-zA-Z0-9_\-.]+)\.([a-zA-Z]{2,5})$/,
            error:"",
            errorMessage:"",
            usernameSubmitted:false,
            loading:false,
            registrationToken:"",
            
            
        }
    },

    methods : {


        verifyUsername ()
        {
            this.loading = true;
             this.usernameSubmitted=true;   
             this.loading=false;
            
        },


        register(){
            this.loading=true;

           const params = new URLSearchParams();
            params.append('email',this.email)

             this.$axios({
                method : 'post',
                url : this.$store.state.URLS.sendOTP,
                data:params
               
            })
            .then(response=>{
              console.log(response)
            })

        }

    },
    mounted () {
       
       this.pagemounted = true;
    },
    watch :{
        // email: function() {
        //   if(!this.emailreg.test(this.email))
        //   {     
            
        //       this.error=true
        //       this.errorMessage="Invalid Email"
        //       this.showVerifyButton=false;
        //   }
        //   else {
        //             if(this.username==="" || this.password ==="")
        //             this.error=false;   
        //   }
        // }
    }
    
}
</script>


<style lang="scss" scoped>
#registerpage{
     position: absolute;
  height:100%;
 
  background: #355C7D;  /* fallback for old browsers */
background: -webkit-linear-gradient(to right, #C06C84, #6C5B7B, #355C7D);  /* Chrome 10-25, Safari 5.1-6 */
background: linear-gradient(to right, #C06C84, #6C5B7B, #355C7D); /* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */

}
.translate {
    z-index:1;
    text-shadow: black 1px 1px 4px;
    
}
.form-container {
    position:absolute;
    margin:auto !important;
   top:40%;
   left:15%;
    input{
    background: none!important;
    border:none !important;
    }

    ::placeholder{
        color:gainsboro;
    }
}







.translate-enter, .translate-leave-to {
  opacity:0;
   transform: translateX(50px);
}
.translate-enter-to, .translate-leave {
  opacity :1;
}
.translate-enter-active , .translate-leave-active {
    transition: all 2s ease;
}






@keyframes bounce-in {
  0% {
    transform: scale(0);
  }
  50% {
    transform: scale(1.5);
  }
  100% {
    transform: scale(1);
  }
}
</style>