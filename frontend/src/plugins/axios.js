import axios from 'axios'

// axios.defaults.headers['Content-Type'] = 'application/x-www-form-urlencoded; charset=UTF-8'
//使用axios下面的create([config])方法创建axios实例，其中config参数为axios最基本的配置信息。
const API = axios.create({

	timeout: 25000,                  //请求超时设置，单位ms
    headers: {'X-Requested-With': 'XMLHttpRequest'},
    baseURL: 'http://localhost:8000/api/'
})

//导出我们建立的axios实例模块，ES6 export用法
export default API
