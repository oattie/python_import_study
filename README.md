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

A module: It is a file, essentially `<<script>>.py`

A package: A folder which contains one or more modules

Ok, now if we want to try out these terminologies, this is when the fun get 
started.

Between Python 2 and 3.3 may not be clever enough to automatically detect a 
folder as a package. Therefore you need an empty `__init__.py` in the 
folder to tell Python interpreter that this is a package.

For example, considering your Python project is structured below:

```
projects
  -> etl
    -> __init__.py
    -> etl_control.py
```

This means you explicitly want Python to interpret this etl folder as a package which contains `etl_control` module.

## Things're changed a bit for Python 3.3+
We no longer need to put `__init__.py` in a folder when creating a package because of [implicit namespace packages](https://www.python.org/dev/peps/pep-0420/). Hurayyyyyyyyyyy!!!

## But what does Python do when searching a module/package really?
Python will do following steps when importing a module/package:
1. It puts built-in modules in a search path ( For example time, sys etc....). There are a list of built-in modules defined which can be found by `sys.builtin_module_names`
2. It finds a package (folder) and a file with the same name of import and puts them in the search path.
3. It put other Python standard libraries or packages in the search path

For example, considering the following structure of a Python project:

```
projects
  main.py
  -> etl
    -> __init__.py
    -> etl_control.py
```

Let's assume that we want to run `main.py` directly and inside `main.py`, it imports etl_control module. 
The Python interpreter will search for built-in packages and put them in a search path, then put the directory of `main.py` in the search path and then put other Python standard libraries/packages into the search path.

So, when you do run the following code, you will see that the `sys.path[0]` will show you the `projects` folder which is the current directory of `main.py`

```
import sys
print(sys.path[0])
```

Now it is **CRUCIAL** to understand that when we do `import etl_control` module in `main.py`, Python only cares the directory of `main.py` (a current directory of a running file) and not the working directoy nor the directory of `etl_control.py`

