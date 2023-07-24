<script>
import Header from "@/components/Base/Header.vue";
import Menu from "@/components/Base/SideMenu.vue";
import LoadBase from "@/components/LoadBase.vue"

export default {
  components: {Header, Menu, LoadBase},
  data() {
    return {
      username: this.$route.query.username
    }
  }
}
</script>

<template>
  <div>
    <Layout>
      <Header
          active-name="load"
          :style="{background: '#fff'}"
          :username=username>
      </Header>
      <Layout style="height: 780px; z-index: auto">
        <Sider
            hide-trigger
            :style="{background: '#fff'}">
          <Menu
              active-name="load"
              :username=username></Menu>
        </Sider>
        <LoadBase style="" :username="username"></LoadBase>
      </Layout>
    </Layout>
  </div>
</template>
