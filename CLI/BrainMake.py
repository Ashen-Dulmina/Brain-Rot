#This is the official CLI tool for Brain-Rot
#/credits: @Ashen-Dulmina

from colorama import init, Fore, Back, Style #for fancy cli
import pyfiglet #for ascii art
import requests #for version check and ect.
import base64 #encode and decode
import time #wait for shit
import json #read and write json
import sys #get args
import os #clear the console ect.

os.system('cls' if os.name == 'nt' else 'clear') #clears the console in the begining
init() #initialize colorama


#############################
#     Json Dump Function    #
#############################

def dump_to_json(data, filename): #this function dumps json objects into json files
  with open(filename, 'w') as file: #with the jsonfile open as file
    json.dump(data, file, indent=4) #write json data with indentation of 4


#############################
#  Convert Files Into B64   #
#############################

def convert_B64(): #this function converts Brain-Rot files into b64 format
  os.system('cls' if os.name == 'nt' else 'clear') #clears the console
  
  pkg_name = input(f"{Fore.RESET}Package Name : {Fore.CYAN}")  #gets the package name
  pkg_version = input(f"{Fore.RESET}Package Version : {Fore.CYAN}")  #gets the package version
  pkg_author = input(f"{Fore.RESET}Package Author : {Fore.CYAN}")  #gets the package author
  pkg_element_count = int(input(f"{Fore.RESET}Package File Count : {Fore.CYAN}"))  #gets the package file count
  
  elements = {} #define empty variable as elemets for future use
  for i in range(pkg_element_count): #loops in range of the element count
    file_name = input(f"{Fore.RESET}Name of file {i+1} : {Fore.CYAN}") #gets the name of file
    print(Fore.RESET)
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
    
  json_file = f"{pkg_name}.json" #defines json file based on the given name
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
  os.system('cls' if os.name == 'nt' else 'clear') #clears the console
  
  invMSG = "" #blank var
  fileLOOP = True #loopbreak
  while fileLOOP: #while loop
    os.system('cls' if os.name == 'nt' else 'clear') #clears the console
    
    print(invMSG) #invalid msg
    local_pkg_file = input(f"{Fore.YELLOW}Select the local package file : {Fore.CYAN}") #select input
    
    if os.path.isfile(local_pkg_file) == True: #if file exists
      fileLOOP = False #breakloop
    else: #if file is imaginary or simply does not exist
      invMSG = f"{Fore.RED}[!] This file does not exist : {Fore.MAGENTA}{local_pkg_file}{Fore.RED}." + '\n' #error lol
  
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
#  Establish Remote Package #
#############################

def establish_remote(): #this function establishes remote packages
  os.system('cls' if os.name == 'nt' else 'clear') #clears the console
  remote_url = input(f"{Fore.YELLOW}Enter URL to the remote package : {Fore.CYAN}") #gets the remote url
  print(Fore.RESET) #resets Color
  #https://raw.githubusercontent.com/Ashen-Dulmina/Brain-Rot/main/CLI/test.json
  
  try:
    rem = requests.get(remote_url) #fetches the json data
    rem.raise_for_status() 
  except requests.exceptions.HTTPError as errh: #on error
    print(f"{Fore.RED}[!] Http Error!")
    print(f"{Fore.RED}[!] {errh.args[0]}")
    exit(1)
  except requests.exceptions.RequestException as errex: #on error
    print(f"{Fore.RED}[!] Exception request!")
    print(f"{Fore.RED}[!] {errex}")
    exit(1)
  except requests.exceptions.ReadTimeout as errrt: #on error
    print(f"{Fore.RED}[!] Request timeout!")
    print(f"{Fore.RED}[!] {errrt}")
    exit(1)
  except requests.exceptions.MissingSchema as errmiss: #on error
    print(f"{Fore.RED}[!] Missing schema: include http or https!")
    print(f"{Fore.RED}[!] {errmiss}")
    exit(1)
  except requests.exceptions.ConnectionError as conerr: #on error
    print(f"{Fore.RED}[!] Connection error!")
    print(f"{Fore.RED}[!] {conerr}")
    exit(1)
  
  remote_pkg_data = rem.json() #fetches the json data
  
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
    
    
    
#############################
#   Establish Readme .MD    #
#############################

def establish_readme(PROJECT_NAME : str): #this function makes readme files
  os.system('cls' if os.name == 'nt' else 'clear') #clears the console
  print(f"{Fore.MAGENTA}Please enter the title for the readme. {Fore.WHITE}{Style.DIM}(Leave blank to use project name){Style.RESET_ALL}") #notice print
  print("") #prints empty line
  readme_title = input(f"{Fore.YELLOW}>> {Fore.CYAN}").replace(" ", "-") #takes the readme title and replaces the space with dash
  print("\n") #printst a newline
  print(f"{Fore.MAGENTA}Enter a suitable project description. {Fore.WHITE}{Style.DIM}(Leave black if you {Back.RED}don't{Back.RESET} know what you are doing){Style.RESET_ALL}") #notice print
  print("")  #prints empty line
  readme_description = input(f"{Fore.YELLOW}>> {Fore.CYAN}") #takes the readme description
  
  os.system('cls' if os.name == 'nt' else 'clear') #clears the console
  
  if readme_title == "" : #if readme title is blank
    readme_title = PROJECT_NAME.replace(" ", "-") #uses the project name
  else: #if not
    pass #continue
  
  with open("README.md", 'w') as readme: #open the readme file
    readme.write(f"# {readme_title}" + '\n') #write the title
    readme.write(readme_description) #write the description
    readme.close() #close the file
    print(f"{Fore.GREEN}[*] Readme written !") #yay print



################################
#  InitializeProjectsTemplate  #
################################

def InitializeTemplateProject(): #Establishes a project from template package
  os.system('cls' if os.name == 'nt' else 'clear') #clears the console
  
  print(f"{Fore.MAGENTA}Please enter the project name. {Fore.RED}(!!Don't leave blank!!){Fore.RESET}") #notify print
  print("") #prints empty line
  projectFolderName = input(f"{Fore.YELLOW}>> {Fore.CYAN}").replace(" ", "-") #gets the project name
  currentTerminalRoot = os.getcwd() #get current working directory
  
  os.chdir(currentTerminalRoot) #change cwd
  
  if not os.path.exists(projectFolderName) : #if project folder dosent exist
    os.makedirs(projectFolderName) #make the folder
  else : #if it exists
    os.system('cls' if os.name == 'nt' else 'clear') #clears the console 
    print(f"{Fore.RED}[!] This Project/Folder Alredy Exists ...{Fore.RESET}") #error
    print(f"{Fore.RED}[!] Quiting Action ...{Fore.RESET}") #error
    exit(1) #exit
  
  os.chdir(projectFolderName) #change cwd to the new folder
  os.system('cls' if os.name == 'nt' else 'clear') #clears the console
  
  print(f"{Fore.MAGENTA}Do you want to install a local or remote template ? {Fore.WHITE}({Fore.GREEN}L{Fore.WHITE}/{Fore.RED}R{Fore.WHITE}){Fore.RESET}") #notify print
  print("") #empty line
  
  loopONE = True #loop one breaker 
  while loopONE: #while loop
    type_selection = input(f"{Fore.YELLOW}>> {Fore.CYAN}") #selection of local or remote template
    print("\n") #newline
    
    if type_selection.lower() == "l" or type_selection.lower() == "r": #if the selection is valid
      loopONE = False #break the loop
    else: #if the selection if invalid
      print(f"{Fore.RED}[!] Invalid Option ...") #prints error
      print("") #prints empty line
      #continues to loop
    
  print(f"{Fore.MAGENTA}Do you want to make a readme file ? {Fore.WHITE}({Fore.GREEN}y{Fore.WHITE}/{Fore.RED}n{Fore.WHITE}){Fore.RESET}") #notify print
  print("") #prints empty line
  
  loopTWO = True #loop two breaker
  while loopTWO: #while loop two
    want_readme = input(f"{Fore.YELLOW}>> {Fore.CYAN}") #selects if user want readme or not
    print("\n") # newline
    if want_readme.lower() == "y" or want_readme.lower() == "n": #if selection is valid
      loopTWO = False #breaks the loop
    else: #if the selection is invalid
      print(f"{Fore.RED}[!] Invalid Option ...") #prints this error
      print("") #prints empty line
      #continues to loop
  
  if type_selection.lower() == "l": #if selection is local
    os.system('cls' if os.name == 'nt' else 'clear') #clears the console
    establish_local() #runs local packager
  elif type_selection.lower() == "r": #if selection is remote
    os.system('cls' if os.name == 'nt' else 'clear') #clears the console
    establish_remote() #runs remote packager
  else: #if both is false just in case
    pass #continue like nothing happened

  if want_readme.lower() == "y": #if user wants readme file
    os.system('cls' if os.name == 'nt' else 'clear') #clears the console
    establish_readme(projectFolderName) #runs readme writer
  else: #if he dosent want it
    pass #we dont care
  
  os.system('cls' if os.name == 'nt' else 'clear') #clears the console
  print(f"{Fore.GREEN}[*] Project successfully created from template !") #yay print
    


################################
#         Help Message         #
################################

def helpMSG(): #displays a help message
  os.system('cls' if os.name == 'nt' else 'clear') #clears the console
  
  print(f"{Fore.GREEN}|-------------------------------------------------------------------------------|") #81 dash line
  print(f"{Fore.GREEN}|                                   {Fore.MAGENTA}HELP-MENUE{Fore.GREEN}                                  |") #81 dash line
  print(f"{Fore.GREEN}|-------------------------------------------------------------------------------|") #81 dash line
  print(f"{Fore.GREEN}| {Fore.CYAN}[1] -h, --help, help{Fore.GREEN}                  | {Fore.YELLOW}Displays help menue.{Fore.GREEN}                  |") #81 dash line
  print(f"{Fore.GREEN}|                                       |                                       |") #81 dash line
  print(f"{Fore.GREEN}| {Fore.CYAN}[2] -i, --initialize, --init,{Fore.GREEN}         | {Fore.YELLOW}Make/Initialize new project.{Fore.GREEN}          |") #81 dash line
  print(f"{Fore.GREEN}|     {Fore.CYAN}^ initialize, init{Fore.GREEN}                | {Fore.YELLOW}~{Fore.GREEN}                                     |") #81 dash line
  print(f"{Fore.GREEN}|                                       |                                       |") #81 dash line
  print(f"{Fore.GREEN}| {Fore.CYAN}[3] -c, --convert, --conv,{Fore.GREEN}            | {Fore.YELLOW}Generate your own template or{Fore.GREEN}         |") #81 dash line
  print(f"{Fore.GREEN}|     {Fore.CYAN}^ convert, conv{Fore.GREEN}                   | {Fore.YELLOW}^ package from written code.{Fore.GREEN}          |") #81 dash line
  print(f"{Fore.GREEN}|-------------------------------------------------------------------------------|") #81 dash line
  exit(1)



################################
#         Run Handler          #
################################

def loader(): #loading animation for noobies
  print(Fore.MAGENTA, end='\r')
  sys.stdout.write('\rLoading Brain-Make .       ⠿')
  time.sleep(0.1)
  sys.stdout.write('\rLoading Brain-Make .       ⠾')
  time.sleep(0.1)
  sys.stdout.write('\rLoading Brain-Make ..      ⠽')
  time.sleep(0.1)
  sys.stdout.write('\rLoading Brain-Make ...     ⠻')
  time.sleep(0.1)
  sys.stdout.write('\rLoading Brain-Make ....    ⠟')
  time.sleep(0.1)
  sys.stdout.write('\rLoading Brain-Make .....   ⠯')
  time.sleep(0.1)
  sys.stdout.write('\rLoading Brain-Make ......  ⠷')
  time.sleep(0.1)
  sys.stdout.write('\rLoading Brain-Make .       ⠾')
  time.sleep(0.1)
  sys.stdout.write('\rLoading Brain-Make ..      ⠽')
  time.sleep(0.1)
  sys.stdout.write('\rLoading Brain-Make ...     ⠻')
  time.sleep(0.1)
  sys.stdout.write('\rLoading Brain-Make ....    ⠟')
  time.sleep(0.1)
  sys.stdout.write('\rLoading Brain-Make .....   ⠯')
  time.sleep(0.1)
  sys.stdout.write('\rLoading Brain-Make ......  ⠷')
  time.sleep(0.1)
  sys.stdout.write('\rLoading Brain-Make .       ⠾')
  time.sleep(0.1)
  sys.stdout.write('\rLoading Brain-Make ..      ⠽')
  time.sleep(0.1)
  sys.stdout.write('\rLoading Brain-Make ...     ⠻')
  time.sleep(0.1)
  sys.stdout.write('\rLoading Brain-Make ....    ⠟')
  time.sleep(0.1)
  sys.stdout.write('\rLoading Brain-Make .....   ⠯')
  time.sleep(0.1)
  sys.stdout.write('\rLoading Brain-Make ......  ⠷')
  time.sleep(0.1)
  sys.stdout.write('\rLoading Brain-Make ....... ⠿')
  time.sleep(0.1)
  sys.stdout.write('\r                             ')
  print(Fore.RESET, end='\r')
  os.system('cls' if os.name == 'nt' else 'clear') #clears the console



################################
#        Choise handler        #
################################

def choice_Handler(choice : int): #handles choices
  os.system('cls' if os.name == 'nt' else 'clear') #clears the console
  
  if choice == 1 : #in need of help?
    helpMSG() #help that poor soul
  elif choice == 2 : #want new project?
    InitializeTemplateProject() #give it to meeee or them anyway the same shit 
  elif choice == 3 : #he knows what he's doing
    convert_B64() #make a package
  else: #how the hell is he going to trigger this
    print(f"{Fore.RED}[!] Error in delecting choise!")
    print(f"[^] Report the error at the issues of our github repository{Fore.RESET}")


################################
#    CLI handler for noobs     #
################################

def unargumented_Handler(): #cli with full guide for noobs
  os.system('cls' if os.name == 'nt' else 'clear') #clears the console
  loader() #runs loading animation
  
  loopX = True #loop breaker
  beginerX = ""
  while loopX: #while loop one
    os.system('cls' if os.name == 'nt' else 'clear') #clears the console
    
    print(Fore.CYAN) #Change color to cyan
    print(f"{pyfiglet.figlet_format('Brain - Make.')}{Fore.RESET}") #ASCII art brainmake
    print(f"{Fore.GREEN}-----------------------------------------------------------") #big fucking line
    print("") #empty line
    print(f"{Fore.CYAN} 1. Help.") #help
    print(f" 2. Make new project.") #shid
    print(f" 3. Generate new package.") #shidd
    print('\n')
    print(Fore.RESET) #reset color
    
    print(beginerX) #just in time error ect.
    print(f"{Fore.MAGENTA}What do you want? {Fore.WHITE}(The number of your choice){Fore.RESET}") #bruh
    choiceCLI = input(f"{Fore.YELLOW}>> {Fore.CYAN}")#ask for choice
    
    if not choiceCLI.isnumeric() == True : #if the choise is not only a number
      beginerX = f"{Fore.RED}[!] Invalid choice. {Fore.RESET}" #error
      
    elif choiceCLI.isnumeric() == True : #if the choise is a number
      choiseList = [1, 2, 3] #list of possible choises
      choiceCLI = int(choiceCLI) #choise in numbers
      if not choiceCLI in choiseList : #if invalid choise
        beginerX = f"{Fore.RED}[!] Invalid choice. {Fore.RESET}" #error hahahahahahahaaaaa!
      elif choiceCLI in choiseList : #if choise is within the list
        loopX = False #loopbreak
        choice_Handler(choiceCLI) #api tamai hodatama kale
        
      



################################
#         Run Handler          #
################################

def run_Handler(): #handles the whole thing
  os.system('cls' if os.name == 'nt' else 'clear') #clears the console
  currentTerminalRoot = os.getcwd() #get current working directory
  os.chdir(currentTerminalRoot) #change cwd
  
  helpA = ["-h", "--help", "help"] #define help arguments
  initI = ["-i", "--initialize", "--init", "initialize", "init"] #define init arguments
  convE = ["-c", "--convert", "--conv", "convert", "conv"] #define convert arguments
  
  if len(sys.argv) > 1: #if there is arguments
    control_Argument = str(sys.argv[1]).lower() #gets argument 1 and converts it into a lowercase string
    if control_Argument in helpA : #if argument in heelp
      helpMSG() #help
    elif control_Argument in initI : #if argument in init
      InitializeTemplateProject() #init
    elif control_Argument in convE : #if argument in convert
      convert_B64() #convert
    else: #if argument in none
      print(f"{Fore.RED}[!] Invalid Argument.") #error
      exit(1) #exit
  else:
    unargumented_Handler()

run_Handler()