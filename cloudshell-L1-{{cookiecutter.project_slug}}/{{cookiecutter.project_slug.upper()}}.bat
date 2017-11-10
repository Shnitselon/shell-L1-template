@ECHO OFF
setlocal
set SERVER_FOLDER=C:\Program Files (x86)\QualiSystems\CloudShell\Server
set DRIVERS_FOLDER=%SERVER_FOLDER%\Drivers
set DRIVER_NAME=%~n0
set LOGS_PATH=%SERVER_FOLDER%\Logs\%DRIVER_NAME%
set DRIVER_ENV=%DRIVERS_FOLDER%\%DRIVER_NAME%
set PYTHON="%DRIVER_ENV%\Scripts\python"
set EXE=%PYTHON% "%DRIVER_ENV%\main.py"
set port=%1
if not defined port set port=4000
echo Starting driver %DRIVER_NAME%
echo Log Path %LOGS_PATH%
%EXE% %port% %LOGS_PATH%
endlocal