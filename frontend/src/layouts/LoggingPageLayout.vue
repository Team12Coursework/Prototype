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
    name: "LoggingPageLayout"
}
</script>