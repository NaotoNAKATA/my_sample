@echo off
SETLOCAL enabledelayedexpansion

set PATH=%PATH%;C:\Program Files\CMake\bin
set PATH=%PATH%;C:\Program Files (x86)\MSBuild\14.0\Bin

set VisualStudio="Visual Studio 14 Win64"
rem	set OpenCV="C:\opencv\opencv-3.2.0\build"

set BUILD=build
set PRJ=ProjectMain.sln
set OBJ=main.exe
set CONFIG=Release
set PLAT=x64

if not exist %BUILD% (
	mkdir %BUILD%
	cd %BUILD%
	cmake .. -G %VisualStudio%
rem	cmake .. -G %VisualStudio% -DCMAKE_PREFIX_PATH=%OpenCV%
	cd ..
)

echo.
set /P STR="(1/Build : 2/Rebuild : 3/Clean) : "

if %STR%==1 (
	MSBuild.exe %BUILD%\%PRJ% /t:Build /p:Configuration=%CONFIG% /p:platform=%PLAT%
	xcopy /Y %BUILD%\%CONFIG%\%OBJ%
) else if %STR%==2 (
	MSBuild.exe %BUILD%\%PRJ% /t:Rebuild /p:Configuration=%CONFIG% /p:platform=%PLAT%
	xcopy /Y %BUILD%\%CONFIG%\%OBJ%
) else if %STR%==3 (
	if exist %OBJ% ( del /Q %OBJ%)
	MSBuild.exe %BUILD%\%PRJ% /t:Clean /p:Configuration=%CONFIG% /p:platform=%PLAT%
) else (
	echo %STR%" : No Action"
)

pause

exit /b

