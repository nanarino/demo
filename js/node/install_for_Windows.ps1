# 先安装 pnpm
iwr https://get.pnpm.io/install.ps1 -useb | iex
# 延迟一段时间，以确保pnpm环境变量的更改生效
Start-Sleep -Seconds 5
# 安装 LTS 版本的 Node.js
pnpm env use --global lts