# #This is a comment
# print("Hello, World!")
#
# #Variables
# x = 5
# y = "John"
# print(x)
# print(y)
#
# x, y, z = "Orange", "Banana", "Cherry"
# print(x)
# print(y)
# print(z)
#
# x = "Python"
# y = "is"
# z = "awesome"
# print(x, y, z)
#
# #Global Variable
# x = "awesome"
#
# def myfunc():
#   x = "fantastic"
#   print("Python is " + x)
#
# myfunc()
#
# print("Python is " + x)
#
# #Type Conversion
# x = 1    # int
# y = 2.8  # float
# z = 1j   # complex
#
# #convert from int to float:
# a = float(x)
#
# #convert from float to int:
# b = int(y)
#
# #convert from int to complex:
# c = complex(x)
#
# print(a)
# print(b)
# print(c)
#
# print(type(a))
# print(type(b))
# print(type(c))
#
# #if-else condition
# a = 200
# b = 33
# if b > a:
#   print("b is greater than a")
# elif a == b:
#   print("a and b are equal")
# else:
#   print("a is greater than b")
#
# a = 330
# b = 330
# print("A") if a > b else print("=") if a == b else print("B")
#
# a = 200
# b = 33
# c = 500
# if a > b or a > c:
#   print("At least one of the conditions is True")
#
# x = 41
#
# if x > 10:
#   print("Above ten,")
#   if x > 20:
#     print("and also above 20!")
#   else:
#     print("but not above 20.")
#
#
# #for loop
# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   print(x)
#
# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   if x == "banana":
#     break
#   print(x)
#
# for x in range(6):
#   print(x)
# else:
#   print("Finally finished!")

# #Array
# cars = ["Ford", "Volvo", "BMW"]
# x = cars[0]
#
# x = len(cars)
#
# for x in cars:
#   print(x)
#
# cars.append("Honda")
#
# cars.pop(1)
#
# cars.remove("Volvo")

#Classes , Objects
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1)

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"

p1 = Person("John", 36)

print(p1)

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()

class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()



