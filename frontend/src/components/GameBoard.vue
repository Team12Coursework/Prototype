<template>
    <div class="flex space-x-2 justify-center w-full">
        <div v-for="i in 15" :key="i" class="flex flex-col space-y-2 w-full">
            <div v-for="j in 15" :key="j" class="flex bg-gray-100 w-full rounded justify-center items-center font-semibold" style="aspect-ratio: 1;">
                {{ j }}
            </div>
        </div>
    </div>
</template>

<script>
export default {
    mounted() {
        console.log("hello");
    }
}
</script>
