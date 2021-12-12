<template>
    <div class="w-full flex rounded justify-center bg-gray-200 p-4">
        <div class="w-1/2 flex justify-around max-w-xl">
            <div class="flex flex-col items-center">
                <p class="text-xl">{{ players[0].name }}</p>
                <p class="font-bold text-6xl">{{ players[0].points }}</p>
            </div>
            <p class="font-bold text-6xl">-</p>
            <div class="flex flex-col items-center">
                <p class="text-xl">{{ players[1].name }}</p>
                <p class="font-bold text-6xl">{{ players[1].points }}</p>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    props: {
        players: Array,
    }
}
</script>
