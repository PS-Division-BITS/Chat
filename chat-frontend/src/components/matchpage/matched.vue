<template>
     <div id="matched" class=" px-2  text-light">
       People you have matched with!


    </div>
</template>

<script>
export default {
    
}
</script>

<style lang="scss" scoped>

#matched {
  background: rgba(255, 106, 188, 0.5);
  
      // background: rgba(255, 106, 188, 0.473);  /* fallback for old browsers */
// background: -webkit-linear-gradient(to top, rgba(124, 145, 248,.8), rgba(245, 107, 135,.8));  /* Chrome 10-25, Safari 5.1-6 */
// background: linear-gradient(to top, rgba(124, 145, 248,.5), rgba(245, 107, 135,.5)); /* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */
height:70px;
width:95%;
 @media only screen and (min-width: 992px)
    {
        width:30%;
        

    }

input {
    background: rgba(255, 106, 188, 0.5);
    border-radius: 45px 0px 0px 45px;
    border:none;
}
button {
     border-radius: 0px 45px 45px 0px;
       background: rgba(255, 106, 188, 0.5);
   
}
 ::placeholder{
        color:whitesmoke;
        font-size: 75%;
    }
}

</style>