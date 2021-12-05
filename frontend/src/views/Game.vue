<template>
        <navbar />

        <main class="w-full flex flex-col min-h-screen h-screen p-6 space-y-4">
            <scoreboard />
            <div class="w-full flex h-full space-x-4">
                <div class="w-full flex flex-col space-y-4">
                    <div class="w-full h-full space-x-2 flex">
                        <div class="space-y-2 w-full h-full flex flex-col" v-for ="i in 15" :key ="i">
                            <board class="bg-gray-300 w-full min-h-24 h-full p-1 flex items-center justify-center" v-for ="j in 15" :key ="j" :id="loc(j, i)" />
                        </div>
                    </div>

                    <board v-if="letters" class="w-full p-2 bg-gray-300 h-32 flex space-x-2" :id="0">
                        <card v-for="i in 7" :key="i" :id="i" :letter="letters[i-1]" :draggable="true"/>
                    </board>
                </div>

                <div class="w-full flex flex-col">
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
import Board from '@/components/Board.vue'
import Card from '@/components/Card.vue'
import Navbar from '@/components/Navbar.vue'
import Chatbox from '@/components/Chatbox.vue'
import Scoreboard from '@/components/Scoreboard.vue'

const alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

export default{
    name: "Game",

    data() {
        return {
            alphabet,
            maxId: 0,
            letters: [],
            chatMessages: [],
            player: {
                name: "HarryLees",
            },
            socket: null,
        }
    },

    components:{
        Board,
        Card,
        Navbar,
        Chatbox,
        Scoreboard,
    },

    methods: {
        loc(x, y) {
            // method to return the square ID given the x, y position on the board
            return 15 * x + y
        },

        resetBoard() {
            this.$store.dispatch("resetBoard");
        },

        nextTurn() {
            this.$store.dispatch("nextTurn");
            this.generatePieces();
        },

        generatePieces() {
            let letters = [];
            for (let i=0; i<7; i++) {
                let letter = this.alphabet[Math.floor(Math.random() * 26)];
                letters.push(letter);
                this.maxId += 1;
            }
            this.letters = letters;
        },

        sendChatMessage(message) {
            this.socket.send(JSON.stringify({type: "message", message: message, fromUser: this.user, sentAt: new Date().toLocaleTimeString('en-GB') }));
        },

        receiveChatMessage(message) {
            this.chatMessages.push(message);
        },

        processMessage(data) {
            if (data.type === "playerJoin" && data.player.name !== this.player.name) {
                this.receiveChatMessage(data);
            }

            if (data.type === "message") {
                this.receiveChatMessage(data);
            }

            if (data.type === "playerLeft") {
                this.receiveChatMessage(data);
            }
        },
    },

    computed: {
        boardArray() {
            return this.$store.state.board;
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

    created() {
        this.generatePieces();
    },

    mounted() {
        this.socket = new WebSocket(`ws://localhost:8000/api/game/ws/${this.$route.game_id}`);
        console.log('user:', this.user);
        this.socket.addEventListener("open", () => {
            this.socket.send(JSON.stringify({
                type: "playerJoin",
                player: {
                    name: this.user,
                },
                sentAt: new Date().toLocaleTimeString('en-GB'),
            }))
            console.log("joined room");
        })

        this.socket.addEventListener("message", (event) => {
            this.processMessage(JSON.parse(event.data));
        })
    },
}
</script>
