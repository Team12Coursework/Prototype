<template>
    <register-page-layout>
        <div class="bg-white h-full border p-5 flex flex-col space-y-4 shadow">
        <div class="mx-auto">
            <img class="logo-max-width" src='../assets/Character_Connect_Logo.jpg'>
            </div>
            <div class="justify-center flex-grow flex flex-col space-y-4">
            <h1 class="text-3xl text-gray-800 font-semibold">Register</h1>
<p class="text-xs">Already have an account?<br><a class="underline underline-offset-2 text-blue-400 hover:text-blue-600" href="/login">Log in</a></p>
            <div class="flex flex-col">
                <label class="mb-2" for="username">Username</label>
                <input type="text" name="username" class="rounded border p-2" />
            </div>

            <div class="flex flex-col">
                <label class="mb-2" for="username">Email</label>
                <input type="email" name="username" class="rounded border p-2" />
            </div>

            <div class="flex flex-col">
                <label class="mb-2" for="password">Password</label>
                <input type="password" name="password" class="rounded border p-2" />
            </div>

            <div class="flex flex-col">
                <label class="mb-2" for="password">Confirm password</label>
                <input type="password" name="password" class="rounded border p-2" />
            </div>

            <input type="submit" value="Create Account" class="cursor-pointer hover:bg-blue-700 rounded p-2 text-white bg-blue-500" />
            </div>
            <div class="flex flex-col flex-grow">
            <div class="flex-grow"></div>
            <div class="flex flex-col">
            <div class="flex justify-around mb-4">
            <a class="transform hover:scale-125 transition duration-200 ease-in-out" href="#" title="Go to our youtube">
            <img class="h-8 w-8" src='../assets/youtube.png'>
            </a>
            <a class="transform hover:scale-125 transition duration-200 ease-in-out" href="#" title="Go to our reddit">
            <img class="h-8 w-8" src='../assets/reddit.png'>
            </a>
            <a class="transform hover:scale-125 transition duration-200 ease-in-out" href="#" title="Go to our discord">
            <img class="h-8 w-8" src='../assets/discord.png'>
            </a>
            <a class="transform hover:scale-125 transition duration-200 ease-in-out" href="#" title="Go to our instagram">
            <img class="h-8 w-8" src='../assets/instagram.png'>
            </a>
            </div>
            <p class="text-xs text-center flex flex-col">
            <a class="underline underline-offset-2 text-blue-400 hover:text-blue-600" href="https://team12coursework.github.io/index.html#rules" target="_blank">Learn more</a>
            © 2021 CharacterConnect by Team 12
            </p>
            </div>
            </div>
        </div>
    </register-page-layout>
</template>

<script>
import RegisterPageLayout from "@/layouts/RegisterPageLayout.vue";

export default {
    components: {
        RegisterPageLayout,
    }
}
</script>
<style scoped>
.logo-max-width{
    max-width: 120px;
}
</style>
