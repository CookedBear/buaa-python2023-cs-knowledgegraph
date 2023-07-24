<script>


import API from "@/plugins/axios";
import Qs from "qs";

export default {
  props: ['username'],
  data() {
    return {
      form: {
        username: this.username,
        newPassword: '',
        checkPassword: ''
      }
    }
  },
  methods: {
    onSubmit: function () {
      if (this.form.newPassword === '') { return }
      console.log(this.form)
      if (this.form.newPassword !== this.form.checkPassword) {
        console.log("?")
      } else {
        API({
          method: 'post',
          url: '/change_password/',
          data: Qs.stringify(this.form)
        }).then(res => {
          console.log(res.data);
          if (res.data.error === 0) {
            this.$router.push(
                {
                  name: 'home',
                  query: {
                    username: this.username
                  }
                }
            );
          }
        })
      }
    }
  }
}
</script>
<template>
  <el-card style="text-align: center; height: 40%; width: 40%; margin: 50px auto auto;">
  <el-form :model="form" label-width="120px" style="margin: 20px 50px">
    <el-form-item label="新的密码">
      <el-input v-model="form.newPassword"/>
    </el-form-item>
    <el-form-item label="重复新的密码">
      <el-input v-model="form.checkPassword"/>
    </el-form-item>
    <el-form-item>
      <el-button type="primary" @click="onSubmit" style="margin-top: 50px; ">Submit</el-button>
    </el-form-item>
  </el-form>
    </el-card>
</template>
