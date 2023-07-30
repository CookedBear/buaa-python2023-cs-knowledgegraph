<template>
  <Menu :active-name="activeName" theme="light" width="auto" :open-names=activeNameAt style="z-index: 2">
    <Submenu name="home">
      <template #title>
        <Icon type="ios-analytics"></Icon>
        主页
      </template>
      <MenuItem name="home" @click="toHome">我的图谱</MenuItem>
      <MenuItem name="new" @click="initGraph">新建图谱</MenuItem>
    </Submenu>
    <Submenu name="">
      <template #title>
        <Icon type="ios-analytics"></Icon>
        个人中心
      </template>
      <MenuItem name="change" @click="toChange">修改密码</MenuItem>
      <MenuItem name="load" @click="toLoad">导入/导出</MenuItem>
      <MenuItem name="favourite" @click="toFavourite">全部节点</MenuItem>
      <MenuItem name="graph" @click="toGraph">收藏的图</MenuItem>
    </Submenu>
    <MenuItem name="about" @click="toAbout">
      <Icon type="ios-navigate"></Icon>
      关于
    </MenuItem>
    <el-dialog v-model="dialogDisplay" title="加载收藏">
      <p>确定要初始化画布吗？这样会丢失当前画布中未保存的操作！</p>
      <template #footer>
      <span class="dialog-footer">
        <Button @click="dialogDisplay = false" style="margin-right: 13px">取消</Button>
        <Button type="error" @click="handleSubmit">
          确认加载
        </Button>
      </span>
      </template>
    </el-dialog>
  </Menu>

</template>
<script>
import {MenuItem} from "view-ui-plus";
import API from "@/plugins/axios";
import {ElNotification} from "element-plus";

export default {
  components: {MenuItem},
  data() {
    return {
      dialogDisplay: false,
    }
  },
  props: ['activeName', 'username'],
  computed: {
    activeNameAt: {
      immediate: true,
      get: function () {
        if (this.activeName === 'load' || this.activeName === 'change'
            || this.activeName === 'favourite' || this.activeName === 'graph') {
          return [""];
        } else if (this.activeName === 'home' || this.activeName === 'new') {
          return ["home"]
        } else {

        }
        return this.activeName;
      }
    }
  },
  methods: {
    toHome() {
      console.log(this.username)
      this.$router.push({name: 'home', query: {username: this.username}})
    },
    toChange() {
      console.log(this.username)
      this.$router.push({name: 'change', query: {username: this.username}})
    },
    toLoad() {
      console.log(this.username)
      this.$router.push({name: 'load', query: {username: this.username}})
    },
    toAbout() {
      this.$router.push({name: 'about', query: {username: this.username}})
    },
    toFavourite() {
      this.$router.push({name: 'favourite', query: {username: this.username}})
    },
    toGraph() {
      this.$router.push({name: 'graph', query: {username: this.username}})
    },
    initGraph() {
      this.dialogDisplay = true
    },
    handleSubmit() {
      var params = new URLSearchParams();
      params.append('username', this.username)
      API({
        url: '/init_graph/',
        method: 'get',
        params: params
      }).then((res) => {
        // this.$router.replace('/refresh,{username: this.username}')
        // this.$router.go(0)
        this.dialogDisplay = false

        if (this.activeName !== 'home') {
          this.$router.push({name: 'home', replace: true, query: {username: this.username}})
        } else {
          this.$router.go('/home?username=' + this.username)
        }
      })
    }
  }
}
</script>
