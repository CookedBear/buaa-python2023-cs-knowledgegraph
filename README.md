# 协作流程与规范

1. 提出自己要完成、修改的内容或功能，发起新 issue，格式参考 #1
1. git pull 最新的仓库 `main` 分支，并从其上新建分支 `git checkout -b <branch-name>`
1. 提交：一个 commit 做一件事，一件事在一个 commit 中完成。如果需要修正之前的提交用 `git commit --amend`，不要创建很多个提交，如果已经推到远程推不上去加 `--force`。push 时注意先 `git push --set-upstream origin <branch-name>`
1. 发起新 pull request，格式参考 #2
1. 等网页转一下 CI，要是能直接合并就点 merge，不能合就 rebase 啥的修修冲突
1. 可能就这些

# 爬虫返回值

1. 所返回的都是字典类型变量
2. 字典的`key`为排序方式`(str)`，`value`为课程的具体数据`(list)`。其中key为`default`表示爬虫默认所获取的顺序

## 课程可能的返回值：

### bilibili

- 默认排序`default`
- 名称`name`
- 播放量`plays`

### icourse163

- 默认排序`default`
- 名称`name`
- 学习人数`plays`

### icourses

- 默认排序`default`
- 名称`name`
- 学校`school`

### imooc

- 默认排序`default`
- 名称`name`
- 学习人数`plays`

### cnmooc

- 默认排序`default`
- 名称`name`
- 学校`school`

## 以下三个为其他在线课程网站（作业要求之外）：

### xuetangx

- 默认排序`default`
- 名称`name`
- 学习人数`plays`

### cmooc

- 默认排序`default`
- 名称`name`
- 热度`plays`
  
### study163

- 默认排序`default`
- 名称`name`
- 学习人数`plays`
  
