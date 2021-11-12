<template>
    <navbar/>
    <main class="flex justify-center w-full">
        <div class="w-full max-w-7xl flex flex-col space-y-12">
            <div>
                <h1 class="text-xl">Welcome To Character Connect</h1>
            </div>
            <button>
                <my-button to='/gamemodes'>Game Modes</my-button>
                <my-button to='/leaderboard'>Leader board</my-button>
            </button>
                    
        </div>
    </main>

</template>



<script>
    import Navbar from "@/components/Navbar.vue"
    import MyButton from '../components/MyButton.vue'

    export default{
        components: {
            Navbar,
            MyButton,
        }
    }

</script>


<style scoped>
    h1{
        
        text-align: center;
        font-size: 55px;
        font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
    }

    main{
        padding: 50px;        
    }

</style>


