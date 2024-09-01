#This is the official compiler for BRAINROT
#extetion '.rot'
#User interaction Keys :-
# [!] = error
# [^] = comment
# [-] = instruction
# [*] = pass (this means something is ok or good)

import sys
import os

#############################
#    validatingROTfiles     #
#############################

def validateROTfile(): #validates the file before reading and compiling
  if len(sys.argv) < 2 : #checks if the number of arguments is less than 2
    print("[!] Minus Aura detected ! ...")
    print("[!] Brainrot Compiler needs one or more arguments to oparate.")
    print("[!] No argument has been passed to the compiler.")
    print("[-] Brainrot <filename.rot>") #error message for no arguments
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
#        Read&Convert       #
#############################

def rConvert(): #this function read and converts things into python
  rotFileSys = open(sys.argv[1], 'r').readlines() #gets the rot file from args and reads it line by line
  convPyFile = f"{sys.argv[1].removesuffix('.rot')}.py" #converts the filename to a .py file
  
  #test loop
  lineCounter = 0 #the line counter component
  while True:
    rotFileSys = open(sys.argv[1], 'r').readlines() #redefined for optimization
    #print(rotFileSys[lineCounter]) #print that line
    
    def detectVariables(lineTOscan): #scans the passed line for a possible variable
      line = lineTOscan #reset the variable in a loop
      if lineTOscan.endswith('\n'): #if line endswith a newline 
        line = lineTOscan.removesuffix('\n') #remove the new line
      else: #if the line does not end with a newline
        pass #continue
      
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
        line = line.replace("devidE", "/") #replace devidE with /
        line = line.replace("multiplY", "*") #replace multiplY with *
        print(line) #prints the line
      else: #if the line does not startswith make 
        pass #exit the function
    
    def detectPrintCommands(lineTOscan): #scans the passed line for a possible print commands
      pline = lineTOscan #reset the variable in a loop
      if lineTOscan.endswith('\n'): #if line endswith a newline 
        pline = lineTOscan.removesuffix('\n') #remove the new line
      else: #if the line does not end with a newline
        pass #continue
      
      pline = pline.replace("  ", "") #replace the tabs with NULL
      
      if pline.startswith("freespeech"): #if the line startswith freespeech
        pline = pline.replace("--", "#") #replace '--' with #
        pline = pline.replace("freespeech", "print") #replace freespeech with print
        pline = pline.split("|") #splits it from the space
        pline = f"{pline[0]}({pline[1]})" #makes a fstring and orders the elements between a bracket
        print(pline) #prints the line
      else: #if the line does not startswith freespeech
        pass #exit the function

    def detectFunctions(lineTOscan): #scans the passed line for a possible functions
      fline = lineTOscan #reset the variable in a loop
      if lineTOscan.endswith('\n'): #if line endswith a newline 
        fline = lineTOscan.removesuffix('\n') #remove the new line
      else: #if the line does not end with a newline
        pass #continue
      
      fline = fline.replace("  ", "") #replace the tabs with NULL

      if fline.startswith("mindset"): #if the line startswith mindset
        fline = fline.replace("--", "#") #replace '--' with #
        fline = fline.replace(" (", ":") #replace ' (' with :
        fline = fline.replace("(", ":") #replace '(' with :
        fline = fline.replace(")", "") #replace ')' with Null
        fline = fline.replace("[", "(") #replace '[' with (
        fline = fline.replace("]", ")") #replace '[' with )
        fline = fline.replace("mindset", "def") #replace mindset with function
        print(fline) #prints the line
      else: #if the line does not startswith mindset
        pass #exit the function
    
    def detectIfStatements(lineTOscan): #scans the passed line for a possible if statements
      iline = lineTOscan #reset the variable in a loop
      if lineTOscan.endswith('\n'): #if line endswith a newline 
        iline = lineTOscan.removesuffix('\n') #remove the new line
      else: #if the line does not end with a newline
        pass #continue
      
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
        iline = iline.replace("isBe//z", "=<") #replace isBe//z with =<
        iline = iline.replace("isAl//z", "=>") #replace isAl//z with =>
        iline = iline.replace(" (", ":") #replace "(" with :
        iline = iline.replace("(", ":") #replace " (" with :
        iline = iline.replace(")", "") #replace ( with Null
        print(iline) #prints the line
      else: #if the line does not startswith byAnyChance
        pass #exit the function
      
    def detectElseStatement(lineTOscan): #scans the passed line for a possible else statements
      eline = lineTOscan #reset the variable in a loop
      if lineTOscan.endswith('\n'): #if line endswith a newline 
        eline = lineTOscan.removesuffix('\n') #remove the new line
      else: #if the line does not end with a newline
        pass #continue
      
      eline = eline.replace("  ", "") #replace the tabs with NULL
      
      if eline.startswith(") whenItsNot"): #if the line startswith whenItsNot
        eline = eline.replace("--", "#") #replace '--' with #
        eline = eline.replace("whenItsNot", "else") #replace whenItsNot with else
        eline = eline.replace("(", ":") #replace '(' with :
        eline = eline.replace(" (", ":") #replace ' (' with :
        eline = eline.replace(") ", "") #replace ( with Null
        print(eline) #prints the line
      else: #if the line does not startswith whenItsNot
        pass #exit the function
        
    def detectBreakSyntax(lineTOscan): #scans the passed line for a possible brake synatxes
      bline = lineTOscan #reset the variable in a loop
      if bline.endswith('\n'): #if line endswith a newline 
        bline = bline.removesuffix('\n') #remove the new line
      else: #if the line does not end with a newline
        pass #continue
      
      bline = bline.replace("  ", "") #replace the tabs with NULL
      
      if bline.startswith("cutThisShit"): #if the line startswith 'cutThisShit'
        bline = bline.replace("cutThisShit", "break") #replace 'cutThisShit' with break
        print(bline) #prints the line
      else: #if the line does not startswith cutThisShit
        pass #exit the function
    
    def detectEmptyLines(lineTOscan): #scans the passed line for a possible emptyline
      emline = lineTOscan #reset the variable in a loop  
      emline = emline.replace("  ", "") #replace the tabs with NULL
      if emline.startswith('\n'): #if line startswith newline
        print('') #prints the line
      else: #if line does not startswith newline
        pass #exit the function
    
    detectEmptyLines(rotFileSys[lineCounter]) #this is a test
    detectElseStatement(rotFileSys[lineCounter]) #this is a test
    detectIfStatements(rotFileSys[lineCounter]) #this is a test
    detectFunctions(rotFileSys[lineCounter]) #this is a test
    detectPrintCommands(rotFileSys[lineCounter]) #this is a test
    detectVariables(rotFileSys[lineCounter]) #this is a test
    detectBreakSyntax(rotFileSys[lineCounter]) #this is a test
    
    lineCounter += 1 #moves to the next line
    if lineCounter == len(rotFileSys): #if the linecouners value is equal to the number of lines
      break #exit the loop
    else: #if the linecouners value is not equal to the number of lines
      continue #continue the loop


  
############
############
############
if validateROTfile() == True:
  rConvert()
else:
  print("Validation Failed!")