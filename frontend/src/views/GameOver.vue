<template>
    <main class="flex flex-col h-screen">
        <navbar/>

        <div class="bg-main-man w-full flex flex-grow">
            <div class="w-full flex justify-around flex-col flex-grow items-center max-w-screen-md mx-auto">
                <div class="space-y-4">
                    <p class="text-8xl font-bold game-over font-effect-anaglyph">{{ won ? "YOU WON" : "YOU LOST" }}</p>
                </div>

                <div class="flex flex-col space-y-4">
                    <router-link class="button bg-blue-400" to='/gamemodes'>PLAY AGAIN</router-link>
                    <router-link class="button bg-green-400" to='/leaderboard'>LEADERBOARD</router-link>
                    <router-link class="button bg-red-400" to='/'>RETURN TO MAIN MENU</router-link>
                </div>
            </div>
        </div>
    </main>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { useRoute } from "vue-router";
import Navbar from "@/components/Navbar.vue";

const route = useRoute();
const won = ref(false);

onMounted(() => {
    won.value = route.params.won;
});
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
    background-image: url(../assets/images/bg-go-3.jpg);
    background-size: cover;
}

</style>
