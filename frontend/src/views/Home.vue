<script>
import Header from "@/components/Header.vue";
import Menu from "@/components/SideMenu.vue";
import HomeBase from "@/components/Base/HomeBase.vue"
import TabCard from "@/components/TabCard.vue"
import ForceDirected from "@/components/Base/ForceDirected.vue";

export default {
  components: {Header, Menu, HomeBase, TabCard, ForceDirected},
  data() {
    return {
      displayCard: false
    }
  },
  methods: {
    changeCardDisplay: function () {
      this.displayCard = !this.displayCard;
      // <HomeBase @changeCardDisplay="changeCardDisplay"></HomeBase>
    }
  }
}
</script>

<template>
  <div>
    <Layout>
      <Header active-name="home" :style="{background: '#fff'}"></Header>
      <Layout :style="{height: '780px'}">
        <Sider hide-trigger :style="{background: '#fff'}">
          <Menu active-name="home"></Menu>
        </Sider>

        <ForceDirected width="1000" height="700" :nodes="nodes" :edges="edges"></ForceDirected>
        <Card v-show="displayCard == true">
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
