git命令
=======

.. highlight:: bash


配置::

    # 查看全局配置
    git config --global --list
    # 查看仓库配置
    git config --local --list
    # 配置全局用户名邮箱
    git config --global user.name "☘"
    git config --global user.email "kogawananari@gmail.com"
    # 配置仓库用户名邮箱
    git config --local user.name "☘☘"
    git config --local user.email "☘☘☘☘☘☘☘☘☘☘☘☘☘☘"
    # 全局代理
    git config --global http.proxy http://127.0.0.1:7890
    git config --global https.proxy http://127.0.0.1:7890
    # 取消全局代理：
    git config --global --unset http.proxy
    git config --global --unset https.proxy
    # 清除配置中纪录的用户名和密码，往後提交代码时会让重新输入账号密码
    git config --system --unset credential.helper
    # 使用後下次pull或push时会缓存输入的用户名和密码
    git config --global credential.helper store



拉取::

    # 克隆
    git clone http://10.10.10.101/☘☘☘☘/☘☘☘☘.git


切分支::
    
    # 查看本地分支
    git branch
    # 创建本地分支
    git branch 本地名
    # 删除本地分支
    git branch -d 本地名
    # 查看远程分支
    git branch -a
    # 删除远程分支
    git push origin -d 远程名
    # 创建本地分支并切换到
    git checkout -b 本地名
    # 创建本地空白分支并切换到
    git switch --orphan
    # 远程分支拉到本地 并切换到
    git checkout -b 本地名 origin/远程名
    # 本地切换分支
    git checkout 本地名
    # 刷新远程分支
    git remote update origin -p


提交::
    
    # 暂存更改
    git add .
    # 提交（--no-verify ：绕过规则）
    git commit -m 'fix' --no-verify
    # 获取分支最新
    git pull
    # 推送所有分支提交
    git push --all origin
    # 強制推送master分支提交
    git push origin master --force
    # 暫存所有修改 附加描述
    git stash save "114514"
    # 強制放棄本地分支歷史 使用遠端的替換 適用於遠端存在rebase, 記得前後暫存修改
    git fetch
    git reset --hard origin/远程名
    # 釋放暫存的修改
    git stash pop


回滚::

    # 查看本地分支提交以及合并记录
    git reflog
    # 回滚到某次记录后
    git reset --hard 编号
    # 重寫之前三次的提交 將之後兩個改成f/s可以合併提交 rebase之後需要強制推送
    git rebase -i HEAD~3
    # 重寫之前所有的提交
    git rebase -i --root
    # 重寫某次提交之後的所有的提交
    git rebase -i 114dec5ed1419a810e
    # 强制推送
    git push origin 远程名 --force