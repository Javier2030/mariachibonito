#!/bin/bash
# uso: meas_est.sh "query" [start]
export WSL_INTEROP=/run/WSL/1544_interop
PS=/mnt/c/Windows/System32/WindowsPowerShell/v1.0/powershell.exe
WS="ws://localhost:9333/devtools/page/AFC262ECBF628F1FE85759A856A82214"
Q=$(python3 -c "import urllib.parse,sys;print(urllib.parse.quote(sys.argv[1]))" "$1")
S=${2:-0}
URL="https://www.google.com/search?q=${Q}&hl=es&gl=co&num=10&start=${S}&pws=0"
cd /mnt/c/temp || exit 1
$PS -NoProfile -ExecutionPolicy Bypass -File cdp_driver.ps1 -Action nav -TabWs "$WS" -Url "$URL" -WaitMs 6000 -OutputFile C:/temp/est_nav.txt >/dev/null 2>&1
$PS -NoProfile -ExecutionPolicy Bypass -File cdp_driver.ps1 -Action eval -TabWs "$WS" -JsFile C:/temp/serp_full_day.js -OutputFile C:/temp/est_out.txt >/dev/null 2>&1
sed 's/^\xef\xbb\xbf//' /mnt/c/temp/est_out.txt
echo
