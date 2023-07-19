<script>
export default {
  data() {
    return {

    }
  },
  props: ['activeName']
}
</script>

<template>

  <Header class="horizontal-menu">
    <Menu mode="horizontal" theme="light" :active-name="activeName" class="horizontal-menu"
          style="{background: #ffffff}">
      <MenuItem name="home" to="/">
        <Icon type="ios-analytics"></Icon>
        主页
      </MenuItem>
      <MenuItem name="self" to="/self">
        <Icon type="ios-navigate"></Icon>
        个人中心
      </MenuItem>
      <MenuItem name="about" to="/about">
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
