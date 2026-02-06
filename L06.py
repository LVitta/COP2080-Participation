"""
## Problem 1
## Modify the following code to use both functions as decorators
# strip off dashes
def strip_string(b_function):
    def wrapper():
        func = b_function()
        strip_string = func.strip('-')
        return strip_string
    return wrapper

#create upper case version of clli code
def uppercase_decorator(some_function):
    def a_wrapper():
        func = some_function()
        make_uppercase = func.upper()
        return make_uppercase

    return a_wrapper

@uppercase_decorator
@strip_string
def clli_code():
    print('The Florida router clli code is', end = '')
    return '---tpaflxacg19----'

print(clli_code())
"""
"""
## Problem 2
## Create mapped tuples of letter to numeric grades in the lambda function
## Wrap the lambda function with a list function and also apply unpack operator to 'a' parameter
## In this context it is being used as an 'arbitrary qty of arguments'
# map.grades.py
# product list of tuples
grades = [95, 88, 85, 75]
letter_grade = ['A', 'B+', 'B', 'C']

print('The original list ',letter_grade)
print('The zipped tuples ', list(zip(letter_grade, grades)))
print('Next is a map-lambda version')

map_lamda = list(map(lambda *a: a, letter_grade, grades)) # equivalent to zip
print(map_lamda)
"""
"""
## Problem 3
## Modify the code below that chacks index 0 of x,
##  and converts the character to upper case to test against clli names that start with either 'F' or 'C'.
## Lambda should display only 3 clli codes located in florida or california
## Start by applying filer() function to the existing lambda function.
## Then, wrap that with a list() function to unpack into iterables.
## Next, wrap all of that in a print() function to display the list.

# filter_clli.py
# returns only clli codes located in Florida or California
clli_names = ['flxa99443oc', 'gaxb32443oc', 'caxo99323oc',
'flxa11443ds']
print(list(filter(lambda x: x[0].upper() in 'FC', clli_names)))
"""
"""
## Problem 4
## Complet the list comprehension to produce the result (in blue) in which x never creates a two-tuple with y if they are equivalent
## Replace each underscore with the appropriate python keyword
# list_comp1.py
print([(x, y) for x in ['a', 'b', 'c'] for y in ['first','b', 3] if x!=y])
"""
"""
## Problem 5
## code golf is where you try to get the shortest possible source code to solve a problem
## The following code checks a list for negative values
## If a negative value is found, the function returns the positive value of the found number
## Demonstrate the efficiency of python by revising the 8 lines of code into two lines to produce the same result
# conv_neg_pos_nocomp.py
a_list = [7, 5, -4, 6]
print(list(map(lambda x: abs(x), a_list)))
"""

## Problem 6
## Correct the code implement a generator comprehension for 'b' that produces the same list of 1 million values as does the list comprehension
## Generator expressions use () instead of [] braces
## Note the difference in memory using a list vs a generator
# listcomp_vs_genexp.py
# list comprehension vs generator expression
import sys
a = [x for x in range(1000000)] #list comp
b = (x for x in range(1000000)) #generator expr
print('list comp byte size is ',sys.getsizeof(a))
print('generator expression byte size is ',sys.getsizeof(b))