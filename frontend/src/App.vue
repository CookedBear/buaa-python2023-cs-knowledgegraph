<template>
  <router-view/>
</template>

<script>
import Home from '@/views/Home.vue'
import Change from '@/views/Change.vue'
import Load from '@/views/Load.vue'
import About from '@/views/About.vue'
import Login from '@/views/Login.vue'

export default {
  name: 'App',
  components: {
    Home, Change, Load, About, Login
  },
  data() {
    return {

    }
  }
}
</script>
