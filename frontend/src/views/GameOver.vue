<template>
    <navbar/>

    <main class="flex justify-center w-full">
        <div class="w-full max-w-7xl flex flex-col space-y-12">
            <div>
                <h1 class="text-xl">Game Over</h1>
            </div>

            <router-link to='/gamemodes'>Play Again</router-link>
            <router-link to='/leaderboard'>Leader board</router-link>
            <router-link to='/'> Return To Main Menu</router-link>
        </div>
    </main>
</template>

<script>
    import Navbar from "@/components/Navbar.vue"

    export default{
        components: {
            Navbar,
        }
    }

</script>

<style scoped>
</style>
