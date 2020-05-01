 <template>
   
     <b-navbar :type="this.variant"  class="mt-2 text-light" toggleable>
         
          <b-navbar-brand id="brand">Chat.Bpgc</b-navbar-brand>
      
         <b-navbar-toggle target="nav-collapse" :key='1'></b-navbar-toggle>
           
            <b-collapse  id="nav-collapse" :key='2' is-nav >
                 <sequential-entrance delay="100">
                <b-navbar-nav class="ml-auto text-right">
                    <b-nav-item class="nav-item" href="#" ><p id="username" class="m-0 p-0 text-center">Hii {{user.username}}</p></b-nav-item>
                    <b-nav-item class="nav-item" :to="{name : 'Homepage'}" waves-fixed>Chat window</b-nav-item>
                    <b-nav-item  class="nav-item" v-if="!this.user.verified" :to="{name : 'Register'}" waves-fixed><span class="text-secondary m-0 p-0" style="font-size:90%; font-style:italic;">Register to use our other features!</span> <span style="font-size:85%; " class="m-0 p-0 text-grey"><br> Private Chat | Match Finder! | Multiple Rooms Access. </span></b-nav-item>
                    <b-nav-item class="nav-item" v-if="this.user.verified" :to="{name :'Chatrooms'}" waves-fixed> Other Chat Rooms </b-nav-item>
                    <b-nav-item class="nav-item" v-if="this.user.verified" :to="{name :'Match'}" waves-fixed> Match Maker </b-nav-item>
                    <!-- <b-nav-item href="#" waves-fixed>1 on 1 Chat</b-nav-item>
                    <b-nav-item :to="{name : 'Chatrooms'}" waves-fixed>Custom Chat Rooms</b-nav-item> -->
                    <b-nav-item class="nav-item" :to="{name : 'Logout'}" waves-fixed>Logout</b-nav-item>
                </b-navbar-nav>
                  </sequential-entrance>
            </b-collapse>
        
        </b-navbar>
      
</template>
<script>
export default {
     props:{
    variant: {type: String, default :"light"}
  },
    data : function(){
        return {
            user: this.$store.state.user
        }
    }
}
</script>

<style lang="scss" scoped>
#brand{
     font-family: 'Comic Neue', cursive;
     
     
}
#username{
     font-family: 'Comic Neue', cursive;
}


.nav-item:hover{
font-size:101% ;
cursor:pointer;
text-shadow:cadetblue 3px 3px 5px;

#username{
  text-shadow:cornflowerblue 4px 4px 5px;
}
}
</style>