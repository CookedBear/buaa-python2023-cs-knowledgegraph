<template>
  <p style="padding: 15px">No Content.</p>
  <button @click="getNode" style="height: 50px">Trial</button>
  <button @click="this.display = !this.display" style="height: 50px">Show/Hide</button>
  <Layout>{{ this.datas }}</Layout>
  <AddNode v-show="display" style="position: absolute; right: 4%; bottom: 18%; z-index: 9" @hideCard="display=!display"></AddNode>

</template>

<script>

import API from "@/plugins/axios.js"
import AddNode from "@/components/Base/AddNode.vue"

export default {
  components: {AddNode},
  data() {
    return {
      datas: '',
      display: false,
    }
  },
  props: ['username'],
  methods: {
    getNode() {
      console.log("begin to get")
      API({
        method: 'get',
        url: '/show_nodes/',
      }).then(res => {
        console.log(this.username);
        this.datas = this.username;
      })

    }
  }
}
// https:/image.anosu.top/pixiv/direct?r18=1&keyword=azurlane
</script>

<style>

  .card {
    text-align: center;
    margin-right: 45px;
    margin-top: 15px;
  }

</style>
