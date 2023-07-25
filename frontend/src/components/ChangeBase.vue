<script>


import API from "@/plugins/axios";
import Qs from "qs";

export default {
  props: ['username'],
  data() {
    const validatePassCheck = (rule, value, callback) => {
      if (value !== this.$refs.form.formValidate.password) {
        callback(new Error('两次输入的密码不匹配！'));
      } else {
        callback();
      }
    };
    return {
      form: {
        username: this.username,
        newPassword: '',
        checkPassword: ''
      },
      passwordRule: [
        {
          required: true, message: '密码不能为空！', trigger: 'change'
        },
        {
          min: 6, message: '密码不能少于6位！', trigger: 'change'
        }
      ],
      passwordConfirmRule: [
        {
          required: true, message: '确认密码不能为空！', trigger: 'change'
        },
        {validator: validatePassCheck, trigger: 'change'}
      ],
    }
  },
  methods: {
    onSubmit: function (valid, {password}) {
      if (!valid) {
        return
      }
      this.form.newPassword = this.form.checkPassword = password
      console.log(this.form)

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
</script>
<template>
  <el-card style="text-align: center; height: 40%; width: 40%; margin: 50px auto auto;">
    <Login ref="form" label-width="120px" style="margin: 20px 50px" @on-submit="onSubmit">
      <Password name="password"
                placeholder="至少6位密码，区分大小写"
                :rules="passwordRule"/>
      <Password name="repeatPassword"
                placeholder="确认密码"
                :rules="passwordConfirmRule"/>
      <Submit style="margin-top: 15px"/>
    </Login>
    <!--    <el-form :model="form" label-width="120px" style="margin: 20px 50px">-->
    <!--      <el-form-item label="新的密码">-->
    <!--        <el-input v-model="form.newPassword"/>-->
    <!--      </el-form-item>-->
    <!--      <el-form-item label="重复新的密码">-->
    <!--        <el-input v-model="form.checkPassword"/>-->
    <!--      </el-form-item>-->
    <!--      <el-form-item>-->
    <!--        <el-button type="primary" @click="onSubmit" style="margin-top: 50px; ">Submit</el-button>-->
    <!--      </el-form-item>-->
    <!--    </el-form>-->
  </el-card>
</template>
