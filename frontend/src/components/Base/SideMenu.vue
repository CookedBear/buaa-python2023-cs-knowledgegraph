<template>
  <Menu :active-name="activeName" theme="light" width="auto" :open-names=activeNameAt>
    <Submenu name="1">
      <template #title>
        <Icon type="ios-navigate"></Icon>
        主页
      </template>
      <MenuItem name="home" @click="toHome">Main</MenuItem>
      <MenuItem name="1-2">Option 2</MenuItem>
      <MenuItem name="1-3">Option 3</MenuItem>
    </Submenu>
    <MenuItem name="self" @click="toSelf">
      <Icon type="ios-analytics"></Icon>
      个人中心
    </MenuItem>
    <MenuItem name="about" @click="toAbout">
      <Icon type="ios-analytics"></Icon>
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
        if (this.activeName === 'home') {
          return ["1"];
        } else {
          return [""];
        }
      }
    }
  },
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
