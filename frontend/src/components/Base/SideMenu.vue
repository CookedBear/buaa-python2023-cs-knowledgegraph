<template>
  <Menu :active-name="activeName" theme="light" width="auto" :open-names=activeNameAt style="z-index: 2">
      <MenuItem name="home" @click="toHome">
        <Icon type="ios-analytics"></Icon>
        主页
      </MenuItem>
    <Submenu name="">
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

</template>
<script>
export default {
  data() {
    return {}
  },
  props: ['activeName', 'username'],
  computed: {
    activeNameAt: {
      immediate: true,
      get: function() {
        if (this.activeName === 'load' || this.activeName === 'change') {
          return [""];
        } else if (this.activeName === 'home' || this.activeName === 'about'){
          return this.activeName;
        }
      }
    }
  },
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
