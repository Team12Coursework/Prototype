<template>
    <div class="w-full flex rounded justify-center bg-gray-200 p-4">
        <div class="w-1/2 flex justify-around max-w-xl">
            <p class="font-bold text-6xl">{{ playerOne }}</p>
            <p class="font-bold text-6xl">-</p>
            <p class="font-bold text-6xl">{{ playerTwo}}</p>
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            playerOne: 0,
            playerTwo: 0,
        }
    }
}
</script>
