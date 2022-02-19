<template>
    <main class="flex flex-col h-screen">
        <navbar/>
                <div class="bg-main-man w-full flex flex-grow">
                <div class="w-full flex justify-around flex-col flex-grow items-center max-w-screen-md mx-auto">
                <div class="space-y-4">
                <div class="flex justify-center space-x-2 logo-container">
                    <img src="../assets/Character_Connect_Logo.jpg" />
                    <img class="hand" src="../assets/hand.png" />
                    <img class="bulb" src="../assets/bulb.png" />
                </div>
                </div>
                <div class="flex flex-col space-y-4">
                <router-link class="button" to='/gamemodes'>New Game</router-link>
                <router-link class="button" to='/gamemodes'>Join Game</router-link>
                <router-link class="button" to='/gamemodes'>Leaderboard</router-link>
                </div>
                </div>
                <img class="bag" src="../assets/letterBag.png" />
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
.button {
    @apply border-4 text-black border-black text-2xl w-full text-center rounded-full font-bold py-4 px-16 bg-white hover:bg-black hover:text-white duration-200
}
.bg-main-man{
	background: url("../assets/menu.png");
	background-size: cover;
}
.logo-container{
	position: relative;
}
.logo-container .hand{
	position: absolute;
	left: -268px;
	transition: 0.3s all;
}

.logo-container .hand:hover{
	transform: rotate(10deg);
}

.logo-container .bulb{
	position: absolute;
	right: -134px;
    height: 100%;
    transition: 0.3s all;
}

.logo-container .bulb:hover{
	transform: scale(1.1);
}

.bag{
	position: fixed;
	left: -10px;
    bottom: -200px;
}
</style>
