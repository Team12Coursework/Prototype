<template>
    <!-- Simple GoBack component allows the user to return to the page they were previously on, 
    this is used in several places throughout the project -->

    <span class="p-2 rounded cstm-button text-white bg-blue-500 border-2 border-blue-500 hover:text-blue-500 hover:bg-white">
        <button @click="goBack" class="flex items-center"><svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 0 24 24" width="24px"><path d="M0 0h24v24H0V0z" fill="none"/><path d="M15.41 7.41L14 6l-6 6 6 6 1.41-1.41L10.83 12l4.58-4.59z"/></svg>Return</button>
    </span>
</template>

<script>
export default{
    methods: {
        goBack() {
            return this.$router.go(-1);
        }
    }
}
</script>

<style>
.cstm-button svg{
    fill: white;
}
.cstm-button:hover svg{
    fill: rgb(59 130 246);
}
</style>
