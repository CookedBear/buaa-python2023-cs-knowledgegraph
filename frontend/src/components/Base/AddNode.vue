<template>

   <Card style="height: 250px; width: 300px; background: rgb(239,255,246); ">
    <br>
    <Form :model="formItem" :label-width="80">
    <FormItem label="Input">
      <Input v-model="formItem.input" placeholder="Enter Node name."></Input>
    </FormItem>
    <FormItem label="Number">
      <Input v-model="formItem.relation" type="number"
             placeholder="Enter something..."></Input>
    </FormItem>
    <FormItem>
      <Button type="primary" @click="submitNode">Submit</Button>
      <Button style="margin-left: 8px">Cancel</Button>
    </FormItem>
  </Form>
  </Card>
</template>
<script>
import API from "@/plugins/axios.js"

export default {
  data() {
    return {
      formItem: {
        input: '',
        relation: null,
      }
    }
  },
  methods: {
    submitNode: function () {
      console.log(this.formItem)

      var params = new URLSearchParams();
      params.append('knowledgeName', this.formItem.input)
      params.append('relation', this.formItem.relation)
      API({
        url: '/add_node/',
        method: 'get',
        params: params
      }).then((res) => {
        console.log(res)
      })

    }
  }
}
</script>
