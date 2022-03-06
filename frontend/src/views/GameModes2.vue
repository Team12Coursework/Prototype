<template>
    <main class="flex flex-col h-screen">
        <navbar/>
        <div class="bg-main-man w-full flex flex-grow">
                <div class="w-full flex justify-around flex-col flex-grow items-center max-w-screen-md mx-auto">
                <div class="space-y-4">
                <div class="text-center text-4xl font-bold game-over font-effect-anaglyph text-black">
                    SELECT A GAME MODE
                </div>
                </div>
                    <div class="flex flex-col space-y-4">
                        <router-link class="button" to="/lobby">GENERAL</router-link>
                <router-link class="button cursor-not-allowed" to="">MATHEMATICS (LOCKED)</router-link>
                <router-link class="button cursor-not-allowed" to="">SCIENCE (LOCKED)</router-link>
                <router-link class="button cursor-not-allowed" to="">CUSTOM (LOCKED)</router-link>
                    </div>
                </div>

                <go-back class="mt-2" />
        </div>
    </main>
</template>

<script>
    import Navbar from "@/components/Navbar.vue"
    import GoBack from '@/components/GoBack.vue'

    export default{
        components: {
            Navbar,
            GoBack
        }
    }

</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Shadows+Into+Light&effect=anaglyph');
.button {
    @apply text-white text-2xl w-full text-center rounded-full font-bold py-4 px-16 hover:bg-black hover:text-white duration-200
}
.button{
    font-family: 'Shadows Into Light', cursive;
}
.game-over{
    font-family: 'Shadows Into Light', cursive;
}

.bg-main-man{
    background-color: #141414;
    background-image: url(../assets/bg-go-3.jpg);
    background-size: cover;
}

</style>
