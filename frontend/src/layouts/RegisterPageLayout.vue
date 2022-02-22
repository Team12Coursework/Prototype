<template>
    <main class="orange-background-color flex flex-col h-screen">
        <div class="flex-grow flex">
            <div class="w-1/3 h-full">
                <slot>
                </slot>
            </div>
            <div class="bg-login flex-grow w-full">
                
            </div>
        </div>
    </main>
</template>

<script>

export default {
    name: "RegisterPageLayout"
}
</script>

<style scoped>
.orange-background-color{
	background: #EE6352;
}
.bg-login{
	background: url("https://images.unsplash.com/photo-1576502200272-341a4b8d5ebb?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=870&q=80");
    background-repeat: no-repeat;
    background-size: cover;
    display: flex;
    justify-content: center;
    align-items: center;
}
</style>