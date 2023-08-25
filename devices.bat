@echo off
adb devices -l | findstr "model:" > tmp.txt

setlocal EnableDelayedExpansion
set count=1
(
  for /F "tokens=1 delims= " %%A in (tmp.txt) do (
    set serial!count!=%%A
    set /a count+=1
  )
)

( 
  for /L %%i in (1,1,%count%) do (
    echo !serial%%i!
  )  
) > devices.txt

endlocal
del tmp.txt
rem Create temp file
copy devices.txt temp.txt >nul

rem Remove line and output to devices.txt
findstr /v "ECHO is off." temp.txt > devices.txt

rem Delete temp file
del temp.txt