echo off
SETLOCAL enabledelayedexpansion

echo %~d0
echo %~p0
echo %~n0
echo %~x0

cd %~dp0

SET CSV=%1

SET FILT="[0:v]setpts=PTS-STARTS,scale=640x480[v0];[1:v]setpts=PTS-STARTS,scale=640x480[v1];[v0][v1]hstack"

for /f "delims=',', tokens=1-3" %%a in (%CSV%) do (
	SET OUT=%%a
	SET COL2=%%b
	SET COL3=%%c
	
rem	ffmpeg.exe -i !COL2! -i !COL3! -filter_complex !FILT! -r 10 -vb 3000k !OUT!
)

pause

exit /b

