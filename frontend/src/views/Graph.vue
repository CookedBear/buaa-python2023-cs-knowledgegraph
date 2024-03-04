<template>
  <div>
    <Layout>
      <Header
          active-name="graph"
          :style="{background: '#fff'}"
          :username=username>
      </Header>
      <Layout style="height: 650px; z-index: auto">
        <Sider
            hide-trigger
            :style="{background: '#fff'}">
          <Menu
              active-name="graph"
              :username=username></Menu>
        </Sider>
        <GraphBase style="" :username="username"></GraphBase>
      </Layout>
    </Layout>
  </div>
</template>


<script>
import Header from "@/components/Base/Header.vue"
import Menu from "@/components/Base/SideMenu.vue"
import GraphBase from "@/components/GraphBase.vue";

export default {
  components: {Header, Menu, GraphBase},
  data() {
    return {
      username: this.$route.query.username
    }
  }
}
</script>

<style>
</style>
