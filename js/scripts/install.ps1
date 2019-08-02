# install pnpm
iwr https://get.pnpm.io/install.ps1 -UseBasicParsing | Invoke-Expression

# update current process PATH environment variable
$env:PNPM_HOME = [System.Environment]::GetEnvironmentVariable("PNPM_HOME","User")
$env:Path += ";$env:PNPM_HOME"

# install Nodejs
pnpm env use --global lts
