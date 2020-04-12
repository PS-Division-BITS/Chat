<template>
    <div id="randomtext">
        {{quotes[0]}}
    </div>
</template>

<script>
export default {
name : "random",
data : function(){
    return{
        quotes:['REMEMBER, Too much Agreement kills a chat! ']
    }
}    
}
</script>

<style lang="scss" scoped>
#randomtext {
    font-size: smaller;
    font-style: italic;
}
</style>