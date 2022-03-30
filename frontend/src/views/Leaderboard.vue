<template>
    <navbar />
    <main class="w-full pt-8">
        <div class="flex w-full justify-around" v-for="user in leaderboard">
            <p class="text-lg font-semibold text-left">{{ user.username }}</p>
            <p class="text-lg font-semibold text-left">{{ user.leaderboard_points }}</p>
        </div>
    </main>
</template>

<script setup>
import axios from "axios";
import { onMounted, ref } from "vue";

import { baseURL } from "@/constants.js";
import Navbar from "@/components/Navbar.vue";
import BaseTable from "@/components/BaseTable.vue";

const leaderboard = ref([]);

onMounted(() => {
    axios.get(`${baseURL}/api/user/leaderboard`)
    .then(response => leaderboard.value = response.data);
})
</script>
