<template>
    <main class="orange-background-color flex flex-col h-screen">
        <div class="flex-grow flex">
            <div class="w-1/3 h-full">
                <slot>
                </slot>
            </div>
            <div class="bg-login flex-grow w-full">
                <div class="side-info">
                <div class="mb-8">
                CharacterConnect is a turn-based multiplayer word game inspired by Scrabble, where you can test your wits against other players by creating words to score points. Compete with friends in an interactive environement, and ascend the leaderboard. Additional game modes and features coming soon.
                </div>
                <a href="https://team12coursework.github.io/index.html#rules">Learn more</a>
                </div>
            </div>
        </div>
    </main>
</template>

<script>

export default {
    name: "LoggingPageLayout"
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
.bg-login a{
	background: white;
	color: black;
	padding: 12px;
	border-radius: 10px;
}
.side-info{
	max-width: 80%;
    font-size: 16px;
    color: white;
    padding: 2em;
    border-radius: 20px;
    background: #00000061;
    text-align: center;
    font-weight: bold;
    display: flex;
    flex-direction: column;
}
</style>