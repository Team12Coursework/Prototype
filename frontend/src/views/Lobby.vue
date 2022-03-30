<template>
    <navbar/>
    <main class=" bg-Lobby flex justify-center w-full h-screen">
        <div class="w-full max-w-7xl flex flex-col space-y-12 items-center">
            <div class="flex flex-col items-center pt-6 mt-32 rounded-2xl p-5 shadow-2xl bg-gray-100">
                <h1 class="text-6xl font-bold font-serif text-grad  text-black">Lobby</h1>

                <p class="mt-6 text-center underline italic subpixel-antialiased text-red-600">Invite friends by using the link below!</p>
                <p class=" bg-gray-700 rounded border mt-4 px-4 py-2 text-white">localhost:8080{{ link.href }}</p>

                <router-link class="rounded p-2 bg-green-400  m-3 w-1/6 text-center transform hover:scale-125" :to="link">GO</router-link>
            </div>
        </div>
    </main>
</template>

<script>
import { ref, onMounted } from "vue";
import { useRouter } from "vue-router";
import Navbar from "@/components/Navbar.vue";

export default {
    components: {
        Navbar,
    },

    setup() {
        const link = ref("");
        const getLink = () => {
            let epoch_time = Date.now();
            const router = useRouter()
            link.value = router.resolve({name: 'Play', params: {game_id: epoch_time}});
        }

        onMounted(getLink);

        return { link }
    },
}
</script>

<style scoped>
.bg-Lobby{
    background: url("../assets/images/roadToLobby.jpg");
    background-size: cover;
    background-position: center;
}
</style>
