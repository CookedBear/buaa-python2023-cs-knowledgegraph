<script>
import Header from "@/components/Base/Header.vue";
import Menu from "@/components/Base/SideMenu.vue";
import FavouriteBase from "@/components/FavouriteBase.vue"

export default {
  components: {Header, Menu, FavouriteBase},
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
          active-name="favourite"
          :style="{background: '#fff'}"
          :username=username>
      </Header>
      <Layout style="height: 650px; z-index: auto">
        <Sider
            hide-trigger
            :style="{background: '#fff'}">
          <Menu
              active-name="favourite"
              :username=username></Menu>
        </Sider>
        <FavouriteBase style="" :username="username"></FavouriteBase>
      </Layout>
    </Layout>
  </div>
</template>
