
# This is a bash file to help you build the project
#This will create the binary and place it in the /usr/bin folder and set the environment variable so you only need to write Linecounter in your terminal


pip install pyinstaller

pyinstaller --onefile ./src/main.py

cp ./dist/main ./Linecounter
sudo cp ./dist/main /usr/bin/Linecounter

export Linecounter=/user/bin/Linecounter 

echo "Thank you for installing Linecounter"
