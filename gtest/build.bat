echo off
SETLOCAL enabledelayedexpansion

set PATH=%PATH%;C:\Program Files\CMake\bin
set PATH=%PATH%;C:\Program Files (x86)\MSBuild\14.0\Bin

set VisualStudio="Visual Studio 14 Win64"

set BUILD=build
set PRJ=googletest-distribution.sln
set CONFIG=Release
set PLAT=x64

cd googletest-release-1.10.0

mkdir %BUILD%
cd %BUILD%
cmake .. -G %VisualStudio% -DCMAKE_INSTALL_PREFIX=..\..\gtest
cd ..


MSBuild.exe %BUILD%\%PRJ% /t:Build /p:Configuration=%CONFIG% /p:platform=%PLAT%
MSBuild.exe %BUILD%\INSTALL.vcxproj /t:Build /p:Configuration=%CONFIG% /p:platform=%PLAT%

pause

exit /b

