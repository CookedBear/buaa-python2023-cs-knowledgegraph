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
      visible: 'visible',
      passwordRule: [
        {
          required: true, message: '密码不能为空！', trigger: 'change'
        },
        {
          min: 6, message: '密码不能少于6位！', trigger: 'change'
        }
      ],
    }
  },
  methods: {
    handleSubmit: function (valid, {username, password}) {
      if (username === '') {
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
        if (res.data.login_error === 0) {
          this.$router.push({name: 'home', query: {username: username}});
        }
      })
    },
    jumpToLost() {
      console.log("找回密码")
      this.login_result = '找不回了，别想了。'
    },
    handleRegister: function (valid, {username, password}) {
      if (username === '') {
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
        if (res.data.register_error === 0) {
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
  <Card style="width:60%; height: 80%" class="center margin">
    <div style="display: flex">
      <Tabs v-model="switcher" class="card">
        <TabPane label="登录" name="login">
          <Login @on-submit="handleSubmit">
            <UserName name="username"/>
            <Password name="password"/>
            <div class="demo-auto-login">
              <a @click="jumpToLost">找回密码</a>
            </div>
            <Submit style="margin-top: 15px"/>
            <p style="margin-top: 8px; color: red; text-align: left">{{ login_result }}</p>
          </Login>
        </TabPane>
        <TabPane label="注册" name="register">
          <Login @on-submit="handleRegister">
            <UserName name="username"/>
            <Password name="password"
                      placeholder="至少6位密码，区分大小写"
                      :rules="passwordRule"/>
            <div class="demo-auto-login"></div>
            <Submit style="margin-top: 15px">注册</Submit>
            <p style="margin-top: 8px; color: red; text-align: left">{{ register_result }}</p>
          </Login>
        </TabPane>
      </Tabs>
      <img src="../../assets/k-on.jpg" style="width: 65%; height: 60%">
    </div>
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
  width: 30%;
  margin-left: 3%;
  top: 50%;
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
