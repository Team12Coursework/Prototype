<template>
    <basic-layout>
        <main class="flex justify-center w-full">
            <div class="w-full max-w-7xl flex flex-col space-y-12">
                <div>
                    <h1 class="text-xl font-semibold">Leaderboard</h1>
                    <leaderboard />
                </div>
 
                <div>
                    <h1 class="text-xl font-semibold">Match History</h1>
                    <match-history />
                </div>
            </div>

        </main>
    </basic-layout>
</template>

<script>
import BasicLayout from "@/layouts/BasicLayout.vue";
import Leaderboard from "@/components/Leaderboard.vue";
import MatchHistory from "@/components/MatchHistory.vue";

export default {
    name: "Home",
    components: {
        BasicLayout,
        Leaderboard,
        MatchHistory,
    },

    computed: {
        loggedIn() {
            return this.$store.state.auth.status.loggedIn;
        }
    },

    created() {
        if (!this.loggedIn) {
            this.$router.push("/login");
        }
    },
};
</script>
