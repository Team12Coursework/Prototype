<template>
    <navbar/>
    <main class="flex justify-center w-full">
        <div class="w-full max-w-7xl flex flex-col space-y-12 items-center">
            <div class="flex flex-col items-center pt-6">
                <h1 class="text-6xl font-bold">Character</h1>
                <h1 class="text-6xl font-bold">Connect</h1>
            </div>

            <div class="w-1/4 flex flex-col justify-center space-y-2" style="min-width: 512px;">
                <router-link class="button" to='/gamemodes'>Game Modes</router-link>
                <router-link class="button" to='/leaderboard'>Leaderboard</router-link>
            </div>
        </div>
    </main>

</template>



<script>
    import Navbar from "@/components/Navbar.vue"

    export default{
        components: {
            Navbar,
        }
    }

</script>

<style scoped>
.button {
    @apply border-2 border-blue-500 rounded-lg text-white font-bold p-4 bg-blue-500 hover:text-blue-500 hover:bg-white duration-200
}
</style>
