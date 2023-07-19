<template>
  <p style="padding: 15px">No Content.</p>
  <button @click="getNode" style="height: 50px">Trial</button>
  <Layout>{{ datas }}</Layout>
  <AddNode></AddNode>
</template>

<script>

import API from "@/plugins/axios.js"
import AddNode from "@/components/AddNode.vue"

export default {
  components: {AddNode},
  data() {
    return {
      datas: ''
    }
  },
  methods: {
    getNode() {
      console.log("begin to get")
      API({
        method: 'get',
        url: '/show_nodes/',
      }).then(res => {
        console.log(res.data);
        this.datas = res.data;
      })

    }
  }
}
// https:/image.anosu.top/pixiv/direct?r18=1&keyword=azurlane
</script>
