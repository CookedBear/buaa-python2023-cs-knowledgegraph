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
      <el-table-column prop="name" label="节点名" sortable/>
      <el-table-column prop="level" label="节点等级" sortable/>
      <el-table-column prop="time" label="添加收藏时间" sortable/>
      <el-table-column label="操作" align="center" width="150">
        <template #header>
          <el-input v-model="search" size="small" placeholder="关键字搜索..."/>
        </template>
        <template #default="scope">
          <div>
            <Button style="margin: auto auto 5px" type="info"
                    @click="handleEdit(scope.$index, scope.row)"
            >修改信息
            </Button>
            <br>
            <Button
                type="error"
                @click="handleDelete(scope.$index, scope.row)"
            >删除收藏
            </Button>
          </div>
        </template>
      </el-table-column>
    </el-table>
  </el-card>
  <el-dialog v-model="dialogDisplay" title="修改节点信息">
    <el-form :model="form" style="width: 50%; text-align: center; margin: auto auto auto 5%">
      <el-form-item label="节点名称">
        <el-input v-model="form.name" autocomplete="off"/>
      </el-form-item>
      <el-form-item label="节点等级">
        <el-input-number v-model="form.level" :min="0" :max="10"/>
      </el-form-item>
      <el-form-item label="收藏">
        <el-switch v-model="form.favourite" size="large"></el-switch>
      </el-form-item>
    </el-form>
    <template #footer>
      <span class="dialog-footer">
        <el-button @click="dialogDisplay = false">取消</el-button>
        <el-button type="primary" @click="handleSubmit">
          确认修改
        </el-button>
      </span>
    </template>
  </el-dialog>
</template>

<script>

import API from "@/plugins/axios.js"
import {Button, Space} from "view-ui-plus";
import Qs from "qs";

export default {
  components: {Space, Button},
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
        // 注意 ： ES6中，为字符串提供了一个新方法，
        // 叫做  String.prototype.includes('要包含的字符串')
        //  如果包含，则返回 true ，否则返回 false
        //  contain
        if (item.name.includes(that.search)) {
          return item
        }
      })
    }
  },
  props: ['username'],
  mounted() {
    this.getFavourite()
  },
  methods: {
    getFavourite: function () {
      console.log("getting favourite...")
      var params = new URLSearchParams();
      params.append('username', this.username)
      API({
        url: '/get_favourite/',
        method: 'get',
        params: params
      }).then((res) => {

        var nodes = []
        for (var i in res.data.nodes) {
          nodes.push({
            name: res.data.nodes[i].fields.knowledgeName,
            level: res.data.nodes[i].fields.relation,
            time: res.data.nodes[i].fields.time,
            favourite: res.data.nodes[i].fields.favourite,
          })
        }
        this.datas = nodes
        this.loading = false
      })
    },
    handleEdit: function (index, row) {
      var node = JSON.parse(JSON.stringify(row))
      console.log(index, node.name)
      this.form.name = node.name
      this.name = node.name
      this.form.level = node.level
      this.form.favourite = (node.favourite === 1);
      this.dialogDisplay = true
    },
    handleDelete: function (index, row) {
      console.log(index, JSON.parse(JSON.stringify(row)).name)
      var data = {}
      data['nodename'] = JSON.parse(JSON.stringify(row)).name
      data['username'] = this.username
      data['favourite'] = 0
      API({
        url: '/change_favourite/',
        method: 'post',
        data: (Qs.stringify(data))
      }).then((res) => {
        console.log(res)
        this.getFavourite()
      })
    },
    handleSubmit: function () {
      this.dialogDisplay = false
      var data = {}
      data['nodename'] = this.name
      data['username'] = this.username
      data['favourite'] = (this.form.favourite === true) ? 1 : 0
      API({
        url: '/change_favourite/',
        method: 'post',
        data: (Qs.stringify(data))
      }).then((res) => {
        var data = {}
        data['username'] = this.username
        data['oldname'] = this.name
        data['newname'] = this.form.name
        data['level'] = this.form.level
        console.log(data)
        API({
          url: '/change_node/',
          method: 'post',
          data: (Qs.stringify(data))
        }).then((res) => {
          console.log(res)
          this.getFavourite()
        })
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
