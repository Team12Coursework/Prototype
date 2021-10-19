<template>
    <central-floating-layout>
        <div class="flex">
            <h1 class="text-7xl font-bold text-blue-700 border-r p-4">404</h1>
            
            <div class="p-4 space-y-2">
                <h1 class="text-6xl font-bold text-gray-900">Page Not Found</h1>
                <p class="text-gray-700">Please check the URL in the address bar and try again.</p>
            </div>
        </div>
    </central-floating-layout>
</template>

<script>
import CentralFloatingLayout from "@/layouts/CentralFloatingLayout.vue";

export default {
    components: {
        CentralFloatingLayout,
    }
}
</script>
