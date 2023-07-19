<template>
  <Menu :active-name="activeName" theme="light" width="auto" :open-names=activeNameAt>
    <Submenu name="1">
      <template #title>
        <Icon type="ios-navigate"></Icon>
        主页
      </template>
      <MenuItem name="home" to="/">Main</MenuItem>
      <MenuItem name="1-2">Option 2</MenuItem>
      <MenuItem name="1-3">Option 3</MenuItem>
    </Submenu>
    <MenuItem name="self" to="/self">
      <Icon type="ios-analytics"></Icon>
      个人中心
    </MenuItem>
    <MenuItem name="about" to="/about">
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
  props: {
    activeName: 'activeName'
  },
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
  }
}
</script>