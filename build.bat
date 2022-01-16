
:: This is a bash file to help you build the project
:: The file to start when build is done is the Linecounter that will appear in the source folder (not src)
:: You might have to do chmod 755 ./build.bash to run this script

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
