print("hello world")
number = int(input("enter a number"))
square = number * number
print("square:", square)


if number % 2 == 0:
    print("even number")
else:
    print("odd number")  

n1 = int(input("enter a number"))
n2 = int(input("enter a number")) 
sum =  n1 + n2
product = n1 * n2
division = n1 / n2
print("sum", sum)
print("product", product)
if n2 != 0:
    division = n1 / n2
    print("division", division)
else:
   print("number cannot divide")

# value swap
n3 = int(input("entr number"))
n4 = int(input("entr number"))
n3 = n3 + n4
n4 = n3 - n4
n3 = n3 - n4
# agar n3 = 5 & n4 7 12, 12-7 =5, 12-5 = 7
print("n3 =", n3)
print("n4 =", n4)

# largest of 3 no
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print("Largest number is:", a)
elif b >= a and b >= c:
    print("Largest number is:", b)
else:
    print("Largest number is:", c)

# pos, neg or 0
num = int(input("Enter a number: "))

if num > 0:
    print("Positive number")
elif num < 0:
    print("Negative number")
else:
    print("Zero")   

# no div by 5 , 11
num = int(input("Enter a number: "))

if num % 5 == 0 and num % 11 == 0:
    print("Divisible by both 5 & 11")
else:
    print("Not divisible by 5 and 11")  

#print no 1-100
for i in range(1, 101):
    print(i)

# table
num = int(input("Enter a number: "))

for i in range(1, 11):
    print(num * i)

# sum of 1 to n numbers
n = int(input("Enter a number: "))
sum = 0
for i in range(1, n + 1):
    sum = sum + i

print("Sum is:", sum)

# factorial
n = int(input("Enter a number: "))

factr = 1
for i in range(1, n + 1):
    factr = factr * i

print("Factorial is:", factr)


#count number of digits
num = int(input("Enter a number: "))

count = 0
while num > 0:
    num = num // 10
    count = count + 1

print("Number of digits:", count) 

#vowel or consonant
 if n == 'a' or n == 'e' or n == 'i' or n == 'o' or n == 'u' or \
n == 'A' or n == 'E' or n == 'I' or n == 'O' or n == 'U':
     print("vowel")
else:
     print("consonant") 


# largest number in list
a = [10,5,20,8]
print(max(a))   


# sum
a = [1,2,3,4]
print(sum(a))

# sorting of a list
a = [3,1,4,2]
a.sort()
print(a)

#duplicate in a list
a = [1,2,4,2, 3, 4, 5]
a = list(set(a))
print(a)

#prime number

for i in range(2, n):
      if n % i == 0:
         print("Not Prime")
         break
else:
        print("Prime")


#simple calculator
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)





 




