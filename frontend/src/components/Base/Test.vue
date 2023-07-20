<script>
import * as echarts from "echarts";


export default {
  methods: {
    mainClick: function () {
      this.contextmenu = false
      this.$refs.rightMenu.style.display = 'none';
    }
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
      contextmenu: false
    }
  },
  mounted() {
    const that = this;
    var myChart = echarts.init(document.getElementById('main'));
    var option = {
      title: {
        text: 'ECharts 入门示例'
      },
      tooltip: {},
      legend: {
        data: ['销量']
      },
      xAxis: {
        data: ['衬衫', '羊毛衫', '雪纺衫', '裤子', '高跟鞋', '袜子']
      },
      yAxis: {},
      series: [
        {
          name: '销量',
          type: 'bar',
          data: [5, 20, 36, 10, 10, 20]
        }
      ]
    };
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
          repulsion: 120, // 节点之间的斥力因子
          gravity: 0.01, // 节点受到的向中心的引力因子 越大越往中心靠拢
          edgeLength: 240, // 边的两个节点之间的距离
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
  <div id="main" ref="main" style="height: 650px; width: 1300px" @contextmenu.prevent="" @click="mainClick"></div>
  <div ref="rightMenu" class="menu" style="display: none;">
    <ul>
      <li @click="">添加关联节点</li>
      <li>删除节点</li>
      <li>添加关系</li>
    </ul>
  </div>
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
