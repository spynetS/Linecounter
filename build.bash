
# This is a bash file to help you build the project
#This will create the binary and place it in the /usr/bin folder and set the environment variable so you only need to write Linecounter in your terminal

command -v python3 >/dev/null 2>&1 || { 
    sudo apt-get update
    sudo apt-get install python3.6
 }

command -v python >/dev/null 2>&1 || { 
    sudo apt update
    sudo apt install python3-pip
 }



pip install pyinstaller

pyinstaller --onefile ./src/main.py

sudo cp ./dist/main /usr/bin/linecounter

export linecounter=/user/bin/linecounter 

echo "Thank you for installing Linecounter"
