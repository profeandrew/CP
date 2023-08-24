# CLI File Manager

This is a command-line interface (CLI) file manager implemented in Python. It allows you to navigate through a directory structure, create subfolders, create files, and view the contents of files.

## Features

- Navigate through a directory structure consisting of folders and files.
- Create subfolders within existing folders.
- Create files within existing folders.
- Change the current directory using the `cd` command.
- List the contents of the current directory using the `ls` command.

## Usage

1. Run the script in your terminal.
2. You will start in the root directory.
3. Enter commands to interact with the file manager.

## Commands

- `ls`: List the contents of the current directory.
- `cd [folder_name]`: Change the current directory to the specified folder.
- `mkdir [folder_name]`: Create a new subfolder in the current directory.
- `touch [file_name].[extension]`: Create a new file in the current directory.
- `exit`: Exit the file manager.

## Examples


ls - To list the contents of the current CurrentDirectory 

 root ,> Enter a command:ls
#output 
Folder: Home
Folder: Documents

cd - To change from one directory to another one. Type down cd and then enter the name of the directory you would like to go. 

root ,> Enter a command:cd
Enter the folder you would like to go: Home

mkdir - To create a new directory. Type down mkdir and then enter the name of the new directory

Home ,> Enter a command:mkdir
Enther then name of the new folder:Checkpoint_Gaia
Folder 'Checkpoint_Gaia' created. 


touch - create a new file in the current directory type down touch and then enter the extension of the file 

Home ,> Enter a command:touch
Enter the name of the new file: ipsec
now enter the extension:txt