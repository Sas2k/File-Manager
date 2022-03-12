# File Manager 📁
Version 3.1.0

A simple cli based File Manager

## Badges

[![Run on Repl.it](https://repl.it/badge/github/Sas2k/File-Manager)](https://repl.it/github/Sas2k/File-Manager)

![GitHub all releases](https://img.shields.io/github/downloads/sas2k/File-Manager/total)

[![Python File Test](https://github.com/Sas2k/File-Manager/actions/workflows/main.yml/badge.svg)](https://github.com/Sas2k/File-Manager/actions/workflows/main.yml)

## Documentation

### commands

|  command       |  description                   |
|:----------     | :-------------                 |
|`create file`   | creates a file                 | 
|`delete file`   | deletes a file                 |
|`read file`     | reads a file                   | 
|`edit file`     | edits a file                   |
|`help`          | displays the help message      |
|`exit`          | exits the program              |
|`create folder` | creates a folder               |
|`delete foler`  | deletes a folder               | 
|`list files`    | list the files in a directory  |
|`list paths`    | list the paths in a directory  |
|`set paths`     | sets the path for the manager  |
|`show path`     | shows the path your working on |
|`show history`  | shows the the commands you used|
|`settings`      | settings

NOTE:File_Manager's default path is the current place it id downloaded

### Edit commands
|  command       |  description                 |
|:----------     | :-------------               |
|`<n>`           | takes a new line             |

### cli-commands [V2.0.0(and newer) Feature]
#### How to use cli command
##### Source Code
Firstly change your directory in your cli to the place you<br>downloaded the file manager source code
```cmd
C:>Users/user>cd path/to/file
C:path/to/file>Python -m 'File Manager.py' <put the flags here>
```
##### EXE (x64)
Firstly read the installation section then come here;
Hello Welcome back now that you have read the installation section <br>Now let's get started
```cmd
C:/Users/user>file_Manager <flag here>
```

|  flag/command       |  description                             |
|:----------          | :-------------                           |
|`-list`              | lists the files in the current directory |
|`-curname`           | Displays the current directory name      |
|`-curpath`           | Displays the current directory path      |
|`-cfile`             | creates a file                           |
|`-dfile`             | deletes a file                           |
|`-h` or `-help`      | displays help                            |

## Installation

### Source Code

click on the "Version x.x.x" Tag from releases from that it will be downloaded <br>
then on your command line change the directory to the place where you downloaded it <br>
Then install the requirements with the command below;

CMD
```cmd
    pip install -r requirements.txt
```

Bash
```bash
    $ python -m pip install -r requirements.txt
```
Then run the file with this commmand;
```cmd
    python Main.py
```
Or;

You can just unzip the file [if you haven't already done it at the start of the process]<br> and double click/run it with python😏

### Windows (x64)

[The EXE File is in the bin file and the release section]
The `File_Manager.exe` file can be found when you unzip source code [sorry 😅] or by going to the code section and click the File_Manager.exe file and<br>click downloaded<br>
also you might want to add the folder where the .exe is intalled to path then;

```cmd
File_Manager -h
```
if you get the output of this;

```cmd
usage: File_Manager.exe [-h] [-list] [-curname] [-curpath] [-cfile] [-dfile]

options:
  -h, --help  show this help message and exit
  -list       lists the files in the current directory
  -curname    Displays the current directory name
  -curpath    Displays the current directory path
  -cfile      creates a file
  -dfile      Deletes a file
```
Then you have correctly setted up the file manager.
