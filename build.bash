
# This is a bash file to help you build the project
#This will create the binary and place it in the /usr/bin folder and set the environment variable so you only need to write Linecounter in your terminal

installPy ()
{
    echo "Do you want to install python 3? (y/n)"
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

PYINSTALLER=$(sudo find / -xdev -name "pyinstaller")

$PYINSTALLER --onefile ./src/main.py

sudo cp ./dist/main /usr/bin/linecounter

export linecounter=/user/bin/linecounter 

echo "Thank you for installing Linecounter"
