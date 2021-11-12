<template>
    <router-link :to="to">
        <div class="pl-5 p-2 hover:bg-blue-500 hover:text-white rounded-xl flex justify-start space-x-6 items-center">
            <slot></slot>
        </div>
    </router-link>
</template>

<script>
export default {
    props: {
        to: {
            type: String,
            required: false,
        }
    }
}
</script>
