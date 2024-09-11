#This is the official CLI tool for Brain-Rot
#/credits: @Ashen-Dulmina

import requests
import base64
import sys
import os


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
#   Establish Remote File   #
#############################

