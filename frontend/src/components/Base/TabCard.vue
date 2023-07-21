<script>
import {ElNotification} from 'element-plus'
import {h} from 'vue'

export default {
  emit: ['hideCard'],
  data() {
    return {
      editableTabsValue: 2,
      editableTabs: [
        {
          title: 'Tab 1',
          name: '1',
          content: 'Tab 1 content',
        },
        {
          title: 'Tab 2',
          name: '2',
          content: 'Tab 2 content',
        },
        {
          title: 'Tab 2',
          name: '2',
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
  props: {
    savedValue: undefined
  },
  methods: {
    close: function () {
      ElNotification({
        title: '哈哈，太着急了吧',
        message: '现成的都拉成这德行，还想要拓展功能？',
        type: 'info',
      })
      this.$emit("hideCard")
    }
  }
}
</script>


<template>
  <el-card style="height: 750px; width: 340px;">
    <div class="card-header">
      <span>Recommendation</span>
      <el-button style="background-color: #beffde" text @click="close">Add Resource</el-button>
    </div>
    <el-tabs
        v-model="editableTabsValue"
        type="card"
        class="demo-tabs"
        style="margin-top: 8px"
    >
      <el-tab-pane
          v-for="item in editableTabs"
          :key="item.name"
          :label="item.title"
          :name="item.name"
      >
        {{ item.content }}
      </el-tab-pane>
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
