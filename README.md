创建前后端交互示例，完成后端传输部分和数据库应用（使用原装 sqlite3），手动注册 api 进行传输。前端未完成。

需要确保电脑有 django（`pip install django`）和 vue（cd frontend + npm install）

运行时可以开两个 cmd：

- backend：`python manage.py runserver`
- frontend：`npm run dev`

现支持 api：

```
http://127.0.0.1:8000/api/add_node/       ---POST
http://127.0.0.1:8000/api/show_nodes/     ---GET
```

