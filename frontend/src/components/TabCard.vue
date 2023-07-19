<script>
export default {
  data() {
    return {

    }
  },
  props: {
    savedValue: undefined
  }
}
</script>


<template>
  <Tabs type="card" :model-value="savedValue">
    <TabPane label="标签一" icon="logo-apple">标签一的内容</TabPane>
    <TabPane label="标签二" icon="logo-windows">标签二的内容</TabPane>
    <TabPane label="标签三" icon="logo-tux">标签三的内容</TabPane>
    <TabPane label="标签四" icon="logo-apple">标签四的内容</TabPane>
  </Tabs>
</template>


<style>

</style>