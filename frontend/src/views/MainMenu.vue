<template>
    <main class="flex flex-col h-screen">
        <navbar/>

        <div class="bg-main-man w-full flex flex-grow">
            <div class="w-full flex justify-around flex-col flex-grow items-center max-w-screen-md mx-auto">
                <div class="space-y-4">
                    <div class="flex justify-center space-x-2 logo-container">
                        <img class="logo" src="../assets/images/Character_Connect_Logo.jpg" />
                        <img class="hand" src="../assets/images/hand.png" />
                        <img class="bulb" src="../assets/images/bulb.png" />
                    </div>
                </div>

                <div class="flex flex-col space-y-4">
                    <router-link class="button bg-blue-400" to='/gamemodes'><img class="feature-for-kids" src="../assets/images/happy.gif" />NEW GAME</router-link>
                    <router-link class="button bg-red-400" to='/leaderboard'><img class="feature-for-kids" src="../assets/images/happy.gif" />LEADERBOARD</router-link>
                </div>
            </div>
        </div>
    </main>
</template>

<script setup>
import Navbar from "@/components/Navbar.vue"
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Shadows+Into+Light&effect=anaglyph');
.button {
    @apply text-white text-2xl w-full text-center rounded-full font-bold py-4 px-16 hover:bg-black hover:text-white duration-200
}
.button{
	font-family: 'Shadows Into Light', cursive;
	position: relative;
}
.button:hover .feature-for-kids{
	right: -50px;
	height: 100px;
	z-index: 1;
}
.bg-main-man{
	background: url("../assets/images/new-menu-clean.png");
	background-size: cover;
	background-position: bottom;
}
.feature-for-kids{
	position: absolute;
	bottom: 0;
	right: 0;
	height: 0;
	width: auto;
	z-index: -1;
	transition: 0.3s all;
}
.logo-container{
	position: relative;
}
.logo-container .logo{
	max-width: 300px;
}
.logo-container .hand{
	position: absolute;
	max-width: 150px;
	left: -120px;
	transition: 0.3s all;
}

.logo-container .hand:hover{
	transform: rotate(10deg);
}

.logo-container .bulb{
	position: absolute;
	right: -55px;
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
