<script>
export default {
  data() {

  }
}
</script>

<template>

  <Header class="horizontal-menu">
        <Menu mode="horizontal" theme="dark" active-name="1" class="horizontal-menu">
          <MenuItem name="1" to="/">
            <Icon type="ios-analytics"></Icon>
            主页
          </MenuItem>
          <MenuItem name="2" to="/self">
            <Icon type="ios-navigate"></Icon>
            个人中心
          </MenuItem>
          <MenuItem name="3" to="/about">
            <Icon type="ios-navigate"></Icon>
            关于
          </MenuItem>
        </Menu>
      </Header>
</template>

<style></style>