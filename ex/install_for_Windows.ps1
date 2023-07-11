# 安装Elixir 请确保在运行脚本之前已经安装了Chocolatey
choco install elixir -y

# 添加Elixir和Erlang路径到环境变量
$elixirPath = "C:\ProgramData\chocolatey\lib\Elixir\tools\bin"
$erlangPath = "C:\Program Files\Erlang OTP\bin"
$envPath = [System.Environment]::GetEnvironmentVariable("PATH", "Machine")
$envPath += ";$elixirPath;$erlangPath"
[System.Environment]::SetEnvironmentVariable("PATH", $envPath, "Machine")

Write-Host "安装完成！请重新打开命令提示符以使更改生效。"