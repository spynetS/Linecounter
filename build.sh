#!/usr/bin/env sh

echo "Installs at /usr/bin"
sudo install -Dm644 ./src/fileReader.py "/usr/bin/fileReader.py"
sudo install -Dm644 ./src/printer.py "/usr/bin/printer.py"
sudo install -Dm755 ./src/main.py "/usr/bin/lctr"
