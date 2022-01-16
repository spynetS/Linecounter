
# This is a bash file to help you build the project
# The file to start when build is done is the Linecounter that will appear in the source folder (not src)
# You might have to do chmod 755 ./build.bash to run this script

pip install pyinstaller

pyinstaller --onefile ./src/main.py

cp ./dist/main ./Linecounter
sudo cp ./dist/main /usr/bin/Linecounter

export Linecounter=/user/bin/Linecounter 

echo "Thank you for installing Linecounter"