# **5. "byAnyChance" Statements.**
The `byAnyChance` statement is a logic statement that compares two or more objects or conditions just like an `If` statement from any other language.

## **5.1 Syntax Structure of `byAnyChance`.**
The syntax structure of `byAnyChance` is just a little bit complex but it's not impossilbe to understand. lets take a look at it's structure.

```brainrot
byAnyChance [<logic>]( --logic is a simple comparison
  --your process
  freespeech||"test"
)
```
The `<logic>` is not a Brain-rot feature or anything it represets thet there is a logic statement there.

### **<u>5.1.1 Oparators</u>**
The logic's default state is on true and it can consist of below operators.
<h4>


- **`iz`** - equal

- **`izNOT`** - does not equal

- **`isBeta`** - is smaller than

- **`isAlpha`** - is grater than

- **`isBe//z`** - smaller or equal than

- **`isAl//z`** - greater or equal than

- **`NOCAP`** - True

- **`CAP`** - False

- **`NOTHING`** - None
</h4>

You can use the above operators in anyway you want inside a `byAnyChance` statement. 

Examples :
```brainrot
make number be 14

byAnyChance [number iz 14]( 
  --only runs if the number equals to 14
  freespeech||"Yes"
)
```

<br>
<h5 align="right">© Official Brain-Rot Doucumentation.</h5>
<br>

#
# <center>_**The End of This Page**_</center>

#### <center align="right">[Next >>](./whenItsNot.md)</center>