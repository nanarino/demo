# 请确保在运行脚本之前已经安装了Chocolatey
# install OTP/elixir
choco install elixir -y

# add elixir in PATH
$elixirPath = "C:\ProgramData\chocolatey\lib\Elixir\tools\bin"
$env:Path = [System.Environment]::GetEnvironmentVariable("PATH", "Machine")
$env:Path += ";$elixirPath"
[System.Environment]::SetEnvironmentVariable("PATH", $env:Path, "Machine")
