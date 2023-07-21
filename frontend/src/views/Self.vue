<script>
import Header from "@/components/Base/Header.vue";
import Menu from "@/components/Base/SideMenu.vue";
import SelfBase from "@/components/SelfBase.vue"

export default {
  components: {Header, Menu, SelfBase},
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
          active-name="self"
          :style="{background: '#fff'}"
          :username=username>
      </Header>
      <Layout :style="{height: '780px'}">
        <Sider
            hide-trigger
            :style="{background: '#fff'}">
          <Menu
              active-name="self"
              :username=username></Menu>
        </Sider>
        <SelfBase :username=username></SelfBase>
      </Layout>
    </Layout>
  </div>
</template>
