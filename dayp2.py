# even or odd
n = 7
if n % 2 == 0:
    print("even number")
else:
    print("odd number")

# Sum of all numbers in a list
numbers = [3, 5, 7, 2]

total = 0
for i in range(len(numbers)):
    total = total + numbers[i]   

print("Sum =", total)

#Find the largest number in a list
numbers = [4, 12, 9, 1]
print("Largest number =", max(numbers))

#Count vowels in a string
text = "Python Programming"
count = 0
vowels = "aeiouAEIOU"

for ch in text:
    if ch in vowels:
        count = count + 1
print("Number of vowels =", count)

#Reverse a string
word = "Python"

reverse = word[::-1]

print("Reversed =", reverse)

# number is prime
n = 11

for i in range(2, n):
    if n % i == 0:
        print("Not Prime")
        break
else:
    print("Prime")

#multiplication table of a number
num = 5
for i in range(1, 11):
    print(num * i)

# remove duplicates
number = [2, 3, 2, 4, 3]
number = list(set(number))
print(number)

# palindrome check
text = "radar"

if text == text[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

# factorial
num = 5
fact = 1

for i in range(1, num + 1):
    fact = fact * i

print("Factorial =", fact)

# print even number in a list
numbers = [1, 2, 3, 4, 5, 6]

for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        print(numbers[i])


#Sum of digits of a number
num = 123
total = 0
while num > 0:
    digit = num % 10
    total = total + digit
    num = num // 10

print("Sum of digits =", total)  

#second largest number in a list
numbers = [5, 9, 1, 12]

numbers.sort()
print("Second largest =", numbers[-2])

# leap year
year = 2024

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not a Leap Year")

# merge two list
list1 = [1, 2, 3]
list2 = [2, 3, 4]

merged = list(set(list1 + list2))

print(merged) 

# Find common elements between two lists
list1 = [1, 2, 3]
list2 = [2, 3, 4]

common = list(set(list1) & set(list2))

print(common)
