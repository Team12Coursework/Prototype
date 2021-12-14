<template>
    <main class="flex flex-col h-screen">
        <navbar/>

        <div class="w-full border flex flex-grow justify-center flex-col transform -translate-y-12 items-center">
            <div class="w-full flex flex-col max-w-screen-md">
                <div class="w-full flex flex-col items-center justify-center space-y-4">
                    <div class="flex flex-wrap flex-col justify-center items-center pb-24 space-y-2">
                        <div class="flex space-x-4">
                            <h1 v-for="letter in firstWord" :key="letter" class="h-36 flex justify-center items-center w-36 rounded-xl text-white text-8xl font-bold text-center bg-blue-400">{{ letter }}</h1>
                        </div>
                        <div class="flex space-x-4">
                            <h1 v-for="letter in secondWord" :key="letter" class="h-36 flex justify-center items-center w-36 rounded-xl text-white text-8xl font-bold text-center bg-blue-400">{{ letter }}</h1>
                        </div>
                    </div>

                    <router-link class="button" to='/gamemodes'>New Game</router-link>
                    <router-link class="button" to='/gamemodes'>Join Game</router-link>
                    <router-link class="button" to='/gamemodes'>Leaderboard</router-link>
                </div>
            </div>
        </div>
    </main>
</template>



<script>
    import Navbar from "@/components/Navbar.vue"

    export default{
        components: {
            Navbar,
        },

        data() {
            return {
                firstWord: "CHARACTER",
                secondWord: "CONNECT",
            }
        }
    }
</script>

<style scoped>
.button {
    @apply border-8 border-blue-500 text-4xl w-full text-center rounded-full text-white font-bold p-8 bg-blue-300 hover:text-blue-500 hover:bg-white duration-200
}
</style>
