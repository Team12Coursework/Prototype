<template>
    <navbar/>

    <main class="flex justify-center w-full">
        <div class="w-full max-w-7xl flex flex-col space-y-12">
            <div>
                <h1 class="text-xl">Select A Game Mode</h1>
            </div>
            <button>
                <my-button to="/play">General</my-button>
                <my-button to="">Mathematics (LOCKED)</my-button>
                <my-button to="">Science (LOCKED)</my-button>
                <my-button to="">Custom (LOCKED)</my-button>

            </button>

            <go-back/>
            
                    
        </div>
    </main>
    
</template>


<script>
    import Navbar from '@/components/Navbar.vue'
    import MyButton from '../components/MyButton.vue'
    import GoBack from '../components/GoBack.vue'

    export default{
        components:{
            Navbar,
            MyButton,
            GoBack,        
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