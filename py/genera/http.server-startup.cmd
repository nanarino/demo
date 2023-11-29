title http.server
@echo off
set /p port=input port:
if not defined port set port=80
py -m http.server %port%
