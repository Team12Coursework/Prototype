<template>
    <register-page-layout>
        <div class="bg-white h-full border p-5 flex flex-col space-y-4 shadow">
            <div class="mx-auto">
                <img class="logo-max-width" src='@/assets/images/Character_Connect_Logo.jpg'>
            </div>
            <div class="justify-center flex-grow flex flex-col space-y-4">
                <h1 class="text-3xl text-gray-800 font-semibold">Register</h1>
                <p class="text-xs">Already have an account?<br><a class="underline underline-offset-2 text-blue-400 hover:text-blue-600" href="/login">Log in</a></p>

                <div class="flex flex-col">
                    <label class="mb-2" for="username">Username</label>
                    <input v-model="username" type="text" name="username" class="rounded border p-2" />
                </div>

                <div class="flex flex-col">
                    <label class="mb-2" for="username">Email</label>
                    <input type="email" name="username" class="rounded border p-2" />
                </div>

                <div class="flex flex-col">
                    <label class="mb-2" for="password">Password</label>
                    <input v-model="password" type="password" name="password" class="rounded border p-2" />
                </div>

                <div class="flex flex-col">
                    <label class="mb-2" for="password">Confirm password</label>
                    <input type="password" name="password" class="rounded border p-2" />
                </div>

                <div v-if="password.length > 0 && passwordErrors" class="flex flex-col">
                    <p class="text-red-400">{{ passwordErrors }}</p>
                </div>
                 <div v-if="noInput == null" class="flex flex-col">
                    <p class="text-red-400">{{ noInput }}</p>
                </div>

                <button @click="handleRegister" class="cursor-pointer hover:bg-blue-700 rounded p-2 text-white bg-blue-500">Create Account</button>
            </div>

            <div class="flex flex-col flex-grow">
                <div class="flex-grow"></div>
                <div class="flex flex-col">
                    <div class="flex justify-around mb-4">
                        <a class="transform hover:scale-125 transition duration-200 ease-in-out" href="https://twitter.com/CC0nnect" title="Go to our twitter">
                            <img class="h-8 w-8" src='../assets/images/twitter.png'>
                        </a>

                        <a class="transform hover:scale-125 transition duration-200 ease-in-out" href="https://www.reddit.com/r/CharacterConnect" title="Go to our reddit">
                            <img class="h-8 w-8" src='../assets/images/reddit.png'>
                        </a>

                        <a class="transform hover:scale-125 transition duration-200 ease-in-out" href="https://discord.gg/n5w42a5thH" title="Go to our discord">
                            <img class="h-8 w-8" src='../assets/images/discord.png'>
                        </a>

                        <a class="transform hover:scale-125 transition duration-200 ease-in-out" href="https://www.instagram.com/characterconnect" title="Go to our instagram">
                            <img class="h-8 w-8" src='../assets/images/instagram.png'>
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

<script setup>
import { ref, computed } from "vue";
import { useRouter } from "vue-router";
import { useStore } from "vuex";
 
import RegisterPageLayout from "@/layouts/RegisterPageLayout.vue";

const socialMedia = [
    { name: "YouTube", url: "https://discord.gg/n5w42a5thH", link: require("@/assets/images/instagram.png") },
    { name: "Discord", link: require("@/assets/images/discord.png") },
    { name: "Reddit",  link: require("@/assets/images/reddit.png") },
    { name: "YouTube", link: require("@/assets/images/youtube.png") },
];

const MIN_LENGTH = 8;

const store = useStore();
const router = useRouter();

const username = ref("");
const password = ref("");
const email = ref("");

function handleRegister(event) {
    if (passwordErrors.value === null && noInput.value === null) {
        store.dispatch("auth/register", {username: username.value, password: password.value}).then(
            () => { router.push("/login") },
            () => { alert("Something went wrong") }
        )
    }

    event.preventDefault();
}

// password valid function, will return a String with an error message
// if there are any, otherwise return null.
//The function is used to check for password strength and helps to ensure that only a strong password has been entered to register for an account
const passwordErrors = computed(() => {
    // regex expression to monitor for capital letters
    const capitals =/[A-Z]/
    // regex expression to monitor for lower case letters
    const lower =/[a=z]/
    // regex expression to monitor for numbers
    const numbers =/[0-9]/
    // regex expression to monitor for special characters
    const specialCharacters = /[`!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?~]/;
    if (password.value.length < MIN_LENGTH) {
        return `The password must be more than ${MIN_LENGTH} characters long`
    }
    if (specialCharacters.test(password.value) === false) {
        return "There must be one or more special characters used within the password entered"
    }
    if (capitals.test(password.value) === false) {
        return "There must be at least one upper case letter used within the password entered"
    }
     if (lower.test(password.value) === false) {
        return "There must be at least one lower case letter used within the password entered"
    }
     if (numbers.test(password.value) === false) {
        return "There must be at least one number used within the password entered"
    }
    return null
})
const noInput = computed(() => {
    if (username.value === "") {
        return "You must enter a username"
    }
     if (email.value === "") {
        return "You must enter a email address"
    }
    return null
})

</script>

<style scoped>
.logo-max-width{
    max-width: 200px;
}
</style>
