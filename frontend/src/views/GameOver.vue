<template>
    <main class="flex flex-col h-screen">
        <navbar/>
        <div class="bg-main-man w-full flex flex-grow">
                <div class="w-full flex justify-around flex-col flex-grow items-center max-w-screen-md mx-auto">
                <div class="space-y-4">
                <div class="text-center text-8xl text-white font-bold game-over font-effect-anaglyph">
                    GAME OVER
                </div>
                </div>
                    <div class="flex flex-col space-y-4">
                        <router-link class="button" to='/gamemodes'>PLAY AGAIN</router-link>
                        <router-link class="button" to='/leaderboard'>LEADERBOARD</router-link>
                        <router-link class="button" to='/'>RETURN TO MAIN MENU</router-link>
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
@import url('https://fonts.googleapis.com/css2?family=Shadows+Into+Light&effect=anaglyph');
.button {
    @apply text-white text-2xl w-full text-center rounded-full font-bold py-4 px-16 hover:bg-black hover:text-white duration-200
}
.button{
    background-color:#4a4a4a47;
    font-family: 'Shadows Into Light', cursive;
}
.game-over{
    font-family: 'Shadows Into Light', cursive;
}

.bg-main-man{
    background-color: #141414;
    background-image: linear-gradient(180deg, #141414 0%, #3b4a89 50%, #890000 100%);
}

</style>
