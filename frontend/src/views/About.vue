<template>
  <Header active-name="about" :style="{background: '#fff'}"></Header>
  <Layout :style="{height: '780px'}">
        <Sider hide-trigger :style="{background: '#fff'}">
          <Menu activeName="about"></Menu>
        </Sider>
        <div class="about">
    <h1>This is an about page</h1>
  </div>
      </Layout>

</template>

<style>
  .about {
    min-height: 100vh;
    text-align: center;
    padding: 15px;
  }
</style>

<script>
import Header from "@/components/Header.vue";
import Menu from "@/components/SideMenu.vue"

export default {
  components: {Header, Menu}
}
</script>