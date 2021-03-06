# Linecounter

Linecounter is a simple python program to count your lines of your source code in your project

## Description

Linecounter is a small python program that helps you count the amount of lines in your source code (it works on any files) 
 
 <a href="https://github.com/spynetS/Linecounter/blob/main/images/show1.png">
    <img src="images/show1.png" alt="Logo" height="500">
    <img src="images/show2.png" alt="Logo" height="300" >
  </a>


## Getting Started

### Dependencies
* Python3 (inlcuding pip)
* Windows, Linux, Mac

### Installing
* Linux

You can download it with yay from aur
```yay -S linecounter-git```
https://aur.archlinux.org/packages/linecounter-git

[Download](https://github.com/spynetS/Linecounter.git) the src code and and run the build.bash file
This will create the binary and place it in the /usr/bin folder and set the environment variable
so you only need to write lctr in your terminal

* Windows
[Download](https://github.com/spynetS/Linecounter.git) the src code and and run the build.bat file
This will create the binary and place it in the C:/User/user/Linecounter folder and create a environment varable (Linecounter)
that you have to copy the value and and adding it to the path varable

### Executing program

* List the total lines in all files and subfolders
```
lctr -l
```
* List the total lines in all files and subfolders with curtain file extensions
```
lctr -l -su .py .txt
```
* List all files with their linecounts in all files and subfolders
```
lctr -lf
```
* List all files with their linecounts in all files and subfolders with curtain file extensions
```
lctr -lf -su .py .txt
```
* Set starting folder 
```
lctr -lf -p ../src/ -su .py .txt
```
* Ignore filextensions 
```
lctr -lf -isu .py
```
* Ignore directory 
```
lctr -lf -id ./.git/
```
## Help



## Authors

Contributors names and contact info

* [spynetS](https://github.com/spynetS)
  
## Version History


* 0.1
    * Initial Release

## License

This project is licensed under the [MIT] License - see the LICENSE.md file for details

## Acknowledgments

