<script>
import Header from "@/components/Header.vue";
import Menu from "@/components/SideMenu.vue";
import SelfBase from "@/components/SelfBase.vue"

export default {
  components: {Header, Menu, SelfBase}
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
        <SelfBase></SelfBase>
      </Layout>
    </Layout>
  </div>
</template>