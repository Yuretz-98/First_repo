"""print("Hello world") #first programm
print("Hello Git")"""

"""
#list work
my_list =  ["apple", "banana", "cherry"]
my_list[1] = "blueberry"
my_list.append("orange")
my_list.insert(0, "grape")
del my_list[1]
print(my_list) """



""""
# dictionary
my_dict = {"name": "Олексій", "age": 31}
my_dict["email"] = "oleksiy@gmail.com"
del my_dict["age"]
print(my_dict)    
"""
"""
my_dict = {"name": "Степан", "age": 65}

if my_dict["age"] <= 18:
    print("Вибачте, ви ще не маєте права голосу")
elif my_dict["age"] >= 65:
    print("Ви маєте право на пенсію")
else:
    print("Ви повнолітній, але ще не маєте права на пенсію")

"""


"""
#Cycle
fruits = ["яблуко", "банан", "вишня"]
for fruit in fruits:
    print(fruit)

"""

"""
sentence = "The quick brown fox jumps over the lazy dog"
length = 0
for i in sentence:
    if i != " ":    
        length = length + 1
print(length)
"""

"""
#range

summary = 0

for i in range(0, 101):
    summary = summary + i
print(summary)
"""
"""
#while
count = 0
while count <= 5:
    print("Число:", count)
    count = count + 1
"""

"""
N = 10
sum_squares = 0
i = 1
while i <= N:
    sum_squares = i*i + sum_squares
    i = i + 1

print(f"The sum of the squares of numbers from 1 to {N} is {sum_squares}")
"""

"""
#FUNCTION
def say_hello():
    print("Hello, world!")

say_hello()
"""
"""
def print_message(message):
    print(message)

print_message("Це повідомлення з функції.")
"""

"""
#Return Функції можуть "повертати" значення за допомогою ключового слова return. Після return функція припиняє своє виконання і повертає вказане значення.
def add_numbers(a, b): #Присвоюємо аргументи ф-ії
    return a + b #Очікуваний результат(типу завдання для цих аргументів)

result = add_numbers(7, 3) # Присвоюємо значення для аргументів.
print(result)  
"""

"""
N = 10

def function(n):
    sum_squares = 0
    i = 1
    while i <= n:
        sum_squares = sum_squares + i * i
        i = i + 1
    return sum_squares
result = function(N)
print(result)

"""


#РЯДКИ
""""
first_name = "Олексій"
last_name = "Гупало"
full_name = first_name + " " + last_name
print(full_name)
"""
"""
first_name = "John"
last_name = "Doe"

def get_fullname(a, b):
    return a + " " + b

fullname = get_fullname(first_name, last_name)
print(fullname)
"""

# number of characters(кількість символів)
"""
first_name = "Олексій"
last_name = "Гупало"
full_name = first_name + " " + last_name
print(len(full_name))
"""
"""
#  Перший за ындексо 0 та 3 з кінця за індексом -з
first_name = "Oleksiy"
last_name = "Gupalo"
full_name = first_name + " " + last_name
length = len(full_name)
print(full_name[0])
print(full_name[length - 3])
"""

"""
first_name = "John"
last_name = "Doe"


def get_initials(a, b):
    return a + " " + b[0] + "."


formatted_name  = get_initials(first_name, last_name)
print(formatted_name)
"""

"""
#Регістри: lower(нижній), upper(верхній).
text = "Python"
print(text.upper())  

# без пробілів
text = "  hello  "
print(text.strip())

"""

"""
first = "Python"
second = "python"


def compare(first, second):
   return first.lower() == second.lower()
result = compare(first, second)
print(result)
"""

"""
# Для пошуку в рядках використовуємо метод find(sub). 
# Він шукає підрядок sub у рядку і повертає індекс його першої появи. Якщо підрядок не знайдено, то метод повертає -1.
#  Це корисно для знаходження позиції підрядка в більшому рядку.

text = "Hello, world!"
print(text.find("world")) 
print(text.find("Python"))  

"""

"""
# Останній метод який ми розглянемо, це replace(old, new). 
# Він замінює всі входження підрядка old на підрядок new у рядку. 
# Це дозволяє легко замінювати одну частину тексту на іншу.
text = "I like cats"
new_text = text.replace("cats", "dogs")
print(new_text)  
"""

"""
text = "Hello, world! Welcome to the world of Python."

position = text.find("world")

updated_text = text.replace("world", "planet")

print(position)
print(updated_text)
"""

"""
#Також давайте розглянемо форматування рядків. Форматування рядків дозволяє вставляти змінні або вирази всередину рядка.
#  Воно дозволяє вставляти вирази всередину рядкових літералів, використовуючи префікс f перед початком рядкового літерала. 
# Для використання f-рядків, просто додайте f безпосередньо перед початковими лапками рядка. 
# Всередині цього рядка ви можете вставляти змінні, вирази або виклики функцій у фігурних дужках {}.
name = "Олексій"
age = 30
greeting = f"Мене звати {name}, і мені {age} років."
print(greeting)
"""
"""
product_name = "Coffee Maker"
product_price = 7500.50
product_quantity = 15


def format_product_info(name, price, quantity):
    return f"Product: {name}, Price: {price} UAH, Quantity: {quantity} pcs."
product_info = format_product_info(product_name, product_price, product_quantity)
print(product_info)
"""

#CLASS 

"""
class Dog:
    # Атрибут класу
    species = "Canis familiaris"

    def __init__(self, name, age):
        # Атрибути екземпляру
        self.name = name
        self.age = age
"""

"""
class Dog:
    # Атрибут класу
    species = "Canis familiaris"

    def __init__(self, name, age):
        # Атрибути екземпляру
        self.name = name
        self.age = age
"""

"""
class Car:
    vehicle_type = "Automobile"

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def get_info(self):
        return f"{self.year} {self.make} {self.model}, Type: {Car.vehicle_type}"
"""
"""
class Car:
    vehicle_type = "Automobile"

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_info(self):
        return f"{self.year} {self.make} {self.model}, Type: {Car.vehicle_type}"
        
car_ford = Car("Ford", "Mustang", 2022)
car_toyota = Car("Toyota", "Corolla", 2021)

print(car_ford.get_info())
print(car_toyota.get_info())
"""

first_name ="Yuriy "
last_name ="Popov"
full_name = first_name + last_name
print(full_name)