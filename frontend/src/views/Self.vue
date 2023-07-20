<script>
import Header from "@/components/Base/Header.vue";
import Menu from "@/components/Base/SideMenu.vue";
import SelfBase from "@/components/SelfBase.vue"

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
