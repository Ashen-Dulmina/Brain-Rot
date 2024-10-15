# **2. Variables in Brain-rot**
Like any other programming language out there Brain-rot has it's own method for defining variables. This page contains all the infomation on how to define a variable and use them in Brain-rot.

## **2.1 Defining Variables.**
You can easyly define a varable in Brain-rot by using `make` and `be` keywords in the correct order as below.
```brainrot
make this be "Value" --defines variable this as "Value"
```
That is the most basic way of defining a variable there are many other data types that caan be used as variables.

```brainrot
make text be "Skibidi Ohio Rizzler!" --string
make number be 14 --integer
make decimal be 6.9 --float
make yes be NOCAP --boolean : True
make no be CAP --boolean : False
make empty be NOTHING --None/Empty variable
```

## **2.2 Special Rules When Using Variables.**
Because of the syntaxing structure of Brain-rot there are special rules that should be followed when working with variables.

### **<u>2.2.1 Don't Use `be` Two Times.</u>**
The variable's syntax structure consist of 2 required syntaxes. They are `make` and `be`.When the compiler calls the converter and the `be` in detected variables are translated into = if there are 2 `be`'s in one variable line and it may cause an error.

For Example :

When you use the below line
```brainrot
make this be "Toby be Updog" 
```

<br>
<h5 align="right">© Official Brain-Rot Doucumentation.</h5>
<br>

#
# <center>_**The End of This Page**_</center>

#### <center align="right">[Next >>](./compiler_and_cli.md)</center>