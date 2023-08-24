
# This class defines folder attributes and methods 
class Folder:
    def __init__(self,name, link_node = None): # constructor that initialize the folder attributes name and pointer 
        self.name = name
        self.link_node = link_node

    def get_folder_name(self): # method for getting the name of the folder 
        return self.name
    
    def get_link_node(self): # method for getting the pointer  
        return self.link_node
    
    def update_pointer (self,link_node):
        self.link_node = link_node
        ## methods that allows changing directory from root to home and then Documents
    
     ## this method allow to find a folder by its name
    def find_folder_by_name(self,name):
        if self.name == name:
            return self
        elif self.link_node:
            return self.link_node.find_folder_by_name(name)
        else:
            return None
    
    
        ## this method allow list the files 

    def list_contents(self):
        current_node = self.link_node
        while current_node:
            if isinstance(current_node, Folder):
                print("Folder:", current_node.get_folder_name())
            elif isinstance(current_node, File):
                print("File:", current_node.get_full_name())
            if hasattr(current_node, "get_link_node"):
                current_node = current_node.get_link_node()
            else:
                break

        ## this method creates folders inside the main folders (Root,Home and Documents)

    def create_subfolder(self, folder_name):
        new_folder = Folder(folder_name)
        if self.link_node is None:
            self.link_node = new_folder
        else:
            current_node = self.link_node
            while current_node.get_link_node():
                current_node = current_node.get_link_node()
            current_node.update_pointer(new_folder)   
    ## this method creates a file         

    def create_file(self, file_name,extension):
        new_file = File(file_name,extension)  
        if self.link_node is None:
            self.link_node = new_file
        else:
            current_node = self.link_node
            while current_node.get_link_node():
                current_node = current_node.get_link_node()
            current_node.update_pointer(new_file)


class CurrentDirectory: # this class will be used by the cd command 
    def __init__(self): # constructor 
        self.current_folder = None
    def set_current_folder(self, folder): # method for setting the current directory 
        self.current_folder = folder

    def get_current_folder(self): # this method gets the current directory value
        return self.current_folder
    
   # class file with different attributes  and methods 
class File:
    def __init__(self, name, extension):
        self.name = name
        self.extension = extension
        self.contents = ""  # Initialize an empty contents string
    # this method retrieves the file name
    def get_name(self):
        return self.name
    # this method retrieves the file name
    def get_extension(self):
        return self.extension
    # this method retrieves the file name and extension
    def get_full_name(self):
        return f"{self.name}.{self.extension}"
    # this method retrieves the file content
    def get_contents(self):
        return self.contents
    # a setter method for create the empty file                                      
    def set_contents(self, contents):
        self.contents = contents
    # append new content
    def append_contents(self, new_contents):
        self.contents += new_contents
    # Read the content of a file
    def display_contents(self):
        print(f"Contents of {self.get_full_name()}:\n{self.contents}")

    #  A special method that returns a string representation of the file

    def __str__(self):
        return f"File: {self.get_full_name()}"

            

#  Instantiate the three folders 
root = Folder("root")
Home = Folder("Home")
Documents = Folder("Documents")

current_directory = CurrentDirectory()
current_directory.set_current_folder(root)

# define the pointer (Relationships):
# Root
# ----> Home
#----------> Documents
root.update_pointer(Home)
Home.update_pointer(Documents)

Home_data = root.get_link_node().get_folder_name()
Documents_data = Home.get_link_node().get_folder_name()



command = input(f"{current_directory.get_current_folder().get_folder_name()} ,> Enter a command:") # the user should enter a command. Current directory is shown at left hand. 

# loop that runs the CLI

while True:
    
    # ls command validation 
    if command == "ls":
        current_folder = current_directory.get_current_folder()
        if current_folder:
            current_folder.list_contents()
            #print(f"{current_folder.get_folder_name()} >", Home_data)
        else:
            print("No current folder selected.")
        command = input(f"{current_directory.get_current_folder().get_folder_name()} ,> Enter a command:")

    # touch command validation 
    elif command == "touch":
        file_name = input("Enter the name of the new file: ")
        extesion = input("now enter the extension:")
        current_folder = current_directory.get_current_folder()
        if current_folder:
            current_folder.create_file(file_name,extesion)
            print(f"File '{file_name}' created.")
        else:
            print("No current folder selected.")
        command = input(f"{current_directory.get_current_folder().get_folder_name()} ,> Enter a command:")
    
    # mkdir command validation 
    elif command == "mkdir":
        folder_name = input("Enther then name of the new folder:")
        current_folder = current_directory.get_current_folder()
        if current_folder:
            current_folder.create_subfolder(folder_name)
            print(f"Folder '{folder_name}' created. ")
        else:
            print("No current folder selected")
        command = input(f"{current_directory.get_current_folder().get_folder_name()} ,> Enter a command:") # the user should enter a command. Current directory is shown at left hand. 

    # cd commmand validation 

    elif command == "cd":
        temp_folder = input("Enter the folder you would like to go: ")
        current_folder = current_directory.get_current_folder()
        if current_folder:
            target_folder = current_folder.find_folder_by_name(temp_folder)
            if target_folder:
                current_directory.set_current_folder(target_folder)
            else:
                print("Folder not found.")
        else:
            print("No current folder selected.")
        command = input(f"{current_directory.get_current_folder().get_folder_name()} ,> Enter a command:")


    elif command == "exit":
        print("Goodbye")
        break
    else:
        command = input("Command not found, Enter a command \n")
