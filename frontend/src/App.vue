<template>
  <router-view/>
</template>

<script>
import Home from '@/views/Home.vue'
import Self from '@/views/Self.vue'
import About from '@/views/About.vue'
import Login from '@/views/Login.vue'

export default {
  name: 'App',
  components: {
    Home, Self, About, Login
  },
  data() {
    return {

    }
  }
}
</script>
