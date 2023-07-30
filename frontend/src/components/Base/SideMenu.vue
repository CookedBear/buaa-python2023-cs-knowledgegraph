<template>
  <Menu :active-name="activeName" theme="light" width="auto" :open-names=activeNameAt style="z-index: 2">
    <Submenu name="home">
      <template #title>
        <Icon type="ios-analytics"></Icon>
        主页
      </template>
      <MenuItem name="home" @click="toHome">我的图谱</MenuItem>
      <Button name="new2" @click="addSelf" v-if="isHome"
              style="margin: 10px auto 10px 50px; font-size: small" type='primary'
              size="small">添加孤立节点<br>
      </Button>
      <Button name="new1" @click="initGraph" v-if="isHome"
              style="margin: 0 auto 10px 50px; font-size: small" type='primary'
              size="small">
        新建图谱<br>
      </Button>
      <Button name="new2" @click="favouriteGraph" v-if="isHome"
              style="margin: 0 auto 10px 50px; font-size: small" type='primary'
              size="small">收藏图谱<br>
      </Button>
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
    <el-dialog v-model="dialogDisplay" title="初始化画布">
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
    <el-dialog v-model="dialogDisplay2" title="保存为收藏">
      <el-form style="width: 50%; text-align: center; margin: auto auto auto 5%">
        <el-form-item label="收藏名">
          <el-input v-model="graphname" autocomplete="off"/>
        </el-form-item>
      </el-form>
      <template #footer>
      <span class="dialog-footer">
        <Button @click="dialogDisplay2 = false" style="margin-right: 10px">取消</Button>
        <Button type="primary" @click="addFavourite">
          确认
        </Button>
      </span>
      </template>
    </el-dialog>
    <el-dialog v-model="addSelfDisplay" title="添加孤立节点">
      <AddSelf v-show="addSelfDisplay === true"
               style="width: 50%; margin: auto auto auto 5%"
               :username=username
               @hideCard="addSelfDisplay=!addSelfDisplay"
               @rebuild="this.$router.go('/home?username=' + this.username)"></AddSelf>
    </el-dialog>
  </Menu>


</template>
<script>
import {MenuItem} from "view-ui-plus";
import API from "@/plugins/axios";
import {ElNotification} from "element-plus";
import AddSelf from "@/components/Base/AddSelf.vue";

export default {
  components: {AddSelf, MenuItem},
  data() {
    return {
      dialogDisplay: false,
      dialogDisplay2: false,
      addSelfDisplay: false,
      graphname: '',
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
    },
    isHome: {
      immediate: true,
      get: function () {
        if (this.activeName === 'home') {
          return true
        } else {
          return false
        }
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
      this.dialogDisplay2 = false
      this.addSelfDisplay = false
    },
    favouriteGraph() {
      this.dialogDisplay = false
      this.dialogDisplay2 = true
      this.addSelfDisplay = false
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
    },
    addSelf: function () {
      this.addSelfDisplay = true
      this.dialogDisplay = false
      this.dialogDisplay2 = false
    },
    addFavourite: function () {
      var params = new URLSearchParams();
      params.append('username', this.username)
      params.append('graphname', this.graphname)
      API({
        url: '/favourite_graph/',
        method: 'get',
        params: params
      }).then((res) => {
        console.log(res)
        if (res.data.add_error === 0) {
          this.dialogDisplay2 = false
          ElNotification({
            title: '收藏添加成功',
            message: '成功添加名为 ' + this.graphname + ' 的收藏',
            type: 'success',
          })
        } else {
          ElNotification({
            title: '哈哈，太着急了吧',
            message: res.data.add_result,
            type: 'error',
          })
        }
      })
    },
  }
}
</script>
