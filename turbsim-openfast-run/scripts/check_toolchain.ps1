$ErrorActionPreference = "Stop"

$openFast = "C:\Users\15382\Desktop\Wind\CL_ROSCO\references\OpenFAST.exe"
$turbSim = "C:\Users\15382\Desktop\Wind\CL_ROSCO\references\openfast-5.0.0\reg_tests\r-test\glue-codes\openfast\5MW_Baseline\Wind\TurbSim.exe"
$downloadedDiscon = "C:\Users\15382\Desktop\Wind\CL_ROSCO\references\DISCON.dll"
$checkoutDiscon = "C:\Users\15382\Desktop\Wind\CL_ROSCO\references\ROSCO\rosco\lib\libdiscon.dll"
$python = "C:\Users\15382\anaconda3\envs\StudyPyTorch\python.exe"

$required = @($openFast, $turbSim, $downloadedDiscon, $checkoutDiscon, $python)
$missing = @($required | Where-Object { -not (Test-Path -LiteralPath $_ -PathType Leaf) })
if ($missing.Count -gt 0) {
    throw "Missing required files: $($missing -join ', ')"
}

$openFastText = (& $openFast -v 2>&1 | Out-String)
$turbSimText = (& $turbSim /h 2>&1 | Out-String)
$cudaText = (& $python -c "import json, torch; print(json.dumps({'torch': torch.__version__, 'cuda': torch.cuda.is_available(), 'device': torch.cuda.get_device_name(0) if torch.cuda.is_available() else None}))" | Out-String).Trim()

[pscustomobject]@{
    OpenFASTPath = $openFast
    OpenFASTVersion = ([regex]::Match($openFastText, "OpenFAST-v[^\r\n]+" )).Value
    OpenFASTSHA256 = (Get-FileHash -LiteralPath $openFast -Algorithm SHA256).Hash
    TurbSimPath = $turbSim
    TurbSimVersion = ([regex]::Match($turbSimText, "TurbSim-v[^\r\n]+" )).Value
    TurbSimSHA256 = (Get-FileHash -LiteralPath $turbSim -Algorithm SHA256).Hash
    DownloadedControllerPath = $downloadedDiscon
    DownloadedControllerSHA256 = (Get-FileHash -LiteralPath $downloadedDiscon -Algorithm SHA256).Hash
    DownloadedControllerROSCOApproved = $false
    CheckoutControllerPath = $checkoutDiscon
    CheckoutControllerSHA256 = (Get-FileHash -LiteralPath $checkoutDiscon -Algorithm SHA256).Hash
    CheckoutControllerROSCOApproved = $false
    ControllerStatus = "Both DLLs accept a missing DISCON.IN; obtain or build a verified ROSCO library."
    PythonPath = $python
    PythonRuntime = ($cudaText | ConvertFrom-Json)
} | ConvertTo-Json -Depth 4
