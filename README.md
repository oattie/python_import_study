# Synopsis

Importing modules and packages are quite confusing as they have 
different ways of imporing in Python 2 and 3
This study will cover only Python 3 contents but from time to time 
Python 2 will be mentioned.

## Why do we have to import in Python?
1. Sometimes, you want to organise your code and have other some code in 
other **modules**; you dont want to write 5,000 lines of code in a 
module, do you?
2. If you write Python in `OPP` style you may want to create a **module** 
per class. And therefore, you can end of with numerous of **modules**.
3. You want to group your **modules** in to **packages** or 
**subpackages**. So, when you want to use them again, you can just import them. No `CTRL+C` and 
`CTRL+V`.
4. For fun :)

## Hang on.. What's module and package and what's the difference between them?

Great, if you have these questions that means you are critically reading 
this repo. Well done lad! 
```
A module: It is a file, essentially `<<script>>.py`
A package: A folder which contains one or more modules
```
Ok, now if we want to try out these terminologies, this is when fun get 
started.

Between Python 2 and 3.3 may not be clever enough to automatically detect a 
folder as a package. Therefore you need an empty `__init__.py` in the 
folder to tell Python interpreter that this is a package.

