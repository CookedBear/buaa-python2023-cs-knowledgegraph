<script>
import {UploadFilled} from '@element-plus/icons-vue'
import {Button} from "view-ui-plus";
import API from "@/plugins/axios";
import Qs from "qs";
import {ElNotification} from "element-plus";

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
      ElNotification({
        title: '成功上传',
        message: '成功上传文件至当前画布',
        type: 'success',
      })
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
  <el-card style="text-align: center; height: 65%; width: 40%; margin: 50px auto auto;">
    <el-upload
        style="margin: 30px"
        drag
        action="http://localhost:8000/api/upload_graph/"
        accept=".json"
        :on-success=success
        :data="fileData"
    >
      <el-icon class="el-icon--upload">
        <upload-filled/>
      </el-icon>
      <div class="el-upload__text">
        Drop file here or <em>click to upload</em>
      </div>
      <div class="el-upload__tip">
        使用本站点下载的布局文件，限制为 json 格式
      </div>

    </el-upload>
    <Button
        style="margin-top: 20px"
        type="primary"
        @click="downloadGraph"
        size="large">下载当前画布布局文件
    </Button>
  </el-card>
</template>

<style>

</style>
