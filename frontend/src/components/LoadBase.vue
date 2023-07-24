<template>
<!--  <p style="padding: 15px">No Content.</p>-->
<!--  <button @click="getNode" style="height: 50px">Trial</button>-->
<!--  <button @click="this.display = !this.display" style="height: 50px">Show/Hide</button>-->
<!--  <Layout>{{ this.datas }}</Layout>-->
<!--  <AddNode v-show="display" style="position: absolute; right: 4%; bottom: 18%; z-index: 9" @hideCard="display=!display"></AddNode>-->
<Upload :username="username"></Upload>
</template>

<script>

import API from "@/plugins/axios.js"
import Upload from "@/components/Base/Upload.vue"

export default {
  components: {Upload},
  data() {
    return {
      datas: '',
      display: false,
    }
  },
  props: ['username'],
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
