<script>
import Header from "@/components/Header.vue";
import Menu from "@/components/SideMenu.vue";
import SelfBase from "@/components/Base/SelfBase.vue"

export default {
  components: {Header, Menu, SelfBase}
}
</script>

<template>
  <div>
    <Layout>
      <Header active-name="self" :style="{background: '#fff'}"></Header>
      <Layout :style="{height: '780px'}">
        <Sider hide-trigger :style="{background: '#fff'}">
          <Menu active-name="self"></Menu>
        </Sider>
        <SelfBase></SelfBase>
      </Layout>
    </Layout>
  </div>
</template>