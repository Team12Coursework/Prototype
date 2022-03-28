<template>
    <navbar />

    <main class="p-12">
        <h1 class=" font-mono font-bold text-3xl text-gray-900 text-center mr-5">Settings</h1>
        
        <div class="mt-4 flex border-b space-x-8 text-gray-600 font-semibold">
            <p class="border-b-2 p-2 border-purple-400 text-purple-500 font-mono">General</p>
            <p class="p-2 font-mono">Password</p>
        </div>

        <div class="mt-12 w-1/2 ml-96 bg-white border-solid border-2 border-black rounded-3xl shadow-2xl">
            <h2 class="font-mono font-bold text-xl ml-5 mt-4">Profile</h2>
            <p class=" font-semibold text-gray-500 text-sm ml-5 mt-4">Do not share this information.</p>

            <div class="border-t p-4 mt-8 flex justify-between">
                <p class="font-bold text-lg text-black">Name:</p>
                <p class="text-black">{{ profileData.name }}</p>
                <p class="font-bold text-black">Update</p>
            </div>

            <div class="border-t p-4 flex justify-between items-center">
                <p class="font-bold text-lg text-black">Photo:</p>
                <p class="h-10 w-10 border rounded-full border-red-600"></p>
                <p class="font-bold text-black">Update</p>
            </div>

            <div class="border-t p-4 flex justify-between">
                <p class="font-bold text-lg text-black">Email:</p>
                <p class="text-black">{{ profileData.email }}</p>
                <p class="font-bold text-black">Update</p>
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
        