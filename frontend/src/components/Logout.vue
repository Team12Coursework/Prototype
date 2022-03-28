<template>
    Logging out, please wait...
</template>

<script setup>
import { onMounted } from "vue";
import { useRouter } from "vue-router";
import { useStore } from "vuex";

const router = useRouter();
const store = useStore();

onMounted(() => {
    store.dispatch("auth/logout")
    .then(
        () => { router.push({ name: "Login" }) }
    );
})
</script>