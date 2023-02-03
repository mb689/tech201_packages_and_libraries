# Modules

import os
import math, datetime, sys

working_directory = os.getcwd()
print(working_directory)

def return_user_id():
    print(os.getpid())

def return_user_name():
    print(os.name())

print(datetime.date.today())
print(sys.path)
print(math.remainder(1, 5))


# When you are building a program, it's really important to think whether you need to make an class/object or a simply a function. You may not need to make a function yourself, if there is a module that does what you are looking for already.

# Built-in functions

# print()
# len()
# type()