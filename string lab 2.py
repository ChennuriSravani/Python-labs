#1. Write a Python program to Count all letters, digits, and special symbols from the given string
# Input = “P@#yn26at^&i5ve”

s = "P@#yn26at^&i5ve"
chars = digits = symbols = 0

for ch in s:
    if ch.isalpha():
        chars += 1
    elif ch.isdigit():
        digits += 1
    else:
        symbols += 1

print("Chars =", chars, "Digits =", digits, "Symbol =", symbols)

#2. Write a Python program to remove duplicate characters of a given string.
#Input = “String and String Function”
 
s = "String and String Function"
result = ""
seen = set()

for ch in s:
    if ch not in seen:
        seen.add(ch)
        result += ch

print(result)

#3. Write a Python program to count Uppercase, Lowercase, special character and numeric values in a given string
 #Input = “Hell0 W0rld ! 123 * # welcome to pYtHoN”
 
s = "Hell0 W0rld ! 123 * # welcome to pYtHoN"
upper = lower = digit = special = 0

for ch in s:
    if ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1
    elif ch.isdigit():
        digit += 1
    elif not ch.isspace():
        special += 1

print("UpperCase :", upper)
print("LowerCase :", lower)
print("NumberCase :", digit)
print("SpecialCase :",special)

#4. Write a Python Count vowels in a string
 #input= “Welcome to Python Assignment”
 
s = "Welcome to Python Assignment"
vowels = "aeiouAEIOU"
count = sum(1 for ch in s if ch in vowels)
print("Total vowels are:",count)

