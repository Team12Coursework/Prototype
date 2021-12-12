import { createRouter, createWebHistory } from 'vue-router'
import MainMenu from '../views/MainMenu.vue'
import store from '../store/index.js'

const routes = [
    {
        path: '/',
        name: 'MainMenu',
        component: MainMenu
    },
    {
        path: "/play/:game_id",
        name: "Play",
        component: () => import("@/views/Game.vue"),
    },
    {
        path: "/settings",
        name: "Settings",
        component: () => import("@/views/Settings.vue"),
    },
    {
        path: "/login",
        name: "Login",
        component: () => import("@/views/Login.vue"),
    },
    {
        path: "/register",
        name: "Register",
        component: () => import("@/views/Register.vue"),
    },
    {
        path: "/lobby",
        name: "Lobby",
        component: () => import("@/views/Lobby.vue"),
    },
    {
        path: "/gamemodes",
        name: "GameModes",
        component: () => import("@/views/GameModes.vue"),

    },
    {
        path: "/gameover",
        name: "GameOver",
        component: () => import("@/views/GameOver.vue"),
    },
    {
        path: '/:catchAll(.*)', // catch-all route used to display a 404 page to any invalid pages
        component: () => import("@/views/404NotFound.vue"),
    },
]

const router = createRouter({
    // router history mode allows using the back button on the browser to visit the previous page
    history: createWebHistory(process.env.BASE_URL),
    routes
})

router.beforeEach((to, from, next) => {
    const loggedIn = store.state.auth.status.loggedIn;
    console.log((to.name !== 'Login' || to.name !== 'Register') && !loggedIn);
    if (to.name === 'Login') {
        next()
    } else if (to.name === 'Register') {
        next()
    } else if (!loggedIn) {
        next({name: 'Login'})
    } else {
        next()
    }
})

export default router
