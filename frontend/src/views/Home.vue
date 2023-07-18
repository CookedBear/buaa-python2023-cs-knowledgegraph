<script>
import Header from "@/components/Header.vue";
import Menu from "@/components/SideMenu.vue";
import HomeBase from "@/components/HomeBase.vue"

export default {
  components: {Header, Menu, HomeBase}
}
</script>

<template>
  <div>
    <Layout>
      <Header></Header>
      <Layout :style="{height: '780px'}">
        <Sider hide-trigger :style="{background: '#fff'}">
          <Menu active-name="main"></Menu>
        </Sider>
        <HomeBase></HomeBase>
      </Layout>
    </Layout>
  </div>
</template>

<style>
.horizontal-menu {
  height: 80px;
  text-aligin: center;
}

.ivu-menu-item {
  text-aligin: center;
  position: center;
}
</style>
