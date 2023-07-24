<template>
  <Header
      active-name="about"
      style="background: #fff; z-index: 11"
      :username=username>
  </Header>
  <Layout :style="{height: '780px'}">
    <Sider
        hide-trigger
        style="background: #fff; z-index: 10">
    <Menu
        activeName="about"
        :username=username></Menu>
    </Sider>
    <div class="about">
      <h1>This is an about page</h1>
      <Test></Test>
    </div>
  </Layout>

</template>

<style>
.about {
  height: 88%;
  text-align: center;
  padding: 15px;
}
</style>

<script>
import Header from "@/components/Base/Header.vue";
import Menu from "@/components/Base/SideMenu.vue"
import Test from "@/components/Base/Test.vue"

export default {
  components: {Header, Menu, Test},
  data() {
    return {
      username: this.$route.query.username
    }
  }
}
</script>
