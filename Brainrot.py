#This is the official compiler for BRAINROT
#extetion '.rot'
#User interaction Keys :-
# [!] = error
# [^] = comment
# [-] = instruction
# [+] = normal
# [*] = pass (this means something is ok or good)
# [=] = Update or Notification

from urllib import request
import requests
import sys
import os


#############################
#       CheckVersion        #
#############################

def checkVersion(): #Checks if the version is stable and up to date
  localVersion = open("VERSION", 'r').read() #read the local VERSION file for version data
  remoteVersion = requests.get('https://raw.githubusercontent.com/Ashen-Dulmina/Brain-Rot/main/VERSION').text #read the remote VERSION file for version data
  remoteVersion = remoteVersion.removesuffix('\n') #removes the newline fron the end
  
  if remoteVersion.endswith("b") or remoteVersion.endswith("a"): #if the version is alpha or beta
    quit #quit the functioj
  elif remoteVersion.endswith("s"): #if the version is stable
    localVersion = localVersion.split("-") #plits the linr from the '-'
    remoteVersion = remoteVersion.split("-") #plits the linr from the '-'
    
    if float(localVersion[0]) < float(remoteVersion[0]) : #if the local version is lower than the latest release
      print(f"[=] Your Current Version is {localVersion[0]}-{localVersion[1]}.") #prints the current version
      print(f"[=] The Latest Release is {remoteVersion[0]}-{remoteVersion[1]}.") #prints the remote version
      print(f"[=] Please Update to Version {remoteVersion[0]}-{remoteVersion[1]} for New Features and Major Bug Fixes.") #pints the update notice
      print('\n') #prints a newline at the end
    elif float(localVersion[0]) == float(remoteVersion[0]) : #if the local version is the latest release
      print("[=] Your are Up-to-Date !")
      print('\n') #prints a newline at the end
    else: #if the version somehow greater to date
      pass #continue



#############################
#      CheckInternet        #
#############################

def checkInternetConnectivity(): #Checks internet Connectivity to check for updates
  try:
    request.urlopen('https://8.8.8.8', timeout=3) #tries to ping googles DNS server
    return True #is it could return true
  except request.URLError as err:  #if it fails
    return False #is it couldn't return false



#############################
#    validatingROTfiles     #
#############################

def validateROTfile(): #validates the file before reading and compiling
  if len(sys.argv) < 4 : #checks if the number of arguments is less than 2
    print("[!] Minus Aura detected ! ...")
    print("[!] Brainrot Compiler needs one or more arguments to oparate.")
    print("[!] No argument has been passed to the compiler.")
    print("[-] Brainrot <filename.rot> <compiled_file name> <autorun(y or n)>") #error message for no arguments
    print("[^] Better luck next time..")
    exit(1) #exits the program code - 1
  else: #if the number of arguments are greater than 2 or equal to 2
    pass #continues to function
  
  rotFileSys = sys.argv[1] #takes the argument
  if rotFileSys.endswith(".rot") == False: #if the argument does not end with '.rot'
    print("[!] Minus Aura detected ! ...")
    print("[!] Invalid argument passed! ... ")
    print(f"[!] Minus Aura detected on : {rotFileSys} : invalid extention.") #error message for invalid extention
    print("[^] Only files with '.rot' extention is supported.")
    exit(1)
  else: #if argument ends with '.rot'
    pass #continues to function
  
  if os.path.isfile(rotFileSys) == False: #if the file does not exist
    print("[!] Minus Aura detected ! ...")
    print("[!] The file mentioned does not exist.")
    print(f"[!] Minus Aura detected on : {rotFileSys} : invalid file.") #error message for invalid file name
    print("[^] Brainrot Compiler only support existing files.")
    print("[^] If you want to compile your imaginary bullshit, this is not your place.")
    exit(1)
  else: #if the file existp
    pass #continues to function
  
  #at this stage all the pre-file-validations have been passed
  #they are :-
  #1.the file exists
  #2.the file has '.rot' extention
  #3.the file exists
  print("[*] Pre-File-Validation Colmpleted !")#return the 1st win flag
  print("[^] This does not mean the script is verified.")
  print("")
  print("")
  return True #return the 1st stage checks are true



#############################
#   Write Compiled Files    #
#############################

def writeCom(Text : str, Line : int):
  compiledFile = open(f"{sys.argv[2]}.bpy", 'a') #creates the compiled file
  compiledFile.write(f"{Text}"+'\n') #writes the text with a newline
  compiledFile.close() #close the file
  print(f"[+] {Line} Lines have been Compiled and Written.", end='\r') #print a Line count
 

#############################
#        Read&Convert       #
#############################

def rConvert(): #this function read and converts things into python
  lineCounter = 0 #the line counter component
  
  while True:
    rotFileSys = open(sys.argv[1], 'r').readlines() #gets the rot file from args and reads it line by line
    
    def detectVariables(lineTOscan : str, XCount : int): #scans the passed line for a possible variable
      lineTabCount = 0 #reset the tabcount to zero
      line = lineTOscan #reset the variable in a loop
      
      line = lineTOscan.removesuffix('\n') #remove the new line
      
      lineTabCount = line.count("  ") #getas the intendation count
      lineTabN = "  " * lineTabCount #repeats the string for the tabs
      line = line.replace("  ", "") #replace the tabs with NULL
        
      if line.startswith("make"): #if the line startswith make 
        line = line.replace("--", "#") #replace '--' with #
        line = line.replace("make ", "") #replace 'make ' with NULL
        line = line.replace("be", "=") #replace "be" with "="
        line = line.replace("NOCAP", "True") #replace NOCAP with True
        line = line.replace("CAP", "False") #replace CAP with False
        line = line.replace("NOTHING", "None") #replace NOTHING with None
        line = line.replace("pluS", "+") #replace pluS with +
        line = line.replace("minuS", "-") #replace minuS with -
        line = line.replace("dividE", "/") #replace devidE with /
        line = line.replace("multiplY", "*") #replace multiplY with *
        writeCom(f"{lineTabN}{line}", XCount) #prints the line
      else: #if the line does not startswith make 
        pass #exit the function
    
    def detectPrintCommands(lineTOscan : str, XCount : int): #scans the passed line for a possible print commands
      plineTabCount = 0 #reset the tabcount to zero
      pline = lineTOscan #reset the variable in a loop

      pline = lineTOscan.removesuffix('\n') #remove the new line
      
      plineTabCount = pline.count("  ") #getas the intendation count
      plineTabN = "  " * plineTabCount #repeats the string for the tabs
      pline = pline.replace("  ", "") #replace the tabs with NULL
      
      if pline.startswith("freespeech"): #if the line startswith freespeech
        pline = pline.replace("--", "#") #replace '--' with #
        pline = pline.replace("pluS", "+") #replace pluS with +
        pline = pline.replace("minuS", "-") #replace minuS with -
        pline = pline.replace("dividE", "/") #replace devidE with /
        pline = pline.replace("multiplY", "*") #replace multiplY with *
        pline = pline.replace("freespeech", "print") #replace freespeech with print
        pline = pline.split("||") #splits it from the |
        pline = f"{pline[0]}({pline[1]})" #makes a fstring and orders the elements between a bracket
        writeCom(f"{plineTabN}{pline}", XCount) #prints the line
      else: #if the line does not startswith freespeech
        pass #exit the function

    def detectFunctions(lineTOscan : str, XCount : int): #scans the passed line for a possible functions
      flineTabCount = 0 #reset the tabcount to zero
      fline = lineTOscan #reset the variable in a loop
      
      fline = lineTOscan.removesuffix('\n') #remove the new line
      
      flineTabCount = fline.count("  ") #getas the intendation count
      flineTabN = "  " * flineTabCount #repeats the string for the tabs
      fline = fline.replace("  ", "") #replace the tabs with NULL

      if fline.startswith("mindset"): #if the line startswith mindset
        fline = fline.replace("--", "#") #replace '--' with #
        fline = fline.replace(" (", ":") #replace ' (' with :
        fline = fline.replace("(", ":") #replace '(' with :
        fline = fline.replace(")", "") #replace ')' with Null
        fline = fline.replace("[", "(") #replace '[' with (
        fline = fline.replace("]", ")") #replace '[' with )
        fline = fline.replace("mindset", "def") #replace mindset with function
        writeCom(f"{flineTabN}{fline}", XCount) #prints the line
      else: #if the line does not startswith mindset
        pass #exit the function
    
    def detectIfStatements(lineTOscan : str, XCount : int): #scans the passed line for a possible if statements
      ilineTabCount = 0 #reset the tabcount to zero
      iline = lineTOscan #reset the variable in a loop
      
      iline = lineTOscan.removesuffix('\n') #remove the new line
      
      ilineTabCount = iline.count("  ") #getas the intendation count
      ilineTabN = "  " * ilineTabCount #repeats the string for the tabs
      iline = iline.replace("  ", "") #replace the tabs with NULL
      
      if iline.startswith("byAnyChance"): #if the line startswith byAnyChance
        iline = iline.replace("--", "#") #replace '--' with #
        iline = iline.replace("byAnyChance", "if") #replace byAnyChance with if
        iline = iline.replace("[", "") #replace [ with Null
        iline = iline.replace("]", "") #replace ] with Null
        iline = iline.replace("iz", "==") #replace iz with ==
        iline = iline.replace("NOCAP", "True") #replace NOCAP with True
        iline = iline.replace("CAP", "False") #replace CAP with False
        iline = iline.replace("NOTHING", "None") #replace NOTHING with None
        iline = iline.replace("isBeta", "<") #replace isBeta with <
        iline = iline.replace("isAlpha", ">") #replace isAlpha with >
        iline = iline.replace("isBe//z", "<=") #replace isBe//z with =<
        iline = iline.replace("isAl//z", ">=") #replace isAl//z with =>
        iline = iline.replace(" (", ":") #replace "(" with :
        iline = iline.replace("(", ":") #replace " (" with :
        iline = iline.replace(")", "") #replace ( with Null
        writeCom(f"{ilineTabN}{iline}", XCount) #prints the line
      else: #if the line does not startswith byAnyChance
        pass #exit the function
      
    def detectElseStatement(lineTOscan : str, XCount : int): #scans the passed line for a possible else statements
      elineTabCount = 0 #reset the tabcount to zero
      eline = lineTOscan #reset the variable in a loop
      
      eline = lineTOscan.removesuffix('\n') #remove the new line
      
      elineTabCount = eline.count("  ") #getas the intendation count
      elineTabN = "  " * elineTabCount #repeats the string for the tabs
      eline = eline.replace("  ", "") #replace the tabs with NULL
      
      if eline.startswith(") whenItsNot"): #if the line startswith whenItsNot
        eline = eline.replace("--", "#") #replace '--' with #
        eline = eline.replace("whenItsNot", "else") #replace whenItsNot with else
        eline = eline.replace("(", ":") #replace '(' with :
        eline = eline.replace(" (", ":") #replace ' (' with :
        eline = eline.replace(") ", "") #replace ( with Null
        writeCom(f"{elineTabN}{eline}", XCount) #prints the line
      else: #if the line does not startswith whenItsNot
        pass #exit the function
      
    
    def detectElifStatements(lineTOscan : str, XCount : int): #scans the passed line for a possible Elif statements
      eiline = lineTOscan #reset the variable in a loop
      eilineTabCount = 0 #reset the tabcount to zero (avoid loop recycling)
      
      eiline = lineTOscan.removesuffix('\n') #remove the new line at the end
      
      eilineTabCount = eiline.count("  ") #getas the intendation count
      eilineTabN = "  " * eilineTabCount #repeats the string for the tabs
      eiline = eiline.replace("  ", "") #replace the tabs with NULL
      
      if eiline.startswith(") ifNotByAnyChance"): #if the line startswith ifNotByAnyChance
        eiline = eiline.replace("--", "#") #replace '--' with #
        eiline = eiline.replace("ifNotByAnyChance", "elif") #replace ifNotByAnyChance with else
        eiline = eiline.replace("(", ":") #replace '(' with :
        eiline = eiline.replace(" (", ":") #replace ' (' with :
        eiline = eiline.replace(") ", "") #replace ( with Null
        eiline = eiline.replace("[", "") #replace [ with Null
        eiline = eiline.replace("]", "") #replace ] with Null
        eiline = eiline.replace("iz", "==") #replace iz with ==
        eiline = eiline.replace("NOCAP", "True") #replace NOCAP with True
        eiline = eiline.replace("CAP", "False") #replace CAP with False
        eiline = eiline.replace("NOTHING", "None") #replace NOTHING with None
        eiline = eiline.replace("isBeta", "<") #replace isBeta with <
        eiline = eiline.replace("isAlpha", ">") #replace isAlpha with >
        eiline = eiline.replace("isBe//z", "<=") #replace isBe//z with =<
        eiline = eiline.replace("isAl//z", ">=") #replace isAl//z with =>
        writeCom(f"{eilineTabN}{eiline}", XCount) #prints the line
      else: #if the line does not startswith ifNotByAnyChance
        pass #exit the function
    
        
    def detectBreakSyntax(lineTOscan : str, XCount : int): #scans the passed line for a possible brake synatxes
      blineTabCount = 0 #reset the tabcount to zero
      bline = lineTOscan #reset the variable in a loop
      
      bline = bline.removesuffix('\n') #remove the new line
      
      blineTabCount = bline.count("  ") #getas the intendation count
      blineTabN = "  " * blineTabCount #repeats the string for the tabs
      bline = bline.replace("  ", "") #replace the tabs with NULL
      
      if bline.startswith("cutThisShit"): #if the line startswith 'cutThisShit'
        bline = bline.replace("--", "#") #replace '--' with #
        bline = bline.replace("cutThisShit", "break") #replace 'cutThisShit' with break
        writeCom(f"{blineTabN}{bline}", XCount) #prints the line
      else: #if the line does not startswith cutThisShit
        pass #exit the function
    
    def detectEmptyLines(lineTOscan : str, XCount : int): #scans the passed line for a possible emptyline
      emline = lineTOscan #reset the variable in a loop  
      emline = emline.replace("  ", "") #replace the tabs with NULL
      if emline.startswith('\n'): #if line startswith newline
        writeCom("", XCount) #prints the line
      else: #if line does not startswith newline
        pass #exit the function
      
    def detectFunctionCallers(lineTOscan : str, XCount : int): #scans the passed line for a possible function caller
      cline = lineTOscan #reset the variable in a loop  
      clineTabCount = 0 #reset the tabcount to zero
      
      cline = lineTOscan.removesuffix('\n') #remove the new line at the end
      
      clineTabCount = cline.count("  ") #getas the intendation count
      clineTabN = "  " * clineTabCount #repeats the string for the tabs
      cline = cline.replace("  ", "") #replace the tabs with NULL
      
      if cline.startswith("activity"): #if the line startswith aactivity
        cline = cline.replace("activity ", "") #replace 'activity ' with null
        cline = cline.replace("--", "#") #replace '--' with #
        writeCom(f"{clineTabN}{cline}", XCount) #prints the line
      else: #if the line does not startswith activity
        pass #exit the function
      
    def detectQuitSyntaxes(lineTOscan : str, XCount : int): #scans the passed line for a possible quit syntaxes
      qline = lineTOscan #reset the variable in a loop
      lineTabCount = 0 #reset the tabcount to zero (avoid loop recycling)
      
      qline = lineTOscan.removesuffix('\n') #remove the new line at the end
      
      qlineTabCount = qline.count("  ") #getas the intendation count
      qlineTabN = "  " * qlineTabCount #repeats the string for the tabs
      qline = qline.replace("  ", "") #replace the tabs with NULL
      
      if qline.startswith("touchGrass"): #if the line startswith touchGrass
        qline = qline.replace("--", "#") #replace '--' with #
        qline = qline.replace("touchGrass", "quit") #replace 'touchGrass' with 'quit'
        writeCom(f"{qlineTabN}{qline}", XCount) #prints the line
      else: #if the line does not startswith touchGrass
        pass #exit the function
      
    
    def detectPassSyntaxes(lineTOscan : str, XCount : int): #scans the passed line for a possible pass syntaxes
      paline = lineTOscan #reset the variable in a loop
      palineTabCount = 0 #reset the tabcount to zero (avoid loop recycling)
      
      paline = lineTOscan.removesuffix('\n') #remove the new line at the end
      
      palineTabCount = paline.count("  ") #getas the intendation count
      palineTabN = "  " * palineTabCount #repeats the string for the tabs
      paline = paline.replace("  ", "") #replace the tabs with NULL
      
      if paline.startswith("ISkip"): #if the line startswith ISkip
        paline = paline.replace("--", "#") #replace '--' with #
        paline = paline.replace("ISkip", "pass") #replace 'ISkip' with 'pass'
        writeCom(f"{palineTabN}{paline}", XCount) #prints the line
      else: #if the line does not startswith ISkip
        pass #exit the function
      

    def detectContinueSyntaxes(lineTOscan : str, XCount : int): #scans the passed line for a possible continue syntaxes
      coline = lineTOscan #reset the variable in a loop
      colineTabCount = 0 #reset the tabcount to zero (avoid loop recycling)
      
      coline = lineTOscan.removesuffix('\n') #remove the new line at the end
      
      colineTabCount = coline.count("  ") #getas the intendation count
      colineTabN = "  " * colineTabCount #repeats the string for the tabs
      coline = coline.replace("  ", "") #replace the tabs with NULL
      
      if coline.startswith("KeepRollin"): #if the line startswith KeepRollin
        coline = coline.replace("--", "#") #replace '--' with #
        coline = coline.replace("KeepRollin", "continue") #replace 'KeepRollin' with 'continue'
        writeCom(f"{colineTabN}{coline}", XCount) #prints the line
      else: #if the line does not startswith KeepRollin
        pass #exit the function
      
      
    def detectBypassBlocks(lineTOscan : str, XCount : int): #scans the passed line for a possible bypass blocks
      bbline = lineTOscan #reset the variable in a loop
      bblineTabCount = 0 #reset the tabcount to zero (avoid loop recycling)
      
      bbline = lineTOscan.removesuffix('\n') #remove the new line at the end
      
      bblineTabCount = bbline.count("  ") #getas the intendation count
      bblineTabN = "  " * bblineTabCount #repeats the string for the tabs
      bbline = bbline.replace("  ", "") #replace the tabs with NULL
      
      if bbline.startswith("bypassBlock"): #if the line startswith bypassBlock
        bbline = bbline.replace("--", "#") #replace '--' with #
        bbline = bbline.split("||") #split the line from the |
        bbline = bbline[1] #gets the second part of the above split
        writeCom(f"{bblineTabN}{bbline}", XCount) #writes theline
      else: #if the line does not startswith bypassBlock
        pass #exit the function
      
      
    detectBypassBlocks(rotFileSys[lineCounter], lineCounter) #this is a test
    detectElifStatements(rotFileSys[lineCounter], lineCounter) #this is a test
    detectContinueSyntaxes(rotFileSys[lineCounter], lineCounter) #this is a test
    detectPassSyntaxes(rotFileSys[lineCounter], lineCounter) #this is a test
    detectQuitSyntaxes(rotFileSys[lineCounter], lineCounter) #this is a test
    detectFunctionCallers(rotFileSys[lineCounter], lineCounter) #this is a test
    detectEmptyLines(rotFileSys[lineCounter], lineCounter) #this is a test
    detectElseStatement(rotFileSys[lineCounter], lineCounter) #this is a test
    detectIfStatements(rotFileSys[lineCounter], lineCounter) #this is a test
    detectFunctions(rotFileSys[lineCounter], lineCounter) #this is a test
    detectPrintCommands(rotFileSys[lineCounter], lineCounter) #this is a test
    detectVariables(rotFileSys[lineCounter], lineCounter) #this is a test
    detectBreakSyntax(rotFileSys[lineCounter], lineCounter) #this is a test
    
    lineCounter += 1 #moves to the next line
    if lineCounter == len(rotFileSys): #if the linecouners value is equal to the number of lines
      print("")
      print("[+] Compiling Into .bpy Done!")
      print("[^] You can run your compiled file using the below command")
      print(f"[-] python {sys.argv[2]}.bpy")
      print("")    
      break #exit the loop
    else: #if the linecouners value is not equal to the number of lines
      continue #continue the loop


  
#############################
#       StartToRun          #
#############################

def runnerController():
  if validateROTfile() == True: #if the file validation is successful
    if checkInternetConnectivity() == True: #if internet connectivity is ok
      checkVersion() #chck the version
    else: #if internet connectivity is not ok
      pass #continue
    rConvert() #compile the file
    if sys.argv[3] == "Y" or sys.argv[3] == "y": #if the autorun argument is true
      os.system(f"python {sys.argv[2]}.bpy") #run the file
    elif sys.argv[3] == "N" or sys.argv[3] == "n": #if the autorun argument is false
      pass #continue
  else: #if the file validation fails
    print("Validation Failed!") #prints that it failed
    

runnerController()