@echo off
adb shell getevent /dev/input/event1 | ts "%Y-%m-%d %H:%M:%.S" > event.log