# table
n = int(input("Enter a number: "))
for i in range(1, 11):
       print(n * i)


#print 1 to n
n = int(input("Enter n: "))
for i in range(1, n + 1):
    print(i)


#print even number
n = int(input("Enter n: "))
for i in range(1, n + 1):
    if i % 2 == 0:
       print(i)

#print odd number
n = int(input("Enter n: "))
for i in range(1, n + 1):
     if i % 2 != 0:
         print(i)


#print square
n = int(input("Enter n: "))
for i in range(1, n + 1):
      print(i * i)

#product of number 1to n
n = int(input("Enter n: "))
product = 1
for i in range(1, n + 1):
      product *= i
      print("Product =", product)


#factor of number
n = int(input("Enter number: "))
for i in range(1, n + 1):
      if n % i == 0:
          print(i)







 