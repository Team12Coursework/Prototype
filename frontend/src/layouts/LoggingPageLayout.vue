<template>
    <main class="orange-background-color flex flex-col h-screen">
        <navbar-logging />

        <div class="flex flex-col justify-center items-center flex-grow">
            <slot>
            </slot>
        </div>
    </main>
</template>

<script>
import NavbarLogging from "@/components/NavbarLogging.vue";

export default {
    name: "LoggingPageLayout",
    components: { NavbarLogging },
}
</script>