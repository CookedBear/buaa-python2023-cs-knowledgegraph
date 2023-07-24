<script>
import {UploadFilled} from '@element-plus/icons-vue'
import {Button} from "view-ui-plus";
import API from "@/plugins/axios";
import Qs from "qs";

export default {
  components: {Button},
  data() {
    return {
      fileData: {username: this.username,}
    }
  },
  props: ['username'],
  methods: {
    success: function () {
      this.$router.push({name: 'home', query: {username: this.username}})
    },
    downloadGraph: function () {
      API({
          method: 'get',
          url: '/download_graph/',
          params: {
            username: this.username
          }
        }).then(res => {
          console.log(res.data);
        })
      window.open("http://localhost:8000/api/download_graph?username=" + this.username, '_blank')
    }
  }
}
</script>

<template>
  <el-upload
      class="upload-demo"
      drag
      action="http://localhost:8000/api/upload_graph/"
      accept=".json"
      :on-success=success
      :data="fileData"
  >
    <el-icon class="el-icon--upload"><upload-filled /></el-icon>
    <div class="el-upload__text">
      Drop file here or <em>click to upload</em>
    </div>
    <div class="el-upload__tip">
      jpg/png files with a size less than 500kb
    </div>

  </el-upload>
  <Button type="primary" @click="downloadGraph" size="large">downloadGraph</Button>
</template>

<style>

</style>
