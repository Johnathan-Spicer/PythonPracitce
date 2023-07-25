import math
import time
import random
import os
# # first_Name = 'Johnathan'
# # last_Name = 'Spicer'
# # full_Name = first_Name + " " + last_Name
# # print("Hello " + full_Name)
# # #print(type(name))
# # #print("Hello " + name)

# # age = 16
# # age += 1
# # print(age)
# # print(type(age))

# # name = 'Johnathan'
# # age = 16
# # attractive = True

# # name, age, attractive = 'Johnathan', 16, True

# # print(name, age, attractive)
# # len = length, find, capitalize, upper, lower, isdigit, isalpha, count, replace

# # name = input("What is your name?: ")
# # age = int(input("How old are you?: "))
# # height = float(input("How tall are you?: "))

# # print("Hello "+name + " " + "You are "+str(age)+" years old" + " " + "You are " +str(height)+"cm tall")

# #round = rounds the number to the nearest full int
# #math.ceil = rounds up to the nearest int so 3 would = to 4
# #math.floor = rounds down to the nearest int
# #abs = tells you how far away the number is from zero
# #pow = raise base number to a power so for example
# #3 to the power of 2 is 9
# #math.sqrt = short for square root
# #max finds the largest value
# #min finds the smallest value

# # name = ""
# # while len(name) == 0:
# #   name = input("Enter your name please: ")
# # print("Hello " + name)

# # #while loop = unlimited
# # #for loop = limited

# # # for i in range(10):
# # #   print(i+1)

# # for seconds in range(10,0,-1):
# #   print(seconds)
# #   time.sleep(1)
# # print("Happy New Year!")

# # rows = int(input("How many rows?: "))
# # columns = int(input("How many columns?: "))
# # symbol = input("Enter a symbol to use: ")

# # for i in range(rows):
# #   for j in range(columns):
# #     print(symbol, end="")
# #   print()

# # while True:
# #   name = input("Enter your name")
# #   if name != "":
# #     break

# # phone_number = "123-456-7890"

# # for i in phone_number:
# #   if i == "-":
# #     continue
# #     print(i, end="")

# # for i in range(1, 21):
# #   if i == 13:
# #     pass
# #     else:
# #       print(i)

# # food = ["pizza", "burger", "sushi", "steak"]
# # # food[0] = "bagel"
# # # print(food[0])
# # # food.append("ice cream")
# # #food.pop()

# # for x in food:
# #   print(x)

# def add(*args):
#   sum = 0
# args = list(args)
# args[0] = 0
#   for i in args:
#     sum += i 
#   return sum
# print(add(1,2,3,4,5,6))  


# ------------ kwargs ------------

# def hello(**kwargs):
#  # print("Hello " + kwargs['first'] + " " + kwargs['last'])
#  print("Hello", end=" ")

# for key,value in kwargs.items():
#   print(value,end=" ")

# hello(first="Johnathan",middle="James",last="Spicer")

# animal = "cow"
# item = "moon"
# print("The {} jumped over the {}".format(animal, item))
# print("The {0} jumped over the {1}".format(animal, item))
# print("The {animal} jumped over the {item}".format(animal="cow", item="moon"))

# x = random.randint(1,6)
# y = random.random()
# myList = ['rock', 'scissors', 'paper']
# z = random.choice(myList)
# cards = [1,2,3,4,5,6,7,8,9,"J","Q","K","A"]
# random.shuffle(cards)
# print(cards)

# class Car:

#  wheels = 4 # Class Variable

#   def __init__(self,make,model,year,color):
#   self.make = make  #Instance variable
#   self.model = model #Instance variable
#   self.year = year #Instance variable
#   self.color = color #Instance variable

#   def drive(self):
#     print("this " +self.model+" is driving")
#   def stop(self):
#     print("This "+self.model+" has stopped")

# class Animal:

#   alive = True

#   def eat(self):
#     print("This animal is eating")

#   def sleep(self):
#     print("This animal is sleeping")

# class Rabbit(Animal):
#   pass  
# class Fish(Animal):
#   pass
# class Human(Animal):
#   pass

# rabbit = Rabbit()
# fish = Fish()
# human = Human()

# print(rabbit.alive)
# fish.eat()
# human.sleep()