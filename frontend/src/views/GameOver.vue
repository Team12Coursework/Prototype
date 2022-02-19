<template>
    <main class="flex flex-col h-screen">
        <navbar/>
        <div class="bg-main-man w-full flex flex-grow">
                <div class="w-full flex justify-around flex-col flex-grow items-center max-w-screen-md mx-auto">
                <div class="space-y-4">
                <div class="text-center text-8xl text-white font-bold">
                    GAME OVER
                </div>
                </div>
                    <div class="flex flex-col space-y-4">
                        <router-link class="button" to='/gamemodes'>Play Again</router-link>
                        <router-link class="button" to='/leaderboard'>Leader board</router-link>
                        <router-link class="button" to='/'> Return To Main Menu</router-link>
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
        }
    }

</script>

<style scoped>

.button {
    @apply border-4 text-black border-black text-2xl w-full text-center rounded-full font-bold py-4 px-16 bg-white hover:bg-black hover:text-white duration-200
}

.bg-main-man{
    background: url("../assets/bg-go.jpg");
    background-size: cover;
}

</style>
