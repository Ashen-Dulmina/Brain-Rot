#This is the official CLI tool for Brain-Rot
#/credits: @Ashen-Dulmina

from colorama import init, Fore, Back, Style
import requests
import base64
import json
import sys
import os

os.system('cls' if os.name == 'nt' else 'clear') #clears the console in the begining
init() #initialize colorama


#############################
#     InitializeProjects    #
#############################

def InitializeProject(NAME : str, ESTABLISH_REMOTE : bool, ESTABLISH_README : bool): #Establishes a project
  projectFolderName = NAME.replace(" ", "-")
  currentTerminalRoot = os.getcwd()
  
  os.chdir(currentTerminalRoot)
  
  if not os.path.exists(projectFolderName) :
    os.makedirs(projectFolderName)
  else :
    print("[!] This Project/Folder Alredy Exists ...")
    print("[!] Quiting Oparaions ...")
    exit(1)
  
  os.chdir(projectFolderName)
  
  if ESTABLISH_REMOTE == True:
    print("Later")
  else:
    print("Later")
    
  if ESTABLISH_README == True:
    print("Later")
  else:
    pass  



#############################
#     Json Dump Function    #
#############################

def dump_to_json(data, filename): #this function dumps json objects into json files
    with open(filename, 'w') as file: #with the jsonfile open as file
        json.dump(data, file, indent=4) #write json data with indentation of 4


#############################
#  Convert Files Into B64   #
#############################

def convert_B64(output_json_file : str): #this function converts Brain-Rot files into b64 format
  pkg_name = input(f"{Fore.RESET}Package Name : {Fore.CYAN}")  #gets the package name
  pkg_version = input(f"{Fore.RESET}Package Version : {Fore.CYAN}")  #gets the package version
  pkg_author = input(f"{Fore.RESET}Package Author : {Fore.CYAN}")  #gets the package author
  pkg_element_count = int(input(f"{Fore.RESET}Package File Count : {Fore.CYAN}"))  #gets the package file count
  
  elements = {} #define empty variable as elemets for future use
  for i in range(pkg_element_count): #loops in range of the element count
    file_name = input(f"{Fore.RESET}Name of file {i+1} : ") #gets the name of file
    readable_file = open(file_name, 'rb').read() #opens and reads it in the read bytes mode
    encoded_srting = base64.b64encode(readable_file).decode('utf-8') #encodes and turns the encoded bytesobject into a string
    elements[f"file_{i+1}"] = {
      "file_name" : file_name,
      "file_content" : encoded_srting
    } #includes the filename and the encoded content into the elements variable
    
  json_structure = {
    "package_name" : pkg_name,
    "package_author" : pkg_author,
    "package_version" : pkg_version,
    "package_element_count" : pkg_element_count,
    "elements" : elements
  } #standerd json structure for this ppackage manager
    
  json_file = f"{output_json_file}.json" #defines json file based on the given name
  dump_to_json(json_structure, json_file) #writes data into the json file
  print(f"{Fore.LIGHTCYAN_EX}[*] Successfully wrote package into {Fore.LIGHTYELLOW_EX}{json_file}{Fore.LIGHTCYAN_EX} !{Fore.RESET}") #prints the happy flag



#############################
#     Reads json files      #
#############################

def read_json_file(filename): #this function read the json data in a given file
    with open(filename, 'r') as file: #open the given file as file
        data = json.load(file) #loads the json data in the file
    return data #returns the json data to the caller



#############################
#  Establish Local Package  #
#############################

def establish_local(): #this function establishes local packages
  local_pkg_file = input(f"{Fore.YELLOW}Select the local package file : {Fore.CYAN}")
  print(Fore.RESET) #resets Color
  pkg_data = read_json_file(local_pkg_file)
  
  os.system('cls' if os.name == 'nt' else 'clear') #clears the console
  print(f"Current package's name : {Fore.CYAN}{pkg_data.get('package_name', 'Package Name Undefined!!')}{Fore.RESET}") #prints package name
  print(f"Current package's author : {Fore.CYAN}{pkg_data.get('package_author', 'Unknown Author!!')}{Fore.RESET}") #prints package author
  print(f"Current package's version : {Fore.CYAN}{pkg_data.get('package_version', 'Unknown Version!!')}{Fore.RESET}") #prints package version
  print(f"Current package's file count : {Fore.CYAN}{pkg_data.get('package_element_count', 'Error!!')}{Fore.RESET}") #prints package element count
  print("\n") #newline
  print(f"{Fore.LIGHTMAGENTA_EX}Please confirm that the above package is the correct package {Fore.RESET}({Fore.GREEN}y{Fore.RESET}/{Fore.RED}n{Fore.RESET}){Fore.LIGHTMAGENTA_EX} : {Fore.RESET}") #prints the confirmation message
  
  confirmation = input(f"{Fore.YELLOW}> {Fore.CYAN}") #verification input
  print(Fore.RESET) #resets Color
  os.system('cls' if os.name == 'nt' else 'clear') #clears the console
  if confirmation.lower() == "y" : #if the input lowercased equals y
    pkg_verified = True #verified
  elif confirmation.lower() == "n" : #if the input lowercased equals n
    print(f"{Fore.RED}[!] Remote package was not verified by the user !" + Fore.RESET)
    exit(1)
  else: #if the input lowercased does not equals y or n
    print(f"{Fore.RED}[!] Invalid Choice ...." + Fore.RESET) #error
    exit(1) #error
    
  
  if pkg_verified == True :# if the package is verified by the user
    os.system('cls' if os.name == 'nt' else 'clear') #clears the console
    for i in range(int(pkg_data.get('package_element_count', "0"))) : #for loop in the range of package item count
      filename = pkg_data["elements"][f"file_{i+1}"].get("file_name") #get the respective file name
      filename = open(filename, 'w') #opens it
      file_content = pkg_data["elements"][f"file_{i+1}"].get("file_content").encode() #get the encoded respective files content
      file_content = base64.b64decode(file_content).decode('utf-8') #decodes and changes it into a string
      filename.write(file_content) #writes the file
      print(f"[*] File Created -- {Fore.MAGENTA}{pkg_data['elements'][f'file_{i+1}'].get('file_name')}{Fore.RESET}") #prints the filename along a just created msg
      filename.close() #closes the file
  else: #if validation is not doen
    print(f"{Fore.RED}[!] Source action failed ....{Fore.RESET}") #source action error
  


#############################
#  Establish Local Package  #
#############################

def establish_remote(): #this function establishes remote packages
  remote_url = input(f"{Fore.YELLOW}Enter URL to the remote package : {Fore.CYAN}") #gets the remote url
  print(Fore.RESET) #resets Color
  #https://raw.githubusercontent.com/Ashen-Dulmina/Brain-Rot/main/CLI/test.json
  remote_pkg_data = requests.get(remote_url).json() #fetches the json data
  
  os.system('cls' if os.name == 'nt' else 'clear') #clears the console
  print(f"Current package's name :  {Fore.CYAN}{remote_pkg_data['package_name']}{Fore.RESET}") #prints package name
  print(f"Current package's author : {Fore.CYAN}{remote_pkg_data['package_author']}{Fore.RESET}") #prints package author
  print(f"Current package's version : {Fore.CYAN}{remote_pkg_data['package_version']}{Fore.RESET}") #prints package version
  print(f"Current package's file count : {Fore.CYAN}{str(remote_pkg_data['package_element_count'])}{Fore.RESET}") #prints package element count
  print("\n") #newline
  print(f"{Fore.LIGHTMAGENTA_EX}Please confirm that the above package is the correct package {Fore.RESET}({Fore.GREEN}y{Fore.RESET}/{Fore.RED}n{Fore.RESET}){Fore.LIGHTMAGENTA_EX} : {Fore.RESET}") #prints the confirmation message
  
  confirmation = input(f"{Fore.YELLOW}> {Fore.CYAN}") #verification input
  print(Fore.RESET) #resets Color
  os.system('cls' if os.name == 'nt' else 'clear') #clears the console
  if confirmation.lower() == "y" : #if the input lowercased equals y
    remote_pkg_verified = True #verified
  elif confirmation.lower() == "n" : #if the input lowercased equals n
    print(f"{Fore.RED}[!] Remote package was not verified by the user !" + Fore.RESET)
    exit(1)
  else: #if the input lowercased does not equals y or n
    print(f"{Fore.RED}[!] Invalid Choice ...." + Fore.RESET) #error
    exit(1) #error
  
  if remote_pkg_verified == True :# if the package is verified by the user
    os.system('cls' if os.name == 'nt' else 'clear') #clears the console
    for i in range(int(remote_pkg_data.get('package_element_count', "0"))) : #for loop in the range of package item count
      filename = remote_pkg_data["elements"][f"file_{i+1}"].get("file_name") #get the respective file name
      filename = open(filename, 'w') #opens it
      file_content = remote_pkg_data["elements"][f"file_{i+1}"].get("file_content").encode() #get the encoded respective files content
      file_content = base64.b64decode(file_content).decode('utf-8') #decodes and changes it into a string
      print(f"[*] File Created -- {Fore.MAGENTA}{remote_pkg_data['elements'][f'file_{i+1}'].get('file_name')}{Fore.RESET}") #prints the filename along a just created msg
      filename.write(file_content) #writes the file
      filename.close() #closes the file
  else: #if validation is not doen
    print(f"{Fore.RED}[!] Source action failed ....{Fore.RESET}") #source action error
    
    
    
establish_remote()