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
      register_data: {
        username: '',
        password: '',
      },
      register_result: ' ',
      register_error: false,
      visible: 'visible'
    }
  },
  methods: {
    handleSubmit: function (valid, {username, password}) {
      if (username == '') {
        return
      }
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
          this.$router.push(
              {
                name: 'home',
                query: {
                  username: username
                }
              }
          );
        }
      })
    },
    jumpToLost() {
      console.log("找回密码")
      this.login_result = '找不回了，别想了。'
    },
    handleRegister: function (valid, {username, password}) {
      if (username == '') {
        return
      }
      this.register_data.username = username
      this.register_data.password = password
      console.log(Qs.stringify(this.register_data))
      API({
        method: 'post',
        url: '/register/',
        data: Qs.stringify(this.register_data)
      }).then(res => {
        console.log(res.data);
        this.register_result = res.data.register_result
        if (res.data.register_error == 0) {
          this.switcher = 'login'
          this.login_data.username = this.register_data.username
          this.login_data.password = this.register_data.password
        }
      })
    }
  }
}
</script>

<template>
  <h2 style="text-align: center; margin-top: 30px">This is content in LoginCard.</h2>
  <Card style="width:45%; height: 50%" class="center margin">
    <Tabs v-model="switcher" class="center card">
      <TabPane label="login" name="login">
        <Login @on-submit="handleSubmit">
          <UserName name="username"/>
          <Password name="password"/>
          <div class="demo-auto-login">
            <Checkbox v-model="autoLogin" size="large">自动登录</Checkbox>
            <a @click="jumpToLost">找回密码</a>
          </div>
          <Submit style="margin-top: 15px"/>
          <p style="margin-top: 8px; color: red; text-align: left">{{ login_result }}</p>
        </Login>
      </TabPane>
      <TabPane label="register" name="register">
        <Login @on-submit="handleRegister">
          <UserName name="username"/>
          <Password name="password"/>
          <div class="demo-auto-login"></div>
          <Submit style="margin-top: 15px">注册</Submit>
          <p style="margin-top: 8px; color: red; text-align: left">{{ register_result }}</p>
        </Login>
      </TabPane>
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
  width: 50%;
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
