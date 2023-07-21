<script>
import {ElNotification} from 'element-plus'
import CreepContent from "@/components/Base/CreepContent.vue"

export default {
  components: {CreepContent},
  emit: ['hideCard'],
  data() {
    return {
      editableTabsValue: 'bilibili',
      editableTabs: [
        {
          title: 'Tab 1',
          name: '1',
          content: 'Tab 2 content',
        },
        {
          title: 'Tab 2',
          name: '2',
          content: 'Tab 2 content',
        },
      ]
    }
  },
  props: ['knowledge'],
  methods: {
    close: function () {
      ElNotification({
        title: '哈哈，太着急了吧',
        message: '现成的都拉成这德行，还想要拓展功能？',
        type: 'info',
      })
      this.$emit("hideCard")
    },
    loading: function () {
      this.$Loading.start();
    },
    loaded: function () {
      this.$Loading.finish();
    },
  }
}
</script>


<template>
  <el-card style="height: 87%; width: 25%;">
    <div class="card-header">
      <span>{{knowledge}}</span>
      <el-button style="background-color: #beffde" text @click="close">Add Resource</el-button>
    </div>
    <el-tabs
        v-model="editableTabsValue"
        type="border-card"
        class="demo-tabs"
        style="margin-top: 8px"
    >
      <el-tab-pane name="bilibili" label="bili">
        <CreepContent></CreepContent>
      </el-tab-pane>
      <el-tab-pane
          v-for="item in editableTabs"
          :key="item.name"
          :label="item.title"
          :name="item.name"
      >
      </el-tab-pane>
      {{editableTabsValue}}
    </el-tabs>
  </el-card>
</template>


<style>
.card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 18px;
}
</style>
