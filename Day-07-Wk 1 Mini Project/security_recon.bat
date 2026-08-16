REM Windows Security Recon Report
echo ==== SYSTEM INFO ==== > report.txt
systeminfo >> report.txt
echo. >> report.txt

echo ==== HOST NAME ==== >> report.txt
hostname >> report.txt
echo. >> report.txt

echo ==== CURRENT USER ==== >> report.txt
whoami >> report.txt
echo. >> report.txt

echo ==== ADMIN CHECK ==== >> report.txt
net localgroup administrators >> report.txt
echo. >> report.txt

echo ==== NETWORK CONFIG ==== >> report.txt
ipconfig >> report.txt
echo. >> report.txt

echo ==== LISTENING PORTS ==== >> report.txt
netstat -ano | findstr LISTENING >> report.txt
echo. >> report.txt

echo ==== RUNNING PROCESSES ==== >> report.txt
tasklist >> report.txt
echo. >> report.txt

echo ==== REPORT COMPLETE ==== >> report.txt
echo Report saved ad report.txt