import argparse
import os
import sys
import time
# *Git Repo is intialized
import blessed

parser = argparse.ArgumentParser()

global Path
Path = os.getcwd() + '\\'
history = []
ani = '[==============]'
term = blessed.Terminal()
run = True
x = 0
help_message = """
#=============================================#
#+++++++++++++++++++++HELP++++++++++++++++++++#
#=============================================#
#  commands | description                     #
#1.edit file | edits a file                   #
#2.create file | creates a file               ##
#3.read file | reads a file and display it here#
#4.delete file | deletes a file               ##
#5.help | displays this message               #
#6.exit | To exit the program                 ###############
#7.create folder | creates a folder in the current directory#
#8.delete folder | deletes a folder                         #
#9.list files | list the files of a path                    #
#10.list paths | list the paths of a path                   #
#NOTE:Don't do the list path command in the C:\ directory   #
#11.set path | sets the  path for other commands            #################################
#12.show path | shows the current path your working on                                      #
#Note:if the path is not set the default path is the current place where you downloaded this#
#13.show history | Shows all the commands you used                                          #
#14.settings | Just the settings                                                            #
#===========================================================================================#
"""
####FM Script runner####
"""def runscript():
    script_name = input('[Script Name]')
    c = 0
    with open(f'{Path}{script_name}', 'r') as sc:
        global file_to_open
        global scr
        lines = sc.readlines()
        lines = [line.rstrip() for line in lines]
        for r in range(0, len(lines)):
            a = lines[r]
            b = lines[r+1]
            if a == 'create file':
                if b[0:6] == 'name = ':
                    ghfile = str(b[7:])
                with open(f'{Path}{ghfile}', 'w+') as cf:
                    cf.close()
                scr = True
            elif a == 'edit file':
                if b[0:6] == 'name = ':
                    ehfile = str(b[7:])
                with open(f'{Path}{ehfile}', 'w+') as cf:
                    cf.close()
                scr = True
            elif a[0:6] == 'name = ':
                pass

    if scr == True:
        print('Script has been executed succesfully')
    else:
        print('The script has an error')"""
####CLI Commands####
parser.add_argument("-list", help="lists the files in the current directory",
                    action="store_true", required=False)
parser.add_argument("-curname", help="Displays the current directory name",
                    action="store_true", required=False)
parser.add_argument("-curpath", help="Displays the current directory path",
                    action="store_true", required=False)
parser.add_argument("-cfile", help="creates a file",
                    action="store_true", required=False)
parser.add_argument("-dfile", help="Deletes a file",
                    action="store_true", required=False)

args = parser.parse_args()

if args.list:
    files = os.listdir(os.curdir)
    for f in files:
        print(f)
    run = False

if args.curname:
    folder_name = os.getcwd()
    print(os.path.basename(folder_name))
    run = False

if args.curpath:
    dir_path = os.getcwd()
    print(dir_path)
    run = False

if args.cfile:
    file_name = input('[Enter Name]:')
    with open(file_name, 'w+') as d:
        print('file created')
        d.close
    run = False

if args.dfile:
    file_name = input('[Enter Name]:')
    if os.path.exists(file_name):
        os.remove(file_name)
    else:
        print(term.red('[ERROR]:No File Found with that name'))
    run = False
###############################
def delete_last_line():
    sys.stdout.write('\x1b[1A')
    sys.stdout.write('\x1b[2K')
def clear():
    # for windows
    if os.name == 'nt':
        _ = os.system('cls')
    if os.name != 'nt':
        _ = os.system('clear')
###########Settings############
color = term.yellow
warning_color = term.red
edit_color = term.blue
###############################
if run == True:
    print(term.green('[:Made by Sasen Perera 2021:]\n[For help type "help"]\n[Version 3.0.0]'))
while run:
    x += 1
    inp = input(color(f'[{x}]:'))
    if inp == 'exit':
        print(warning_color('[]Are you sure?'))
        ex = input(warning_color('[y/n]:'))
        if ex == 'y':
            history = []
            run = False
        elif ex == 'n':
            pass
    
    elif inp == 'set path':
        history.append('set path')
        Path = input('[Enter Path]:')

    elif inp == 'show path':
        history.append('show path')
        print(Path)

    elif inp == 'settings':
        history.append('settings')
        print('[color for prompts ex.[0]]')
        cc = input('[red, green, yellow[default], blue]:')
        match cc:
            case 'red':
                color = term.red
            case 'green':
                color = term.green
            case 'yellow':
                color = term.yellow
            case 'blue':
                color = term.blue
            case None:
                color = term.yellow
        print('[color for warnings]')
        wc = input('[red[default], green, yellow, blue]:')
        match wc:
            case None:
                warning_color = term.red
            case 'red':
                warning_color = term.red
            case 'green':
                warning_color = term.green
            case 'yellow':
                warning_color = term.yellow
            case 'blue':
                warning_color = term.blue
        print('[color for edits ex. [>>]]')
        ec = input('[red, green, yellow, blue[default]]:')
        match ec:
            case None:
                edit_color = term.blue
            case 'red':
                edit_color = term.red
            case 'green':
                edit_color = term.green
            case 'yellow':
                edit_color = term.yellow
            case 'blue':
                edit_color = term.blue
    elif inp == 'create file':
        history.append('create file')
        file_name = input('[enter name]:')
        with open(f'{Path}{file_name}', 'w+') as g:
            for y in range(len(ani)+1):
                print(ani[0:y])
                time.sleep(1)
                delete_last_line()
            print('[]file created')
            print('[]To write this file write "write file" command and write the name')
            g.close

    elif inp == 'edit file':
        history.append('edit file')
        file_name = input('[enter name]:')
        with open(f'{Path}{file_name}', 'w', encoding="utf-8") as f:
            edit = True
            while edit:
                i_e = input(warning_color('[Status[stop,resume]]:'))
                if i_e == 'stop':
                    f.close()
                    edit = False
                elif i_e == 'resume':
                    e_i = input(edit_color('[>>]:'))
                    if e_i == '<n>':
                        f.write('\n')
                    else:
                        f.write(e_i)

    elif inp == 'read file':
        history.append('read file')
        file_name = input('[enter name]:')
        with open(f'{Path}{file_name}', 'r') as h:
            a = h.read()
            print(f'{a}')
            h.close()

    elif inp == 'delete file':
        file = input('[enter name]:')
        filepath = f'{Path}{file}'
        for z in range(len(ani)+1):
            print(ani[0:z])
            time.sleep(1)
            delete_last_line()
        os.remove(filepath)
        print('[ ]File Deleted')
        history.append('delete file')

    elif inp == 'help':
        print(help_message)
    
    elif inp == 'create folder':
        folder_name = input('[enter name]:')
        folder_path = f'{Path}{folder_name}'
        for a in range(len(ani)+1):
            print(ani[0:a])
            time.sleep(1)
            delete_last_line()
        os.makedirs(folder_path)
        print(term.green("Folder "+folder_name+" Created"))
        history.append('create folder')

    elif inp == 'delete folder':
        folder_name = input('[enter name]:')
        folder_path = f'{Path}{folder_name}'
        if len(os.listdir(folder_path)) == 0:
            for b in range(len(ani)+1):
                print(ani[0:b])
                time.sleep(1)
                delete_last_line()
            os.rmdir()
            history.append('delete folder')
        else:
            print(term.red('Folder not empty'))

    elif inp == 'list files':
        history.append('list files')
        files = os.listdir(Path)

        for f in files:
            print(f)

    elif inp == 'list paths':
        history.append('list paths')
        for root, directories, files in os.walk(Path, topdown=False):
            for name in files:
                print(os.path.join(root, name))
            for name in directories:
                print(os.path.join(root, name))
    
    elif inp == 'show history':
        history.append('show history')
        for k in range(0,len(history)):
            print(f'({k+1}){history[k]}')

    # elif inp == 'run script':
        # runscript()

    elif inp == '':
        """Nothing will happen"""

    elif inp[0] == "'" and inp[-1] == "'" or inp[0] == '"' and inp[-1] == '"':
        print(inp[1:-1])

    elif inp == 'clear':
        clear()

    else:
        print(warning_color('[]incorrect command'))