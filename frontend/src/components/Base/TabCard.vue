<script>
import {ElNotification} from 'element-plus'
import Bili from "@/components/Base/Bili.vue"
import API from "@/plugins/axios";
import Qs from "qs";
import Imooc from "@/components/Base/Imooc.vue";
import Icourse163 from "@/components/Base/Icourse163.vue";
import Icourses from "@/components/Base/Icourses.vue";
import Study163 from "@/components/Base/Study163.vue";
import Cnmooc from "@/components/Base/Cnmooc.vue";
import Cmooc from "@/components/Base/Cmooc.vue";
import Xuetangx from "@/components/Base/Xuetangx.vue";

export default {
  components: {Xuetangx, Cmooc, Icourse163, Icourses, Imooc, Bili, Study163, Cnmooc},
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
      ],
      displayData: {}
    }
  },
  props: ['knowledge', 'bilibili', 'imooc', 'icourse163', 'icourses', 'study163', 'cnmooc', 'cmooc', 'xuetangx'],
  methods: {
    close: function () {
      this.$emit("hideCard")
    },
    loading: function () {
      this.$Loading.start();
    },
    loaded: function () {
      this.$Loading.finish();
    },
  },
  mounted() {
    // this.getCreepContent()
  }
}
</script>


<template>
  <el-card style="height: 87%; width: 25%;">
    <div class="card-header">
      <span>{{ knowledge }}</span>
      <Button type="primary" text @click="close">关闭窗口</Button>
    </div>
    <el-tabs
        v-model="editableTabsValue"
        type="border-card"
        class="demo-tabs"
        style="margin-top: 8px"
    >
      <el-tab-pane name="bilibili" label="Bilibili">
        <Bili
            :data="this.bilibili"></Bili>
      </el-tab-pane>
      <el-tab-pane name="cmooc" label="cmooc">
        <Cmooc
            :data="this.cmooc"></Cmooc>
      </el-tab-pane>
      <el-tab-pane name="cnmooc" label="cnmooc">
        <Cnmooc
            :data="this.cnmooc"></Cnmooc>
      </el-tab-pane>
      <el-tab-pane name="iMooc" label="iMooc">
        <Imooc
            :data="this.imooc"></Imooc>
      </el-tab-pane>
      <el-tab-pane name="iCourse163" label="iCourse163">
        <Icourse163
            :data="this.icourse163"></Icourse163>
      </el-tab-pane>
      <el-tab-pane name="iCourses" label="iCourses">
        <Icourses
            :data="this.icourses"></Icourses>
      </el-tab-pane>
      <el-tab-pane name="study163" label="study163">
        <Study163
            :data="this.study163"></Study163>
      </el-tab-pane>
      <el-tab-pane name="xuetangx" label="xuetangx">
        <Xuetangx
            :data="this.xuetangx"></Xuetangx>
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
