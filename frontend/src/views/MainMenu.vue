<template>
    <main class="flex flex-col h-screen">
        <navbar/>
                <div class="bg-main-man w-full flex flex-grow">
                <div class="w-full flex justify-around flex-col flex-grow items-center max-w-screen-md mx-auto">
                <div class="space-y-4">
                <div class="flex justify-center space-x-2 logo-container">
                    <img class="logo" src="../assets/Character_Connect_Logo.jpg" />
                    <img class="hand" src="../assets/hand.png" />
                    <img class="bulb" src="../assets/bulb.png" />
                </div>
                </div>
                <div class="flex flex-col space-y-4">
                <router-link class="button" to='/gamemodes'>NEW GAME</router-link>
                <router-link class="button" to='/gamemodes'>JOIN GAME</router-link>
                <router-link class="button" to='/gamemodes'>LEADERBOARD</router-link>
                </div>
                </div>
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
@import url('https://fonts.googleapis.com/css2?family=Shadows+Into+Light&effect=anaglyph');
.button {
    @apply text-white text-2xl w-full text-center rounded-full font-bold py-4 px-16 hover:bg-black hover:text-white duration-200
}
.button{
	background-color:#4a4a4a47;
	font-family: 'Shadows Into Light', cursive;
}
.bg-main-man{
	background: url("../assets/menu-new.png");
	background-size: cover;
	background-position: bottom;
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
