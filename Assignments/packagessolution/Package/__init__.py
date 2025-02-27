'''
To create an packages, we have to :
1. Create a folder 
2. Make a " __init__.py " file (its neccessary even if you dont want to write anything inside it)
3. Create the package by making another file below this file (like here i created "operations")
4. After creating package import it as you know
'''

from .module1 import add
from .subpackage.module2 import mult