<template>
  <el-card style=" text-align: center; height: 90%; width: 75%; margin: 20px auto auto;">
    <el-table
        v-loading="loading"
        stripe border
        :data="displayDatas"
        max-height="515"
        :default-sort="{ prop: 'name', order: 'descending' }"
        style="width: 90%; margin: 20px auto auto;"
    >
      <el-table-column prop="name" label="收藏名" sortable/>
      <el-table-column prop="nodeCount" label="总节点数量" sortable/>
      <el-table-column prop="time" label="添加收藏时间" sortable/>
      <el-table-column label="操作" align="center" width="150">
        <template #header>
          <el-input v-model="search" size="small" placeholder="关键字搜索..."/>
        </template>
        <template #default="scope">
          <div>
            <Button style="margin: auto auto 5px" type="info"
                    @click="handleEdit(scope.$index, scope.row)"
            >加载到画布
            </Button>
            <br>
            <Button
                type="error"
                @click="handleDelete(scope.$index, scope.row)"
            >删除此收藏
            </Button>
          </div>
        </template>
      </el-table-column>
    </el-table>
  </el-card>
  <el-dialog v-model="dialogDisplay" title="加载收藏">
    <p>确定要加载收藏吗？这样会丢失当前画布中未保存的操作！</p>
    <template #footer>
      <span class="dialog-footer">
        <Button @click="dialogDisplay = false" style="margin-right: 13px">取消</Button>
        <Button type="error" @click="handleSubmit">
          确认加载
        </Button>
      </span>
    </template>
  </el-dialog>
</template>

<script>

import API from "@/plugins/axios.js"
import {Button} from "view-ui-plus";
import Qs from "qs";
import {ElNotification} from "element-plus";

export default {
  components: {Button},
  data() {
    return {
      datas: [],
      display: false,
      loading: true,
      search: '',
      dialogDisplay: false,
      form: [],
      name: '',
    }
  },
  computed: {
    displayDatas: function () {
      var that = this
      return this.datas.filter(item => {
        if (item.name.includes(that.search)) {
          return item
        }
      })
    }
  },
  props: ['username'],
  mounted() {
    this.getFavouriteGraphs()
  },
  methods: {
    getFavouriteGraphs: function () {
      console.log("getting favourite...")
      var params = new URLSearchParams();
      params.append('username', this.username)
      API({
        url: '/get_favourite_list/',
        method: 'get',
        params: params
      }).then((res) => {
        var graphs = []
        for (var i in res.data.graphs) {
          graphs.push({
            name: res.data.graphs[i].fields.favourite,
            nodeCount: res.data.graphs[i].fields.nodecount,
            time: res.data.graphs[i].fields.time,
          })
        }
        this.datas = graphs
        this.loading = false
      })
    },
    handleEdit: function (index, row) {
      var graph = JSON.parse(JSON.stringify(row))
      this.name = graph.name
      this.dialogDisplay = true
    },
    handleDelete: function (index, row) {
      console.log(index, JSON.parse(JSON.stringify(row)).name)
      var params = new URLSearchParams();
      params.append('username', this.username)
      params.append('graphname', JSON.parse(JSON.stringify(row)).name)
      this.loading = true
      API({
        url: '/delete_favourite_graph/',
        method: 'get',
        params: params
      }).then((res) => {
        console.log(res)
        ElNotification({
          title: '成功删除',
          message: '成功修改删除收藏 ' + JSON.parse(JSON.stringify(row)).name,
          type: 'success',
        })
        this.getFavouriteGraphs()
      })
    },
    handleSubmit: function () {
      this.dialogDisplay = false
      var params = new URLSearchParams();
      params.append('username', this.username)
      params.append('favourite', this.name)
      API({
        url: '/load_favourite/',
        method: 'get',
        params: params
      }).then((res) => {
        ElNotification({
          title: '成功加载',
          message: '成功修改加载收藏 ' + this.name + ' 至当前画布',
          type: 'success',
        })
        this.$router.push({name: 'home', query: {username: this.username}})
      })
    }
  }
}
</script>

<style>
.card {
  text-align: center;
  margin-right: 45px;
  margin-top: 15px;
}
</style>
