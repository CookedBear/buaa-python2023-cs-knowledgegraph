<template>

  <Card style="height: 250px; width: 300px; background: rgb(239,255,246); ">
    <br>
    <Form :model="formItem" :label-width="80">
      <FormItem label="节点名">
        <Input
            v-model="formItem.input"
            placeholder="请输入新名称"
            :data="nodenames"></Input>
      </FormItem>
      <FormItem label="等级">
        <el-input-number v-model="formItem.relation" :min="0" :max="10"/>
      </FormItem>
      <FormItem>
        <Button type="primary" @click="submitNode">修改</Button>
        <Button style="margin-left: 8px" @click="hide">取消</Button>
        <p style="color: red">{{ error_result }}</p>
      </FormItem>
    </Form>
  </Card>
</template>
<script>
import API from "@/plugins/axios.js"
import Qs from "qs";

export default {
  emit: ['hideCard', 'rebuild'],
  data() {
    return {
      formItem: {
        input: '',
        relation: null,
      },
      nodeName: '',
      nodenames: [],
      data: {
        source: '',
        target: '',
        name: "linking"
      },
      error_result: ''
    }
  },
  props: ['selected', 'username', 'nodes'],
  methods: {
    submitNode: function () {

      if (this.formItem.input === '') {
        return
      }
      var data = {}
      data['username'] = this.username
      data['oldname'] = this.selected
      data['newname'] = this.formItem.input
      data['level'] = this.formItem.relation
      console.log(data)
      API({
        url: '/change_node/',
        method: 'post',
        data: (Qs.stringify(data))
      }).then((res) => {
        console.log(res)
        this.$emit('rebuild')
        this.hide()
      })
    },
    hide: function () {
      this.formItem.relation = null
      this.formItem.input = ''
      this.$emit("hideCard")
    }
  },
  watch: {
    selected(val) {
      this.nodeName = val
    },
    nodes: {
      deep: true,
      handler: function () {
        for (var i in this.nodes) {
          this.nodenames.push(this.nodes[i].name)
        }
      }
    }
  }
}
</script>
