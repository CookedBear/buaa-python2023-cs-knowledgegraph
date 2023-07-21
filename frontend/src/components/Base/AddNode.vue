<template>

  <Card style="height: 250px; width: 300px; background: rgb(239,255,246); ">
    <br>
    <Form :model="formItem" :label-width="80">
      <FormItem label="Input">
        <AutoComplete
            v-model="formItem.input"
            placeholder="Enter Node name."
            :data="nodenames"></AutoComplete>
      </FormItem>
      <FormItem label="Level">
        <Input v-model="formItem.relation" type="number"
               placeholder="Enter level of the node."></Input>
      </FormItem>
      <FormItem>
        <Button type="primary" @click="submitNode">Submit</Button>
        <Button style="margin-left: 8px" @click="hide">Cancel</Button>
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
      console.log(this.formItem)
      console.log({'node1': this.selected, 'node2': this.formItem.input})
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
        var params = new URLSearchParams();
        params.append('source', this.formItem.input)
        params.append('target', this.selected)
        params.append('name', 'LINKING')
        params.append('username', this.username)
        API({
          url: '/add_relation/',
          method: 'get',
          params: params
        }).then((res) => {
          console.log(res)
          if (res.data.add_error !== 0) {
            this.error_result = res.data.add_result
            return
          }
          this.$emit('rebuild')
          this.hide()
        })
        // console.log(this.nodeName)

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
