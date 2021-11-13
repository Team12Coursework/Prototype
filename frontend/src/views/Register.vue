<template>
    <central-floating-layout>
        <div class="bg-white rounded border p-5 flex flex-col space-y-4 shadow">
            <h1 class="text-3xl text-gray-800 font-semibold">Register</h1>

            <form @submit="handleRegister">
                <div class="flex flex-col">
                    <label for="username">USERNAME</label>
                    <input required v-model="user.username" type="text" name="username" class="rounded border p-2" />
                </div>

                <div class="flex space-x-2">
                    <div class="flex flex-col">
                        <label for="password">PASSWORD</label>
                        <input required v-model="user.password" type="password" name="password" class="rounded border p-2" />
                    </div>

                    <div class="flex flex-col">
                        <label for="password">CONFIRM PASSWORD</label>
                        <input type="password" name="password" class="rounded border p-2" />
                    </div>
                </div>

                <input type="submit" value="Create Account" class="rounded p-2 text-white bg-blue-500" />
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

    mounted() {
        if (this.loggedIn) {
            this.$router.push("/");
        }
    },

    methods: {
        handleRegister(e) {
            e.preventDefault();
            this.$store.dispatch("auth/register", this.user).then(
                () => {
                    this.$router.push("/login");
                },
                () => {
                    alert("something went wrong");
                },
            );
        }
    }
}
</script>
