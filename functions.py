#!/usr/bin/python/deskop/inspire with stem/functions.py

#######       functions
#       Name : Collins muli
#       Date : 18/6/2022
######################################

# function is a block of code executed together

# initializing a function
def say_hello():
    print("Hello from JKUAT NCBD ")
    x = 10
    y = 33
    z = x+y
    print(z)
say_hello()

# print function of sound made by 3 animals
def purr():
    print("Cats purr")
purr()

# function parameters(what the function requires)
# function to add 2 numbers
def add_numbers(x,y):
    sum_nums = x+y
    print("The sum of the numbers is",sum_nums)
add_numbers(77,33)

# function for product of two numbers
def prod(x,y):
    product = x*y
    print("The product is",product)
prod(99,15)

# using default parameters
def print_name(name = "Joseph"):    # print_name is the name of the function
    print(name)
print_name("Jesse")

# return from a function
def get_sum(num_1,num_2):
    sum_nums = num_1 + num_2
    return sum_nums
print(get_sum(74,56))

# write a function to get the powers of numbers
def powers(num,power):
    pow_num = num**power
    return pow_num
print(powers(10,4))

# print name
def get_full_name(f_name,s_name):
    full_name = f_name + " " + s_name
    return full_name.title()
print(get_full_name('Jesse','Annabel'))

#parsing a list in a function

def greet_friends(names):
    for name in names: 
        msg="Hello " + name.title() + "!"
        print (msg)
friends=['Cassidy','Deborah','Maikai','Racheal','Bond','Kendra']
greet_friends(friends)