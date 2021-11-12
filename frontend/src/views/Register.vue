<template>
    <central-floating-layout>
        <div class="bg-white rounded border p-5 flex flex-col space-y-4 shadow">
            <h1 class="text-3xl text-gray-800 font-semibold">Register</h1>

            <div class="flex flex-col">
                <label for="username">USERNAME</label>
                <input type="text" name="username" class="rounded border p-2" />
            </div>

            <div class="flex flex-col">
                <label for="username">EMAIL</label>
                <input type="email" name="username" class="rounded border p-2" />
            </div>

            <div class="flex space-x-2">
                <div class="flex flex-col">
                    <label for="password">PASSWORD</label>
                    <input type="password" name="password" class="rounded border p-2" />
                </div>

                <div class="flex flex-col">
                    <label for="password">CONFIRM PASSWORD</label>
                    <input type="password" name="password" class="rounded border p-2" />
                </div>
            </div>

            <input type="submit" value="Create Account" class="rounded p-2 text-white bg-blue-500" />
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
