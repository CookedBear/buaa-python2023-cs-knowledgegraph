<script>
import Header from "@/components/Base/Header.vue";
import Menu from "@/components/Base/SideMenu.vue";
import ChangeBase from "@/components/ChangeBase.vue"

export default {
  components: {Header, Menu, ChangeBase},
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
          active-name="change"
          :style="{background: '#fff'}"
          :username=username>
      </Header>
      <Layout :style="{height: '640px'}">
        <Sider
            hide-trigger
            :style="{background: '#fff'}">
          <Menu
              active-name="change"
              :username=username></Menu>
        </Sider>
        <ChangeBase :username=username></ChangeBase>
      </Layout>
    </Layout>
  </div>
</template>
