<template>

  <Form :model="formItem" :label-width="80">
    <FormItem label="节点名">
      <Input v-model="formItem.input" placeholder="请输入新节点名称"></Input>
    </FormItem>
    <FormItem label="等级">
      <el-input-number v-model="formItem.relation" :min="0" :max="10"/>
    </FormItem>
    <FormItem>
      <Button type="primary" @click="submitNode">添加</Button>
      <Button style="margin-left: 10px" @click="hide">取消</Button>
      <p style="color: red">{{ error_result }}</p>
    </FormItem>
  </Form>
</template>
<script>
import API from "@/plugins/axios.js"
import Qs from "qs";
import {ElNotification} from "element-plus";

export default {
  emit: ['hideCard', 'rebuild'],
  props: ['username'],
  data() {
    return {
      formItem: {
        input: '',
        relation: null,
      },
      nodeName: '',
      data: {
        source: '',
        target: '',
        name: "linking"
      },
      error_result: ''
    }
  },
  methods: {
    submitNode: function () {
      console.log(this.formItem)
      if (this.formItem.input === '') {
        return
      }

      var params = new URLSearchParams();
      params.append('knowledgeName', this.formItem.input)
      params.append('relation', this.formItem.relation)
      params.append('username', this.username)
      API({
        url: '/add_node/',
        method: 'get',
        params: params
      }).then((res) => {
        console.log(res)
        if (res.data.error_num !== 0) {
          this.error_result = res.data.msg
          return
        }
        this.$emit('rebuild')
        this.hide()
        // console.log(this.nodeName)

      })
    },
    hide: function () {
      this.formItem.relation = null
      this.formItem.input = ''
      this.$emit("hideCard")
    }
  },
}
</script>
