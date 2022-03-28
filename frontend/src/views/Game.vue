<template>
        <navbar />

        <main class="w-full flex flex-col items-center min-h-screen p-6 space-y-4 bg-cover" :style="{'background-image': 'url(' + backgroundImage(this.$store.getters.getGameNum) + ')'}">
            <div class="max-w-screen-2xl space-y-4 w-full flex flex-col">
                <scoreboard v-if="players.length === 2" :players="players" />

                <div class="w-full flex h-full justify-center space-x-4">
                    <div class="w-full flex flex-col space-y-4">
                        <div class="w-full space-x-2 flex p-4 rounded" style="background: rgb(255,233,190); background: linear-gradient(0deg, rgba(255,233,190,1) 0%, rgba(236,198,126,1) 25%, rgba(237,200,130,1) 75%, rgba(255,233,190,1) 100%);">
                            <div class="space-y-2 w-full flex flex-col" v-for ="i in 15" :key ="i">
                                <board-square class="w-full p-1 flex items-center justify-center" :style="tileColour(squareId(i, j))" v-for ="j in 15" :key ="j" :id="squareId(i, j)" />
                            </div>
                        </div>

                        <div class="w-full p-2 bg-blue-200 shadow-inner rounded h-24 flex space-x-2">
                            <card v-for="(tile, i) in tiles" :key="tile" :letter="tile" :id="i" :draggable="true"/>
                        </div>

                        <div class="border-4 mt-3 w-full">
                            <div class="border-2 m-2 float-left p-4 text-center">
                                <button class="text-center p-2"><img class="w-32" src="../assets/img/one_tile.jpg"></button>
                                <p class="font-bold">One Random Letter (2 Points)</p>
                            </div>
                             <div class="border-2 m-2 float-left p-4 text-center">
                                <button class="text-center p-2"><img class="w-32" src="../assets/img/change_bag.jpg"></button>
                                <p class="font-bold">Change Bag (3 Points)</p>
                            </div>
                             <div class="border-2 m-2 float-left p-4 text-center">
                                <button class="text-center p-2"><img class="w-32" src="../assets/img/two_tiles.jpg"></button>
                                <p class="font-bold">Two Random Letters (4 Points)</p>
                            </div>
                        </div> 

                    </div>

                    <div class="w-1/2 flex flex-col">
                        <chatbox :messages="chatMessages" @update:messages="this.sendChatMessage($event)" />

                        <div v-if="piecePlaced" class="flex space-x-2 w-full">
                            <button @click="resetBoard" class="cursor-pointer p-2 bg-blue-500 w-full rounded text-white">Reset</button>
                            <button @click="nextTurn" class="cursor-pointer p-2 bg-blue-500 w-full rounded text-white">Next Turn</button>
                        </div>
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
    },

    methods: {
        backgroundImage(number) {
      let num = number;
      if (num == 1) {
        return require("../assets/img/general_page.jpg");
      }
      else if (num == 2) {
        return require("../assets/img/maths_page.jpg");
      }
      else if (num == 3) {
        return require("../assets/img/science_page.jpg");
      } 
      else if (num == 4) {
          return require("../assets/img/custom_page.jpg");
      }
    },

        squareId(x, y) {
            return `${(x-1).toString()},${(y-1).toString()}`
        },

        tileColour(squareId) {
            const RED_TILES = new Set([ "0,0", "0,7", "7,14", "14,7", "14,14", "0,14", "14,0", "7,0", "7,7"]);
            const BLUE_TILES = new Set([
                "11,0", "3,0", "7,3", "8,2", "9,1", "6,2", "5,1", // top side
                "0,11", "0,3", "3,7", "2,8", "1,9", "2,6", "1,5", // left side
                "11,14", "3,14", "7,11", "8,12", "9,13", "6,12", "5,13", // bottom side
                "14,11", "14,3", "11,7", "12,8", "13,9", "12,6", "13,5", // left side
            ]);

            // check if square is one of the predefined red tiles
            if (RED_TILES.has(squareId)) {
                return "background-color: rgba(248, 113, 113, 1)";
            }

            // check if square is one of the squares surrounding the red tiles
            // on the edge of the board.
            if (BLUE_TILES.has(squareId)) {
                return "background-color: rgba(96, 165, 250, 0.3)";
            }

            let idx = squareId.split(",");
            let x = parseInt(idx[0]);
            let y = parseInt(idx[1]);

            // check if square is on the diagonal
            if (x === y || x === 14 - y) {
                // check if diagonals are within 3 tiles of the center
                if (Math.abs(x-7) < 3 && Math.abs(y-7) < 3)
                    return "background-color: rgba(96, 165, 250, 0.3)";
                else
                    return "background-color: rgba(248, 113, 113, 0.3)";
            }


            return "background: rgba(243, 244, 246, 0.5)";
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
