<template>
  <div class="infinite-list-wrapper" style="overflow: auto">
    <el-scrollbar height="90%">
    <ul
        v-infinite-scroll="load"
        class="list"
        :infinite-scroll-disabled="disabled"
        infinite-scroll-distance="35"
    >
      <li v-for="i in count" :key="i" class="list-item">{{ i }}</li>
    </ul>
    <p v-if="loading" style="text-align: center">Loading...</p>
      </el-scrollbar>
  </div>

</template>

<script>
export default {
  data() {
    return {
      count: 10,
      loading: false,
    }
  },
  computed: {
    noMore: function () {
      return this.count >= 20;
    },
    disabled: function () {
      return this.loading
    }
  },
  methods: {
    load: function () {
      this.loading = true
      console.log("aaaa")
      setTimeout(() => {
        this.count += 5
        this.loading = false
      }, 2000)
    }
  }
}
</script>

<style>
.infinite-list-wrapper {
  height: 580px;
}

.infinite-list-wrapper .list {
  padding: 0;
  margin: 0;
  list-style: none;
}

.infinite-list-wrapper .list-item {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 125px;
  background: var(--el-color-danger-light-9);
  color: var(--el-color-danger);
}

.infinite-list-wrapper .list-item + .list-item {
  margin-top: 10px;
}
</style>
