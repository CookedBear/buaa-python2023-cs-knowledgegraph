<script>
import API from "@/plugins/axios.js"
import Qs from 'qs'

export default {
  data() {
    return {
      autoLogin: false,
      switcher: 'login',
      login_data: {
        username: '',
        password: '',
      },
      login_result: ' ',
      login_error: false,
      visible: 'visible'
    }
  },
  methods: {
    handleSubmit: function (valid, { username, password }) {

      console.log(username)
      this.login_data.username = username
      this.login_data.password = password
      console.log(Qs.stringify(this.login_data))
      API({
        method: 'post',
        url: '/login_in/',
        data: Qs.stringify(this.login_data)
      }).then(res => {
        console.log(res.data);
        this.login_result = res.data.login_result
        if (res.data.login_error == 0) {
          this.$router.push({name:'home'});
        }
      })

    },
    jumpToLost() {
      console.log("找回密码")
    }
  }
}
</script>

<template>
  <h2 style="text-align: center; margin-top: 30px">This is content in LoginCard.</h2>
  <Card style="width:50%" class="center margin">
    <Tabs :model-value="switcher" class="center card">
      <TabPane label="login" name="login">
        <Login @on-submit="handleSubmit">
          <UserName name="username"/>
          <Password name="password"/>
          <div class="demo-auto-login">
            <Checkbox v-model="autoLogin" size="large">自动登录</Checkbox>
            <a @click="jumpToLost">找回密码</a>
          </div>
          <Submit style="margin-top: 15px"/>
          <p style="margin-top: 8px; color: red; text-align: left">{{login_result}}</p>
        </Login>
      </TabPane>
      <TabPane label="register" name="register">标签二的内容</TabPane>
    </Tabs>
  </Card>
</template>

<style>
.center {
  text-align: center;
  margin: auto;
}

.margin {
  margin-top: 40px;
}

.card {
  height: 340px;
  width: 85%;
}

.ivu-tabs-nav-wrap {
  text-align: center;
}

.ivu-tabs-nav-scroll {
  display: inline-block;
}

.demo-login {
  width: 400px;
  margin: 0 auto !important;
}

.demo-auto-login {
  margin-bottom: 24px;
  text-align: left;
}

.demo-auto-login a {
  float: right;
}
</style>
