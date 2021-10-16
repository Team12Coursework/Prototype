<template>
    <div class='flex flex-col items-center justify-center'>
        <div>
            <div class='flex justify-center items-center space-x-2 font-bold text-2xl text-gray-600 mb-6'>
                <div v-for="(row, i) in board" :key='row' class='space-y-2'>
                    <div v-for="(cell, j) in row" :key='cell'>
                        <div id='cell' @click='selected = 9 * i + j' class='bg-gray-100 rounded-md flex justify-center items-center w-16 h-16 cursor-pointer' v-bind:class='{ "bg-blue-400 text-white": (9 * i + j) == selected }'>
                            <span>0</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        data() {
            return {
                board: Array(10).fill(0).map(() => Array(10).fill(0)),
            }
        },
    }
</script>