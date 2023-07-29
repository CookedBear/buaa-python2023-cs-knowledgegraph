<script>
import Header from "@/components/Base/Header.vue";
import Menu from "@/components/Base/SideMenu.vue";
import HomeBase from "@/components/HomeBase.vue"
import TabCard from "@/components/Base/TabCard.vue"
import {Layout} from "view-ui-plus";

export default {
  components: {Layout, Header, Menu, HomeBase, TabCard},
  data() {
    return {
      displayCard: false,
      username: this.$route.query.username
    }
  },
}
</script>

<template>
  <div>
    <Layout>
      <Header
          active-name="home"
          :style="{background: '#fff'}"
          :username=username>
      </Header>
      <Layout style="">
        <Sider
            hide-trigger
            :style="{background: '#fff'}">
          <Menu
              style="height: 640px"
              active-name="home"
              :username=username>
          </Menu>
        </Sider>
        <HomeBase
            style="height: 650px"
            :username=username>
        </HomeBase>
        <Card v-show="displayCard === true">
          <TabCard></TabCard>
        </Card>
      </Layout>
    </Layout>
  </div>
</template>

<style>

/deep/ .ivu-layout-header {
  background: #ffffff;
}
</style>
