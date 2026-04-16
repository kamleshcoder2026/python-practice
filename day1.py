student = [
    {
    "rollno": 12, 
    "name": "kam",
    "age": 18 
    },
    {
    "rollno": 13, 
    "name": "sam",
    "age": 28 
    }
]
registry = {
    "rollno": 12, 
    "name": "kam",
    "age": 18 
    } 
print(registry["name"])

# table
n = int(input("Enter a number: "))
for i in range(1, 11):
       print(n * i)

# reverse table

for i in range(10, 0, -1):
      print(n, "x", i, "=", n * i)

#print 1 to n
for i in range(1, n + 1):
    print(i)


#print even number

for i in range(1, n + 1):
    if i % 2 == 0:
       print(i)

#print odd number

for i in range(1, n + 1):
     if i % 2 != 0:
         print(i)

#print factorial
fact = 1

for i in range(1, n + 1):
       fact *= i

       print("Factorial =", fact)

#prime number

for i in range(2, n):
      if n % i == 0:
         print("Not Prime")
         break
else:
        print("Prime")


#print square

for i in range(1, n + 1):
      print(i * i)

#product of number 1to n
product = 1

for i in range(1, n + 1):
      product *= i
  
      print("Product =", product)

#factor of number

for i in range(1, n + 1):
      if n % i == 0:
          print(i)


