<template>
    <central-floating-layout>
        <div class="bg-white rounded border p-5 flex flex-col space-y-4 shadow">
            <h1 class="text-3xl text-gray-800 font-semibold">Login</h1>

            <form @submit="handleLogin">
                <div class="flex flex-col">
                    <label for="username">USERNAME</label>
                    <input required v-model="user.username" type="text" name="username" class="rounded border p-2" />
                </div>

                <div class="flex flex-col pt-2">
                    <label for="password">PASSWORD</label>
                    <input required v-model="user.password" type="password" name="password" class="rounded border p-2" />
                </div>

                <input type="submit" value="Login" class="rounded p-2 text-white bg-blue-500 cursor-pointer" />
            </form>
        </div>
    </central-floating-layout>
</template>

<script>
import CentralFloatingLayout from "@/layouts/CentralFloatingLayout.vue";

export default {
    components: {
        CentralFloatingLayout,
    },

    data() {
        return {
            user: {
                username: "",
                password: "",
            }
        }
    },

    computed: {
        loggedIn() {
            return this.$store.state.auth.status.loggedIn;
        },
    },

    created() {
        if (this.loggedIn) {
            this.$router.push("/");
        }
    },

    methods: {
        handleLogin(e) {
            console.log("called");
            this.$store.dispatch("auth/login", this.user).then(
                () => {
                    this.$router.push("/");
                },
                () => {
                    alert("username or password incorrect");
                }
            )
            e.preventDefault();
        }
    }
}
</script>
