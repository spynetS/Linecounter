
:: This is a bash file to help you build the project

SET mypath=%~dp0
echo %mypath:~0,-1%

if not "%1"=="am_admin" (powershell start -verb runas '%0' am_admin & exit /b)

CD %mypath:~0,-1%

pip install pyinstaller

pyinstaller --onefile ./src/main.py
mkdir %HOMEPATH%\Linecounter\
copy .\dist\main.exe %HOMEPATH%\Linecounter\Linecounter.exe

setx /M Linecounter "%path%;%HOMEDRIVE%%HOMEPATH%\Linecounter\"

echo "Installation at %HOMEPATH%\Linecounter\ completed"
echo "Thank you for installing Linecounter!"
pause
