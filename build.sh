
# This is a bash file to help you build the project
#This will create the binary and place it in the /usr/bin folder and set the environment variable so you only need to write Linecounter in your terminal

pip install pyinstaller

python3 -m PyInstaller --onefile ./src/main.py

echo "Copy build files to /usr/bin/ ?"
sudo cp ./dist/main /usr/bin/lctr

export lctr=/user/bin/lctr
echo ""
echo ""
echo ""
echo "Thank you for installing Linecounter"
echo ""
echo ""
echo ""
