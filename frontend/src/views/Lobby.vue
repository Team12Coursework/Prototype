<template>
    <navbar/>

    <main class="flex justify-center w-full">
        <div class="w-full max-w-7xl flex flex-col space-y-12 items-center">
            <div class="flex flex-col items-center pt-6">
                <h1 class="text-6xl font-bold">Lobby</h1>

                <p class="mt-4">Invite Friends with the link below</p>
                <p class="rounded border mt-4 px-4 py-2">localhost:8080{{ link.href }}</p>

                <router-link class="rounded p-2 bg-green-400" :to="link">Go</router-link>
            </div>
        </div>
    </main>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { useRouter } from "vue-router";

import Navbar from "@/components/Navbar.vue";

const link = ref("");
const router = useRouter()

onMounted(() => {
    let epoch_time = Date.now();
    link.value = router.resolve({
        name: "Play",
        params: {
            game_id: epoch_time
        }
    });
});
</script>
