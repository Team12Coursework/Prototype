<template>
    <main class="flex flex-col h-screen">
        <navbar/>

        <div class="bg-main-man w-full flex flex-grow">
            <div class="w-full flex justify-around flex-col flex-grow items-center max-w-screen-md mx-auto">
            <div class="space-y-4">
            <div class="text-center text-6xl font-bold game-over font-effect-anaglyph text-black">
                SELECT A GAME MODE
            </div>

            </div>
                <div class="flex flex-col space-y-4">
                    <router-link class="button general" to="/lobby"><img class="feature-for-kids" src="@/assets/images/happy.gif" />GENERAL</router-link>
                    <router-link class="button cursor-not-allowed math" to=""><img class="feature-for-kids" src="@/assets/images/mathematics.png" />MATHEMATICS (LOCKED)</router-link>
                    <router-link class="button cursor-not-allowed science" to=""><img class="feature-for-kids" src="@/assets/images/science.png" />SCIENCE (LOCKED)</router-link>
                    <router-link class="button cursor-not-allowed custom" to=""><img class="feature-for-kids" src="@/assets/images/happy.gif" />CUSTOM (LOCKED)</router-link>
                </div>
            </div>

            <go-back class="return-button mt-2" />
        </div>
    </main>
</template>

<script setup>
import Navbar from "@/components/Navbar.vue"
import GoBack from "@/components/GoBack.vue"
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Shadows+Into+Light&effect=anaglyph');

.button {
    @apply text-white text-2xl w-full text-center rounded-full font-bold py-4 px-16 hover:text-white duration-200
}
.button{
    font-family: 'Shadows Into Light', cursive;
    position: relative;
    background-size: cover!important;
    background-repeat: no-repeat!important;
}

.button:hover .feature-for-kids{
    right: -50px;
    height: 80px;
    z-index: 1;
}

.button.math{
    background:url('../assets/images/maths_page.jpg');
}

.button.science{
    background:url('../assets/images/science_page.jpg');
}

.button.custom{
    background:url('../assets/images/pattern-colors.jpg');
}

.button.general{
    background: #D44D5C;
    color: white;
}

.game-over{
    font-family: 'Shadows Into Light', cursive;
}

.bg-main-man{
    background-color: #141414;
    background-image: url(../assets/images/bg-go-3.jpg);
    background-size: cover;
    position: relative;
}

.return-button{
    position: absolute;
    bottom: 20px;
    left: 20px;
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
</style>
