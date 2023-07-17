# 协作流程与规范

1. 提出自己要完成、修改的内容或功能，发起新 issue，格式参考 #1
1. git pull 最新的仓库 `main` 分支，并从其上新建分支 `git checkout -b <branch-name>`
1. 提交：一个 commit 做一件事，一件事在一个 commit 中完成。如果需要修正之前的提交用 `git commit --amend`，不要创建很多个提交，如果已经推到远程推不上去加 `--force`。push 时注意先 `git push --set-upstream origin <branch-name>`
1. 发起新 pull request，格式参考 #2
1. 等网页转一下 CI，要是能直接合并就点 merge，不能合就 rebase 啥的修修冲突
1. 可能就这些