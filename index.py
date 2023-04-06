# ejercicio 1 **********************************************************

print("Hola Ekain")

# ejercicio 2 **********************************************************

color = "Yellow"

print(color)

# ejercicio 3 **********************************************************

age = int(input('What is your age?\n'))
# CHANGE THE CODE BELOW TO ADD 10 TO AGE
age = age + 10

print("Your age is: "+str(age))

# ejercicio 4 **********************************************************

# Set the values for my_var1 and my_var2 here
my_var1 = 'Hello'

my_var2 = 'World'

## Don't change below this line
the_new_string = my_var1+' '+my_var2
print(the_new_string)

# ejercicio 5 **********************************************************

a = '</title>'
b = '</html>'
c = '<head>'
d = '</body>'
e = '<html>'
f = '</head>'
g = '<title>'
h = '<body>'

# ⬆ DON'T CHANGE THE CODE ABOVE ⬆
# ↓ start coding below here ↓

html_document = e+c+g+a+f+h+d+b

print(html_document)

# ejercicio 6 **********************************************************

total = int(input('How much money do you have in your pocket\n'))

# YOUR CODE HERE
if total > 100: 
    print('Give me your money!')
elif total > 50:
    print('Buy me some coffee you cheap')
else: 
    print('You are poor guy, go away')

# ejercicio 7 ********************************************************** 

user_input = int(input('How many people are coming to your wedding?\n'))

if user_input <= 50:
    price = 4000
elif user_input <= 100:
    price = 10000
elif user_input <= 200:
    price = 15000
else:
    price = 20000

print('Your wedding will cost '+str(price)+' dollars')

# ejercicio 8 ********************************************************** 

import random

def get_randomInt():
  	# CHANGE ONLY THIS LINE BELOW
	random_number = random.randint(1, 10)
	return random_number

print(get_randomInt())

# ejercicio 9 ********************************************************** 

def is_odd(my_number):
  	return (my_number % 2 != 0)


def my_main_code():
    my_number = 45345
    print(is_odd(my_number))

# ejercicio 10 ********************************************************** 

def sum(number1,number2):
    return number1 + number2

total = sum(2,3)
super_duper = sum(3445324, 53454423)
print(total)
print(super_duper)

# ejercicio 11 ********************************************************** 

# Define the function called "multi" that expects 2 parameters:
def multi(num1, num2):
    return num1 * num2
# don't edit anything below this line
return_value = multi(7,53812212)
print(return_value)

# ejercicio 12 ********************************************************** 

# declarando una función normal para una multiplicación
def multiply(p1, p2):
    return p1 * p2

# declarándola en una línea como una función lambda
multiply = lambda p1,p2: p1 * p2

# ejercicio 13 **********************************************************

is_odd = lambda num: (num % 2) != 0

# ejercicio 14 **********************************************************

multy = lambda x, y: x * y
print(multy(2,2))

# ejercicio 15 **********************************************************

rapid = lambda rapid_name: rapid_name[:-1]

# From this line above, plese do not change code below
print(rapid("bob")) #should print bo

# ejercicio 16 **********************************************************

# Comando para imprimir en consola: /home/gitpod/.pyenv/shims/python /workspace/pythonbestpractice/index.py
# Click derecho sobre el file que se quiere ver en la terminal y elegir la opcion: "Run Python File in Terminal"