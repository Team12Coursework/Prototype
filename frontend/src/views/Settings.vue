<template>
    <navbar />

    <main class="p-12">
        <h1 class="font-bold text-3xl text-gray-900">Settings</h1>

        <div class="mt-4 flex border-b space-x-8 text-gray-600 font-semibold">
            <p class="border-b-2 p-2 border-purple-400 text-purple-500">General</p>
            <p class="p-2">Password</p>
        </div>

        <div class="mt-4">
            <h2 class="font-semibold text-xl">Profile</h2>
            <p class="text-gray-500 text-sm">This information will be publicly available, so be careful what you share.</p>

            <div class="border-t p-4 mt-4 flex justify-between">
                <p class="font-semibold text-gray-600">Name</p>
                <p>{{ profileData.name }}</p>
                <p class="font-semibold text-purple-600">Update</p>
            </div>

            <div class="border-t p-4 flex justify-between items-center">
                <p class="font-semibold text-gray-600">Photo</p>
                <p class="h-10 w-10 border rounded-full"></p>
                <p class="font-semibold text-purple-600">Update</p>
            </div>

            <div class="border-t p-4 flex justify-between">
                <p class="font-semibold text-gray-600">Email</p>
                <p>{{ profileData.email }}</p>
                <p class="font-semibold text-purple-600">Update</p>
            </div>
        </div>
    </main>
</template>

<script>
import Navbar from "@/components/Navbar.vue";

export default {
    name: "Home",
    components: {
        Navbar
    },

    data() {
        return {
            profileData: {
                name: "Harry Lees",
                email: "harry.lees@gmail.com",
                profilePicture: "",
            }
        };
    },
};
</script>