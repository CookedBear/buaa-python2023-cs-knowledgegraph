<script>
export default {
  data() {
    return {}
  },
  props: ['activeName', 'username'],
  methods: {
    toHome() {
      console.log(this.username)
      this.$router.push({name: 'home', query: {username: this.username}})
    },
    toChange() {
      console.log(this.username)
      this.$router.push({name: 'change', query: {username: this.username}})
    },
    toLoad() {
      console.log(this.username)
      this.$router.push({name: 'load', query: {username: this.username}})
    },
    toAbout() {
      this.$router.push({name: 'about', query: {username: this.username}})
    }
  }
}
</script>

<template>

  <Header class="horizontal-menu" style="z-index: 3">
    <Menu mode="horizontal" theme="light" :active-name="activeName" class="horizontal-menu"
          style="{background: #ffffff; z-index: 3}">
      <MenuItem name="home" @click="toHome">
        <Icon type="ios-analytics"></Icon>
        主页
      </MenuItem>
      <Submenu name="2">
      <template #title>
        <Icon type="ios-analytics"></Icon>
      个人中心
      </template>
      <MenuItem name="change" @click="toChange">修改密码</MenuItem>
      <MenuItem name="load" @click="toLoad">导入/导出</MenuItem>
    </Submenu>
      <MenuItem name="about" @click="toAbout">
        <Icon type="ios-navigate"></Icon>
        关于
      </MenuItem>
    </Menu>
  </Header>
</template>

<style>
.ivu-layout-header {
  padding: 0;
}
</style>
