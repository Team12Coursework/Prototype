<template>
    <!-- Simple GoBack component allows the user to return to the page they were previously on, 
    this is used in several places throughout the project -->

    <span class="p-2 rounded text-white bg-blue-500 border-2 border-blue-500 hover:text-blue-500 hover:bg-white">
        <button @click="goBack">Return</button>
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
