 <template>
   
     <b-navbar type="light" variant="" class="mt-2" toggleable>
          <b-navbar-brand>Chat.Bpgc</b-navbar-brand>

         <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
            <b-collapse id="nav-collapse" is-nav >
                <b-navbar-nav class="ml-auto text-right">
                      <b-nav-item href="#" ><p class="m-0 p-0 text-center"><code>Hii {{username}}</code></p></b-nav-item>
                    <b-nav-item :to="{name : 'Homepage'}" waves-fixed>Campus Chat Room</b-nav-item>
                    <!-- <b-nav-item href="#" waves-fixed>1 on 1 Chat</b-nav-item>
                    <b-nav-item :to="{name : 'Chatrooms'}" waves-fixed>Custom Chat Rooms</b-nav-item> -->
                    <b-nav-item :to="{name : 'Logout'}" waves-fixed>Logout</b-nav-item>
                </b-navbar-nav>
            </b-collapse>
        </b-navbar>
</template>
<script>
export default {
    data : function(){
        return {
            username : this.$store.state.user.username
        }
    }
}
</script>