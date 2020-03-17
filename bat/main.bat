echo off
SETLOCAL enabledelayedexpansion

echo %~d0
echo %~p0
echo %~n0
echo %~x0

cd %~dp0

pause

exit /b

