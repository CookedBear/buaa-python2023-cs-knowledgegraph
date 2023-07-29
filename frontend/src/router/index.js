import {createRouter, createWebHistory} from 'vue-router'
import Home from '@/views/Home.vue'
import About from '@/views/About.vue'
import Change from '@/views/Change.vue'
import Load from '@/views/Load.vue'
import Favourite from "@/views/Favourite.vue";
import Login from "@/views/Login.vue"

const routes = [
    {
        path: '/home',
        name: 'home',
        component: Home,
    },
    {
        path: '/about',
        name: 'about',
        component: About,
    },
    {
        path: '/self/change',
        name: 'change',
        component: Change,
    },
    {
        path: '/self/load',
        name: 'load',
        component: Load,
    },
    {
        path: '/self/favourite',
        name: 'favourite',
        component: Favourite,
    },
    {
        path: '/login',
        name: 'login',
        component: Login,
    },
    {
        path: '/',
        redirect: '/login',
    }
]

const router = createRouter({
    routes,
    history: createWebHistory(),
    scrollBehavior() {
        return {top: 0}
    }
})

export default router
