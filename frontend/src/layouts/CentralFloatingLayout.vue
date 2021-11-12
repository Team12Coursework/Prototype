<template>
    <main class="flex flex-col h-screen">
        <navbar />

        <div class="flex flex-col justify-center items-center flex-grow">
            <slot>
            </slot>
        </div>
    </main>
</template>

<script>
import Navbar from "@/components/Navbar.vue";

export default {
    name: "CentralFloatingLayout",
    components: { Navbar },
}
</script>