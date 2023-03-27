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

# Comando para imprimir en consola: /home/gitpod/.pyenv/shims/python /workspace/pythonbestpractice/index.py
# Click derecho sobre el file que se quiere ver en la terminal y elegir la opcion: "Run Python File in Terminal"