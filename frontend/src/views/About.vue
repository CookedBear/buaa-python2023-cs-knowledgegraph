<template>
  <Header active-name="about" :style="{background: '#fff'}"></Header>
  <Layout :style="{height: '780px'}">
    <Sider hide-trigger :style="{background: '#fff'}">
      <Menu activeName="about"></Menu>
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
  components: {Header, Menu, Test}
}
</script>
