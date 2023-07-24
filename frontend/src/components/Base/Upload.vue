<script>
import {UploadFilled} from '@element-plus/icons-vue'

export default {
  data() {
    return {
      fileData: {username: this.username,}
    }
  },
  props: ['username'],
  methods: {
    success: function () {
      this.$router.push(
              {
                name: 'home',
                query: {
                  username: this.username
                }
              }
          );
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
</template>

<style>

</style>
