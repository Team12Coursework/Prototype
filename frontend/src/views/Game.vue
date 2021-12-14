<template>
        <navbar />
        <waiting-modal v-if="players.length < 2" />

        <main class="w-full flex flex-col min-h-screen h-screen p-6 space-y-4 bg-gray-100">
            <scoreboard v-if="players.length === 2" :players="players" />

            <div class="w-full flex h-full space-x-4">
                <div class="w-full flex flex-col space-y-4">
                    <div class="w-full h-full space-x-2 flex p-4 rounded" style="background: rgb(255,233,190); background: linear-gradient(0deg, rgba(255,233,190,1) 0%, rgba(236,198,126,1) 25%, rgba(237,200,130,1) 75%, rgba(255,233,190,1) 100%);">
                        <div class="space-y-2 w-full h-full flex flex-col" v-for ="i in 15" :key ="i">
                            <board-square class="w-full min-h-24 h-full p-1 flex items-center justify-center" style="background: rgba(243, 244, 246, 0.5)" v-for ="j in 15" :key ="j" :id="squareId(i, j)" />
                        </div>
                    </div>

                    <div class="w-full p-2 bg-green-600 shadow-inner rounded h-32 flex space-x-2">
                        <card v-for="(tile, i) in tiles" :key="tile" :letter="tile" :id="i" :draggable="true"/>
                    </div>
                </div>

                <div class="w-1/2 flex flex-col">
                    <chatbox :messages="chatMessages" @update:messages="this.sendChatMessage($event)" />

                    <div v-if="piecePlaced" class="flex space-x-2">
                        <button @click="resetBoard" class="cursor-pointer p-2 bg-blue-500 rounded text-white">Reset</button>
                        <button @click="nextTurn" class="cursor-pointer p-2 bg-blue-500 rounded text-white">Next Turn</button>
                    </div>
                </div>
            </div>
        </main>
</template>

<script>
import BoardSquare from '@/components/BoardSquare.vue'
import Card from '@/components/Card.vue'
import Navbar from '@/components/Navbar.vue'
import Chatbox from '@/components/Chatbox.vue'
import Scoreboard from '@/components/Scoreboard.vue'
import WaitingModal from '@/components/WaitingModal.vue'

export default{
    name: "Game",

    data() {
        return {
            chatMessages: [],
            socket: null,
            gameData: null,
            placed: false,
            localBoard: null,
        }
    },

    components:{
        BoardSquare,
        Card,
        Navbar,
        Chatbox,
        Scoreboard,
        WaitingModal,
    },

    methods: {
        squareId(x, y) {
            return `${(x-1).toString()},${(y-1).toString()}`
        },

        resetBoard() {
            this.$store.commit("board/updateBoard", JSON.parse(JSON.stringify(this.gameData.board)));
        },

        updateError(data) {
            alert(data.message);
            this.resetBoard();
        },

        updateGame(data) {
            this.gameData = data;
            this.resetBoard();
        },

        nextTurn() {
            this.socket.send(JSON.stringify({
                type: "gameUpdate",
                board: this.$store.state.board.board,
            }))
        },

        sendChatMessage(message) {
            this.socket.send(JSON.stringify({type: "message", message: message, fromUser: this.user, sentAt: new Date().toLocaleTimeString('en-GB') }));
        },

        receiveChatMessage(message) {
            this.chatMessages.push(message);
        },
    },

    computed: {
        storeData() {
            return this.$store.state.board;
        },

        tiles() {
            if (this.gameData === null)
                return [];

            for (let player of this.gameData.players)
                if (player.name == this.user)
                    return player.tiles;
            return [];
        },

        players() {
            if (this.gameData == null)
                return [];
            return this.gameData.players;
        },

        piecePlaced() {
            return this.$store.state.board.placed;
        },

        user() {
            // function to decode the JWT token given to the client at login.
            // this function will decode the JWT and extract the username which will be used to play the game.

            var base64Url = this.$store.state.auth.user.accessToken.split('.')[1];
            var base64 = base64Url.replace(/-/g, '+').replace(/_/g, '/');
            var jsonPayload = decodeURIComponent(atob(base64).split('').map(function(c) {
                return '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2);
            }).join(''));

            return JSON.parse(jsonPayload).sub;
        },
    },

    mounted() {
        this.socket = new WebSocket(`ws://localhost:8000/api/game/ws/${this.$route.params.game_id}`);

        this.socket.addEventListener("open", () => {
            this.socket.send(JSON.stringify({
                type: "playerJoin",
                player: this.user,
            }))
        })

        this.socket.addEventListener("message", (event) => {
            let data = JSON.parse(event.data);
            switch(data.type) {
                case "gameUpdate":
                    this.updateGame(data);
                    break;
                case "message":
                    this.receiveChatMessage(data);
                    break;
                case "updateError":
                    this.updateError(data);
                    break;
            }
        })
    },
}
</script>
