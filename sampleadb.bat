@echo off

for /F %%i in (devices.txt) do adb -s %%i shell getprop ro.build.version.release