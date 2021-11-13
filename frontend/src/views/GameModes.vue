<template>
    <navbar/>

    <main class="flex flex-col w-full items-center pt-6">
            <h1 class="text-6xl font-bold">Select A Game Mode</h1>

            <div class="w-1/2 max-w-xl flex flex-col items-center space-y-2 mt-4">
                <router-link class="button" to="/play">General</router-link>
                <router-link class="button cursor-not-allowed" to="">Mathematics (LOCKED)</router-link>
                <router-link class="button cursor-not-allowed" to="">Science (LOCKED)</router-link>
                <router-link class="button cursor-not-allowed" to="">Custom (LOCKED)</router-link>
            </div>

            <go-back class="mt-2" />
    </main>
    
</template>


<script>
    import Navbar from '@/components/Navbar.vue'
    import GoBack from '../components/GoBack.vue'

    export default{
        components:{
            Navbar,
            GoBack,        
        }
    }
</script>


<style scoped>
.button {
    @apply p-2 w-full border-2 border-blue-500 bg-blue-500 text-white hover:bg-white hover:text-blue-500 rounded-lg duration-200
}
</style>
