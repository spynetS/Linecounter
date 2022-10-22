
# This is a bash file to help you build the project
#This will create the binary and place it in the /usr/bin folder and set the environment variable so you only need to write Linecounter in your terminal

installPy ()
{
	echo "It seems you don't have python3. Do you want to install python3 (if you know you have python3 press n)? (y/n)"
    read varname
    if [[ $varname = y* ]]
    then
        sudo apt update
        sudo apt install python3-pip
    fi
}

command -v python >/dev/null 2>&1 || {
    installPy

}
command -v python3 >/dev/null 2>&1 || {
    installPy
}


pip install pyinstaller

PYINSTALLER=$(sudo find / -xdev -name "pyinstaller" -print -quit)
#PYINSTALLER=pyinstaller
echo $PYINSTALLER

$PYINSTALLER --onefile ./src/main.py

sudo cp ./dist/main /usr/bin/lctr

export lctr=/user/bin/lctr
echo ""
echo ""
echo ""
echo "Thank you for installing Linecounter"
echo ""
echo ""
echo ""
