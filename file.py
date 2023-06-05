num1 = 42 #int variable decleration
num2 = 2.3 #float variable decleration
boolean = True #boolean decleration
string = 'Hello World' # string decleration
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] # list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} # dictionary
fruit = ('blueberry', 'strawberry', 'banana')# tuple
print(type(fruit)) # checking data type (<class 'tuple'>)
print('++++++++++++++++++++++++++++')

print(pizza_toppings[1])# prints pizza toppings at index one ('Sausage')
print('++++++++++++++++++++++++++++')

pizza_toppings.append('Mushrooms') # adds 'mushrooms' to end of pizza_toppings list
print(person['name']) # prints John
print('++++++++++++++++++++++++++++')

person['name'] = 'George' # updates key-value
person['eye_color'] = 'blue' # adds new key-value pair to person dict.
print(fruit[2]) #prints (Banana)
print('++++++++++++++++++++++++++++')

if num1 > 45: # if else statment ..will print its lower
    print("It's greater")
else:
    print("It's lower")
print('++++++++++++++++++++++++++++')

if len(string) < 5: # checks how long a string is.. in this case Hello World is 11 so it'll print just right
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")
print('++++++++++++++++++++++++++++')

for x in range(5): # for loop that prints 1-4 in sequence (0,1,2,3,4)
    print(x)
print('++++++++++++++++++++++++++++')

for x in range(2,5): #for loop that  prints 2-4 increments by 1 = (2,3,4)
    print(x)
print('++++++++++++++++++++++++++++')

for x in range(2,10,3): #for loop that prints 2-10 incriments by 3 = (2,5,8) 
    print(x)
print('++++++++++++++++++++++++++++')


pizza_toppings.pop() #removes the last item in the list (olives)
pizza_toppings.pop(1) #removes the item at the first index in the list (sausage)

print(person) #prints the whole person dict
print('++++++++++++++++++++++++++++')

person.pop('eye_color') #removes eye_coler key
print(person) #prints person dict without eye_color key
print('++++++++++++++++++++++++++++')



"""
for loop that iterates thorugh the pizza_toppings list 
and keeps printing 'After 1st is statment' 
until it reaches olives
prints ('After 1st is statment 3 times')
"""
for topping in pizza_toppings: 
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break
print('++++++++++++++++++++++++++++')




"""
function that prints hello 10 times. range is set to 10 
so it'll start at 0 and go to 10 giving us 10 hello's
"""
def print_hello_ten_times():
    for num in range(10):
        print('Hello')

print_hello_ten_times()
print('++++++++++++++++++++++++++++')






"""
function that prints hello 4 times. range is set to 4 
so it'll start at 0 and go to 3 giving us 4 hello's
"""

def print_hello_x_times(x):
    for num in range(x):
        print('Hello')

print_hello_x_times(4)
print('++++++++++++++++++++++++++++')




"""
function that prints hello 14 times. range is set to x 
x is set to 10 
so it'll start at 0 and go to 10 giving us 10 hello's
and then x is set to 4  giving us 4 more Hello's
bringing the total to 14 hello's
"""


def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)