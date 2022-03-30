<template>
    <main class="flex flex-col h-screen">
        <navbar/>

        <div class="w-full grow flex flex-col items-center justify-center">
            <div class="w-full max-w-screen-md flex flex-col items-center space-y-4">
                <div>
                    <h1 class="mt-4 text-3xl font-semibold">Invite Friends with the link below</h1>
                    <p class="text-sm italic text-gray-500">Please copy this link into the navigation bar on your browser to join the game</p>
                </div>
                <p class="rounded border mt-4 px-4 py-2 text-center">http://{{ windowLoc }}{{ link.href }}</p>
            </div>
        </div>
    </main>
</template>

<script setup>
import { ref, onMounted, computed } from "vue";
import { useRouter } from "vue-router";

import Navbar from "@/components/Navbar.vue";

const link = ref("");
const router = useRouter()

const windowLoc = computed(() => window.location.host);

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
