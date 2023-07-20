<template>
  <div id='graph' class='hoverWarp'>
    <svg :id='id' :width='width' :height='height'></svg>

    <div id='tooltip' class='hidden'>
      <p><strong>状态参数</strong></p>
      <p>
        <span id='position'></span> <br/>
        <span id='jointAngle'></span>
      </p>
    </div>
  </div>
  <div id="app">
    <div id="graph">

    </div>
  </div>
</template>

<script>
import * as d3 from 'd3'

export default {
  emits: ['changeCardDisplay'],
  methods: {
    changeCard: function () {
      this.$emit("changeCardDisplay");
    },
    init() {
      console.log('init')

      let marge = {top: 60, bottom: 60, left: 60, right: 60}
      let width = this.width ? this.width : 900
      let height = this.height ? this.height : 600

      // 重新加载
      d3.selectAll('#graph svg > *').remove()
      let svg = d3.selectAll('svg')

      let g = svg
          .append('g')
          .attr('transform', `translate(${marge.top}, ${marge.left})`)

      // 准备数据
      // 节点集
      let nodes = this.my_nodes
      // 边集
      let edges = this.my_edges

      // 新建一个力导向图
      let forceSimulation = d3
          .forceSimulation(nodes) // 新建一个力模拟器，但是没有任何力的作用 调用force方法来生成力
          .force('link', d3.forceLink().links(edges).distance(200)) // 连线导致的引力
          .force('charge', d3.forceManyBody().strength(-500)) // 斥力
          .force(
              'center',
              d3.forceCenter().x(width / 2).y(height / 2)
          ) // 确定模拟图的中心
          .on('tick', ticked) // 如何随时间变化

      // 绘制边
      let links = g
          .append('g')
          .selectAll('line')
          .data(edges)
          .enter()
          .append('line')
          .attr('stroke', 'gray')
          .attr('stroke-width', 1)

      // 边上的文字
      let linksText = g
          .append('g')
          .selectAll('text')
          .data(edges)
          .enter()
          .append('text')
          .text((d) => `[${d.parameter}]`)

      // 创建分组
      let gs = g
          .selectAll('.circleText')
          .data(nodes)
          .enter()
          .append('g')
          .attr('transform', (d) => `translate(${d.x}, ${d.y})`)
          .call(
              d3.drag().on('start', started).on('drag', dragged).on('end', ended)
          )

      // 绘制节点
      gs.append('circle')
          .attr('r', 25)
          .attr('fill', '#D9C8AE')
          .attr('stroke', '#c0a378')
          .attr('stroke-width', 2)

      // 文字
      gs.append('text')
          .attr('x', -10)
          .attr('y', 5)
          .attr('fill', 'white')
          .text((d) => d.name)

      // hover
      gs.on('mouseover', function (event, d) {
        let xPosition = event.pageX + 10
        let yPosition = event.pageY + 10

        console.log(xPosition, yPosition)

        // 显示div标签信息
        let tooltip = d3
            .select('#tooltip')
            .style('opacity', 1)
            .style('left', xPosition + 'px')
            .style('top', yPosition + 'px')

        // 设置div标签内容
        tooltip.select('#jointAngle').text(`关节角: ${d.jointAngle}`)
        tooltip.select('#position').text(`位置: ${d.position}`)

        d3.select('#tooltip').classed('hidden', false)
      })

      // leave
      gs.on('mouseleave', function (event, d) {
        d3.select('#tooltip').classed('hidden', true)
      })

      // ticked 表示力导向图如何随时间变化
      function ticked() {
        links
            .attr('x1', (d) => d.source.x)
            .attr('y1', (d) => d.source.y)
            .attr('x2', (d) => d.target.x)
            .attr('y2', (d) => d.target.y)

        linksText
            .attr('x', (d) => (d.source.x + d.target.x) / 2)
            .attr('y', (d) => (d.source.y + d.target.y) / 2)

        gs.attr('transform', (d) => `translate(${d.x}, ${d.y})`)
      }

      // drag
      function started(event, d) {
        if (!event.active) {
          // 设置衰减系数，对节点位置移动过程的模拟，数值越高移动越快，数值范围[0, 1]
          forceSimulation.alphaTarget(0.8).restart()
        }
        d.fx = d.x
        d.fy = d.y
      }

      function dragged(event, d) {
        d.fx = event.x
        d.fy = event.y
      }

      function ended(event, d) {
        if (!event.active) {
          forceSimulation.alphaTarget(0)
        }
        d.fx = null
        d.fy = null
      }
    },
    highlightNode(node) {
      console.log('highlightNode', node)
      // 还原原本的颜色
      d3.selectAll('circle').attr('fill', '#D9C8AE')

      //画新颜色
      let highlightNode = d3.selectAll('circle').filter((d) => node.nodesInPath.includes(d.name))
      highlightNode.attr('fill', '#66ccff')
    },

    cleanNode() {
      d3.selectAll('circle').attr('fill', '#D9C8AE')
    }
  },
  props: {
    id: String,
    width: String,
    height: String,
    nodes: Array,
    edges: Array
  },
  data() {
    return {
      my_nodes: this.nodes,
      my_edges: this.edges
    }
  },
  mounted() {
    this.my_nodes = this.nodes
    this.my_edges = this.edges

    //this.init()
    console.log('重新加载啦')
  },
  watch: {
    // 监听节点和边的变化，每当node变化时更新组件
    nodes() {
      this.my_nodes = this.nodes
      this.my_edges = this.edges

      //this.init()
    }
  },

}
</script>


<style scoped>
#tooltip {
  position: absolute;
  width: 200px;
  height: auto;
  padding: 10px;
  background-color: white;

  -webkit-border-radius: 10px;
  -moz-border-radius: 10px;
  border-radius: 10px;

  -webkit-box-shadow: 4px 4px 10px rgba(0, 0, 0, 0.4);
  -moz-box-shadow: 4px 4px 10px rgba(0, 0, 0, 0.4);
  box-shadow: 4px 4px 10px rgba(0, 0, 0, 0.4);

  pointer-events: none;
}

#tooltip.hidden {
  display: none;
}

#tooltip p {
  margin: 0;
  font-family: sans-serif;
  font-size: 16px;
  line-height: 20px;
}
</style>
