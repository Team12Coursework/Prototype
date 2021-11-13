<template>
    <div class='h-12 w-12 rounded text-white flex justify-center font-bold items-center' :style="{background: color}">
        <p><slot></slot></p>
    </div>
</template>

<script>

export default {
    name: 'Tile',
    props: {
	color: String
	},
    data() {
         return {
    isMultiply: true,
    }

    },
}

</script>