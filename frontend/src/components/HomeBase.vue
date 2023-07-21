<script>
import * as echarts from "echarts";
import AddNode from "@/components/Base/AddNode.vue"
import API from "@/plugins/axios";
import Qs from "qs";
import AddSelf from "@/components/AddSelf.vue";
import TabCard from "@/components/Base/TabCard.vue";

export default {
  props: {
    username: String
  },
  methods: {
    mainClick: function () {
      this.contextmenu = false
      this.$refs.rightMenu.style.display = 'none';
      this.$refs.rightMenu1.style.display = 'none';
    },
    addNode: function () {
      // 显示卡片：节点名 + 级别; 菜单自消失
      this.addNodeDisplay = true
      this.$refs.rightMenu.style.display = 'none';
    },
    addSingle: function () {
      this.addSelfDisplay = true
      this.$refs.rightMenu.style.display = 'none';
    },
    setChartsOn: function () {
      const that = this;
      // console.log(this.graphNodes)
      var myChart = echarts.getInstanceByDom(document.getElementById('main'))
      if (myChart == null) {
        myChart = echarts.init(document.getElementById('main'));
      }
      myChart.setOption({
        tooltip: {
          show: true,
          formatter: "<div style='display:block;word-break: break-all;word-wrap: break-word;white-space:pre-wrap;max-width: 95px'>" + "{b} " + "</div>"
        },
        series: [{
          type: 'graph', // 声明绘制关系图
          layout: 'force', // 声明绘制关系图中的力导向图
          symbolSize: (value, params) => {
            switch (params.data.level) {
              case 0:
                return 75;
              case 1:
                return 60;
              case 2:
                return 50;
              default:
                return 45;
            }
          },
          itemStyle: {
            normal: {
              shadowBlur: 4,
              color: (params) => {
                switch (params.data.level) {
                  case 0:
                    return 'purple';
                  case 1:
                    return 'red';
                  case 2:
                    return 'blue';
                  case 3:
                    return 'green';
                  default:
                    return 'black';
                }
              },
            }
          },
          lineStyle: { //==========关系边的公用线条样式。
            normal: {
              color: 'rgba(77,50,77,0.4)',
              width: '2.4',
              type: 'solid', //线的类型 'solid'（实线）'dashed'（虚线）'dotted'（点线）
              curveness: 0.27, //线条的曲线程度，从0到1
              opacity: 0.8,
              shadowBlur: 10,
              shadowColor: 'red',
              // 图形透明度。支持从 0 到 1 的数字，为 0 时不绘制该图形。默认0.5
            },
            emphasis: {//高亮状态
              opacity: 1,
              width: '3.2',
            }
          },
          draggable: true, // 节点是否可拖拽
          roam: true,  // 是否开启鼠标缩放和平移漫游
          focusNodeAdjacency: true, // 是否在鼠标移到节点上的时候突出显示节点以及节点的边和邻接节点
          edgeSymbol: ['', ''],
          cursor: 'pointer',
          emphasis: { //  鼠标悬浮高亮图形的样式
            itemStyle: {
              borderColor: '#bd99f6',
              borderWidth: 2,
              borderType: 'solid',
              symbolSize: 40,
            },

          },
          edgeLabel: { // 设置连线label样式
            normal: {
              show: true,
              textStyle: {
                fontSize: 14,
                color: '#000'
              },
              formatter(x) {
                return x.data.name;
              }
            }
          },
          grid: { // 让图表占满容器
            top: "0px",
            left: "0px",
            right: "0px",
            bottom: "0px"
          },
          label: { // 节点label设置
            show: true,
            position: 'inside',
            fontSize: 15,
            color: '#fff',
            bold: true,
            formatter: (record) => {
                if (record.name.length > 10) {
                  return record.name.substr(0, 5) + '...'
                } else {
                  return record.name
                }
              }
          },
          force: { // 力引导布局相关的配置项
            repulsion: 110, // 节点之间的斥力因子
            gravity: 0.03, // 节点受到的向中心的引力因子 越大越往中心靠拢
            edgeLength: [230, 200], // 边的两个节点之间的距离
            layoutAnimation: true, // 显示布局的迭代动画
          },
          nodes: this.graphNodes,  // 节点数据列表
          links: this.graphLinks, // 关系数据列表
        }]
      })
      myChart.on('click', function (param) {
        // console.log(param)
        var nodeName = param.data.name
        that.selectedNodeName = nodeName
        console.log(nodeName)
      })
      myChart.on('contextmenu', function (params) {
        console.log(params)
        if (params.dataType === 'node') {
          that.selectedNodeName = params.data.name
          console.log(that.selectedNodeName)
          that.contextmenu = true
          // 去掉悬停
          that.$refs.main.children[1].style.display = 'none'
          that.$refs.rightMenu1.style.display = 'none';
          that.$refs.rightMenu.style.display = 'block';
          // // //让自定义菜单随鼠标的箭头位置移动
          that.$refs.rightMenu.style.left = params.event.offsetX + 45 + 'px'
          that.$refs.rightMenu.style.top = params.event.offsetY + 45 + 'px'
        } else {
          that.selectedSource = params.data.source
          that.selectedTarget = params.data.target
          that.contextmenu1 = true
          // 去掉悬停
          that.$refs.main.children[1].style.display = 'none'
          that.$refs.rightMenu.style.display = 'none';
          that.$refs.rightMenu1.style.display = 'block';
          // // //让自定义菜单随鼠标的箭头位置移动
          that.$refs.rightMenu1.style.left = params.event.offsetX + 120 + 'px'
          that.$refs.rightMenu1.style.top = params.event.offsetY + 40 + 'px'
        }

      });
      console.log("graph built.")
    },
    rebuildChart: function () {
      console.log("rebuilding graph...")
      var params = new URLSearchParams();
      params.append('username', this.username)
      API({
        url: '/read_graph/',
        method: 'get',
        params: params
      }).then((res) => {
        console.log(res.data)
        console.log(res.data.nodes)

        var nodes = []
        for (var i in res.data.nodes) {
          nodes.push({
            name: res.data.nodes[i].fields.knowledgeName,
            level: res.data.nodes[i].fields.relation
          })
        }
        var links = []
        for (var j in res.data.links) {
          links.push({
            source: res.data.links[j].fields.source,
            target: res.data.links[j].fields.target,
            name: res.data.links[j].fields.name
          })
        }
        this.graphNodes = nodes
        this.graphLinks = links
        this.setChartsOn()
      })
    },
    delNode: function () {
      var data = {}
      data['del_node'] = this.selectedNodeName
      data['username'] = this.username
      API({
        url: '/del_node/',
        method: 'post',
        data: (Qs.stringify(data))
      }).then((res) => {
        console.log(res)
        this.$refs.rightMenu.style.display = 'none';
        this.rebuildChart()
      })
    },
    delLine: function () {
      var data = {}
      data['source'] = this.selectedSource
      data['target'] = this.selectedTarget
      data['username'] = this.username
      API({
        url: '/del_line/',
        method: 'post',
        data: (Qs.stringify(data))
      }).then((res) => {
        console.log(res)
        this.$refs.rightMenu1.style.display = 'none';
        this.rebuildChart()
      })
    }
  },
  components: {
    AddSelf,
    AddNode,
    TabCard,
  },
  data() {
    return {
      graphLinks: [{
        source: '存储设备2',
        target: '服务器',
        name: '数据传输'
      }, {
        source: '存储设备1',
        target: '服务器',
        name: '数据传输'
      },
        {
          source: '服务器',
          target: '防火墙',
          name: '访问'
        },
        {
          source: '防火墙',
          target: '网络设备1',
          name: '访问'
        },
        {
          source: '防火墙',
          target: '网络设备2',
          name: '访问'
        }
      ],
      graphNodes: [{
        name: '服务器',
        level: 0
      },
        {
          name: '存储设备1',
          level: 1
        },
        {
          name: '存储设备2',
          level: 1
        },
        {
          name: '防火墙',
          level: 1
        },
        {
          name: '网络设备1',
          level: 2
        },
        {
          name: '网络设备2',
          level: 2
        }
      ],
      contextmenu: false,
      addNodeDisplay: false,
      addSelfDisplay: false,
      tabCardDisplay: true,
      selectedNodeName: 'GGG',
      selectedSource: '',
      selectedTarget: '',
      contextmenu1: false,
    }
  },
  mounted() {
    this.rebuildChart()
    this.setChartsOn()
  },
  // watch: {
  //   graphLinks: {
  //     deep: true,
  //     handler: function (newV) {
  //       this.setChartsOn()
  //     }
  //   },
  //   graphNodes: {
  //     deep: true,
  //     handler: function (newV) {
  //       this.setChartsOn()
  //     }
  //   },
  // }
}
</script>

<template>
  <div id="main" ref="main" style="height: 600px" @contextmenu.prevent="" @click="mainClick"></div>
  <div ref="rightMenu" class="menu" style="display: none;">
    <ul>
      <li @click="addNode">添加关联节点</li>
      <li @click="delNode">删除节点</li>
      <li @click="addSingle">添加孤立节点</li>
    </ul>
  </div>
  <div ref="rightMenu1" class="menu" style="display: none;">
    <ul>
      <li @click="delLine">删除边</li>
    </ul>
  </div>
  <AddNode v-show="addNodeDisplay === true"
           style="position: absolute; right: 6%; bottom: 8%; z-index: 9"
           :selected=selectedNodeName
           :username=username
           @hideCard="addNodeDisplay=!addNodeDisplay"
           @rebuild="rebuildChart"></AddNode>
  <AddSelf v-show="addSelfDisplay === true"
           style="position: absolute; right: 4%; bottom: 18%; z-index: 9"
           :username=username
           @hideCard="addSelfDisplay=!addSelfDisplay"
           @rebuild="rebuildChart"></AddSelf>
  <TabCard v-show="tabCardDisplay === true"
           style="position: absolute; right: 4%; top: 8%; z-index: 8;"
           @hideCard="tabCardDisplay=!tabCardDisplay"></TabCard>
</template>

<style>
.menu {
  position: absolute;
  background: rgba(168, 234, 222, 0.93);
  border-radius: 5px;
  left: -99999px;
  top: -99999px;
}

.menu ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

.menu ul li {
  cursor: pointer;
  padding: 5px 10px;
  color: #000000;
  border-bottom: 1px dashed #a9a9a9;
  font-size: 14px;
}

.menu ul li:last-child {
  border-bottom: none;
}
</style>
