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
    toSelf() {
      console.log(this.username)
      this.$router.push({name: 'self', query: {username: this.username}})
    },
    toAbout() {
      this.$router.push({name: 'about', query: {username: this.username}})
    }
  }
}
</script>

<template>

  <Header class="horizontal-menu">
    <Menu mode="horizontal" theme="light" :active-name="activeName" class="horizontal-menu"
          style="{background: #ffffff}">
      <MenuItem name="home" @click="toHome">
        <Icon type="ios-analytics"></Icon>
        主页
      </MenuItem>
      <MenuItem name="self" @click="toSelf">
        <Icon type="ios-navigate"></Icon>
        个人中心
      </MenuItem>
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
