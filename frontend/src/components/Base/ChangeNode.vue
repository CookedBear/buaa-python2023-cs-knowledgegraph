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
