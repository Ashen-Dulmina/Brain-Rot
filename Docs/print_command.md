# **1. Print Command in Brain-rot**
Like any other programming language out there Brain-rot has it's own print function. This page contains all the infomation on how to use the print command in Brain-rot.

## **1.1 Syntax Structure.**
The print function in brainrot is called `freespeech`. you can use `freespeech` to output anything onto the console. This function is backed by python and its structure is simple. you can use `freespeech` just like below.

```brainrot
freespeech||"Skibidi Ohio Rizzler!" --prints a string
```

As you can see the above line will print the text string "Skibidi Ohio Rizzler!" into the console. You can use any other data type like an `int`, `float` or a `boolean` by using `freespeech`.

```brainrot
freespeech||"Skibidi Ohio Rizzler!" --string
freespeech||12 --integer
freespeech||2.5 --float
freespeech||CAP --boolean
freespeech||NOCAP --boolean
```

## **1.2 Special Rules When Using `freespeech` .**
Because of the unique struncture of Brain-rot, You must follow few rules when using the  `freespeech` command.

### <u>**1.2.1 Only Use the Word  "freespeech" once.**</u>
The word  `freespeech` must only be used once and that is when using the commands name only. But if you include the word  `freespeech` even as a text string or a variable, It will be detected by the compiler as a command and it would be converted into `print`. So if you want to use the word  `freespeech` use the word like defined below.
```plaintext
"FreeSpeech"
"free speech"
"free-speech"
```

### <u>**1.2.2 Dont Use "||" Two Times in The Same Line.**</u>
Like `freespeech` the double bars shouldn't be repeated as it is a seperating syntax and everything after the second `||` would be void as the compiler would usually split the line into 2 parts from `||` to seperate the command and the value. but when adding a 2nd `||` the line would be split into 3 parts instead of 2 and the converter would only convert the 1st two parts. so the compiler wouldn't notice the value after the 2nd `||` .

Example :
```brainrot
freespeech||1234||5678 --"5678" part will be void
```
Output :
```terminal
1234
```

### <u>**1.2.3 `freespeech` Has intergrated `bypassBlock` Support.**</u>
<img src="./Assets/advance_warning.png" alt="Read this part only after reading the bypassblocks documentation but for beginers ignoring this rule would be fine as it cointains infomation needed when advancing more using Brain-rot." height="150">

When using `bypassBlock`s with print command don't use `bypassBlock`s seperately. Instead use the `bypass Block`s without using the `bypassBlock` command. `freespeech` has integrated `bypassBlock` support.

Example :
```brainrot
freespeech||bypassBlock||sys.argv[1] --Wrong/Error

freespeech||sys.argv[1] --Correct
```

<br>
<h5 align="right">© Official Brain-Rot Doucumentation.</h5>
<br>

#
# <center>_**The End of This Page**_</center>

#### <center align="right">[Next >>](./variables.md)</center>