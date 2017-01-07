echo off
SETLOCAL enabledelayedexpansion

set PATH=%PATH%;C:\Program Files\CMake\bin
set PATH=%PATH%;C:\Program Files (x86)\MSBuild\14.0\Bin

set VisualStudio="Visual Studio 14 Win64"
set OpenCV="C:\opencv\opencv-3.2.0\build"

if not exist build (
	mkdir build
	cd build
	cmake .. -G %VisualStudio% -DCMAKE_PREFIX_PATH=%OpenCV%
	cd ..
)

echo.
set /P STR="(1/Build : 2/Rebuild : 3/Clean) : "

if %STR%==1 (
	MSBuild.exe build\ProjectMain.sln /t:Build /p:Configuration=Release /p:platform=x64
	xcopy /Y build\Release\main.exe
) else if %STR%==2 (
	MSBuild.exe build\ProjectMain.sln /t:Rebuild /p:Configuration=Release /p:platform=x64
	xcopy /Y build\Release\main.exe
) else if %STR%==3 (
	if exist main.exe ( del /Q main.exe)
	MSBuild.exe build\ProjectMain.sln /t:Clean /p:Configuration=Release /p:platform=x64
) else (
	echo %STR%" : No Action"
)

pause

exit /b

