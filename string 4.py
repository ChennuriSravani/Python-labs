#Write a python program to handle a ZeroDivisionError exception when dividing a number by zero.
a=10
b=8
try:
  if b==0:
    raise ZeroDivisionError("b value should not be zero")
  else:
    c=a/b
    print(c)
except ZeroDivisionError as e:
    print(e)
#Write apython program that prompts the user to input an integer and raises a ValueError exception if the input is not avalid integer.

try:
    a=int(input("Enter a value:"))
    b=int(input("Enter b value:"))
    c=a/b
    print(c)
    print("Middle")
except ZeroDivisionError:
    print("b value cannot be a zero")
except ValueError:
    print("value should be a number")
print("End")

#Write a python program that opens a file and handles a FileNotFoundError exception if the file does not exist.

try:
  file=open("three.txt","r")
  for line in file:
    print(line)
except:
  print("File not Found")
else:
  print("else block")


#Write a python program that prompts the user to input two numbers and raises a TypeError exception if the inputs are not numerical.

try:
  a=input("Enter a number:")
  b=input("Enter a number:")
  c=a/b
  print(c)
  print("Middle")
except:
  print("Inputs should be Numerical")
print("End")
