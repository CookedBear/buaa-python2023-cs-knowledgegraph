<script>
import * as echarts from "echarts";
import AddNode from "@/components/Base/AddNode.vue"


export default {
  methods: {
    mainClick: function () {
      this.contextmenu = false
      this.$refs.rightMenu.style.display = 'none';
    },
    addNode: function () {
      // 显示卡片：节点名 + 级别；自带消失
      this.addNodeDisplay = true
      this.$refs.rightMenu.style.display = 'none';
    }
  },
  components: {
    AddNode
  },
  data() {
    return {
      graphLinks: [
        {
          source: 'BUAA',
          target: 'SCSE',
          name: ''
        },
        {
          source: 'BUAA',
          target: 'Python',
          name: ''
        },
        {
          source: 'BUAA',
          target: '上网不涉密',
          name: ''
        },
        {
          source: 'BUAA',
          target: '涉密不上网',
          name: ''
        },
        {
          source: 'SCSE',
          target: 'Python',
          name: ''
        },
        {
          source: 'Python',
          target: '上网不涉密',
          name: ''
        },
        {
          source: '上网不涉密',
          target: '涉密不上网',
          name: ''
        },
        {
          source: '涉密不上网',
          target: 'SCSE',
          name: ''
        },
      ],
      graphNodes: [{
        name: 'BUAA',
        level: 0
      },
        {
          name: 'SCSE',
          level: 1
        },
        {
          name: '上网不涉密',
          level: 1
        },
        {
          name: '涉密不上网',
          level: 1
        },
        {
          name: 'Python',
          level: 1
        }
      ],
      contextmenu: false,
      addNodeDisplay: false
    }
  },
  mounted() {
    const that = this;
    var myChart = echarts.init(document.getElementById('main'));
    // myChart.setOption(option);
    myChart.setOption({

      tooltip: {
        show: true,
        formatter: "<div style='display:block;word-break: break-all;word-wrap: break-word;white-space:pre-wrap;max-width: 80px'>" + "{b} " + "</div>"
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
            color: (params) => {
              switch (params.data.level) {
                case 0:
                  return 'red';
                case 1:
                  return 'blue';
                case 2:
                  return 'green';
                default:
                  return 'white';
              }
            },
          }
        },
        lineStyle: { //==========关系边的公用线条样式。
          normal: {
            color: 'rgba(77,50,77,0.4)',
            width: '2.1',
            type: 'solid', //线的类型 'solid'（实线）'dashed'（虚线）'dotted'（点线）
            curveness: 0.27, //线条的曲线程度，从0到1
            opacity: 0.8
            // 图形透明度。支持从 0 到 1 的数字，为 0 时不绘制该图形。默认0.5
          },
          emphasis: {//高亮状态
            opacity: 1,
            width: '2.8',
          }
        },
        draggable: true, // 节点是否可拖拽
        roam: true,  // 是否开启鼠标缩放和平移漫游
        focusNodeAdjacency: true, // 是否在鼠标移到节点上的时候突出显示节点以及节点的边和邻接节点
        edgeSymbol: ['', ''],
        cursor: 'pointer',
        emphasis: { //  鼠标悬浮高亮图形的样式
          itemStyle: {
            borderColor: 'black',
            borderWidth: 1,
            borderType: 'solid',
            symbolSize: 40,
          },
          label: {
            show: true,
            formatter: (record) => {
              if (record.name.length > 10) {
                return record.name.substr(0, 5) + '...'
              } else {
                return record.name
              }
            }
          }
        },
        edgeLabel: { // 设置连线label样式
          normal: {
            show: true,
            textStyle: {
              fontSize: 16,
              color: '#000'
            },
            formatter(x) {
              return x.data.name;
            }
          }
        },
        label: { // 节点label设置
          show: true,
          position: 'inside',
          color: '#fff',
          formatter: (record) => {
            console.log(record)
            return record.data.name
            // if (record.name.length > 10) {
            //   return record.name.substr(0, 5) + '...'
            // } else {
            //   return record.name
            // }
          }
        },
        force: { // 力引导布局相关的配置项
          repulsion: 11000, // 节点之间的斥力因子
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
      console.log(nodeName)
    })
    myChart.on('contextmenu', function (params) {
      // console.log('params', params)
      that.contextmenu = true
      // 去掉悬停
      that.$refs.main.children[1].style.display = 'none'
      that.$refs.rightMenu.style.display = 'block';
      // // //让自定义菜单随鼠标的箭头位置移动
      that.$refs.rightMenu.style.left = params.event.offsetX + 45 + 'px'
      that.$refs.rightMenu.style.top = params.event.offsetY + 45 + 'px'
    });
  },

}
</script>

<template>
  <div id="main" ref="main" style="height: 580px; width: 1300px" @contextmenu.prevent="" @click="mainClick"></div>
  <div ref="rightMenu" class="menu" style="display: none;">
    <ul>
      <li @click="addNode">添加关联节点</li>
      <li @click="delNode">删除节点</li>
      <li @click="addRelation">添加关系</li>
      <li @click="addSingle">添加孤立节点</li>
    </ul>
  </div>
  <AddNode v-show="addNodeDisplay === true" style="position: absolute; right: 4%; bottom: 18%; z-index: 9"
           @hideCard="addNodeDisplay=!addNodeDisplay"></AddNode>
</template>

<style>
.menu {
  /*这个样式不写，右键弹框会一直显示在画布的左下角*/
  position: absolute;
  background: rgba(168, 234, 219, 0.93);
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
