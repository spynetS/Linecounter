# Linecounter
Linecounter is a simple python program to count your lines of your source code in your project

Use
//Linux
After cloning the project run the build.bash
this will install the binarys in the /user/bin folder
Then just call Linecounter in your terminal

# Linecounter

Linecounter is a simple python program to count your lines of your source code in your project

## Description

Linecounter is a small python program that helps you count the amount of lines in your source code (it works on any files) 

## Getting Started

### Dependencies

* Windows, Linux, Mac

### Installing
###Linux
[Download](https://github.com/spynetS/Linecounter.git) the src code and and run the build.bash file
This will create the binarys and place them in the /usr/bin folder and set the environment variable
so you only need to write Linecounter in your terminal

### Executing program

* List the total lines in all files and subfolders
```
Linecounter -l
```
* List the total lines in all files and subfolders with curtain file extensions
```
Linecounter -l -su .py .txt
```
* List all files with their linecounts in all files and subfolders
```
Linecounter -lf
```
* List all files with their linecounts in all files and subfolders with curtain file extensions
```
Linecounter -lf -su .py .txt
```
* Set starting folder 
```
Linecounter -lf -p ../src -su .py .txt
```

## Help



## Authors

Contributors names and contact info

* [spynetsS](https://github.com/spynetS)
  
## Version History


* 0.1
    * Initial Release

## License

This project is licensed under the [MIT] License - see the LICENSE.md file for details

## Acknowledgments

