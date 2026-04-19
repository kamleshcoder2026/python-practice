a = [1,2,3,4]
print(a)

#add
a = [1,2,3]
a.append(4)
print(a)

# delete
a = [1,2,3]
a.remove(2)
print(a)

# sum
a = [1,2,3,4]
print(sum(a))

# largest number in list
a = [10,5,20,8]
print(max(a))

#reverse the list
a = [1,2,3]
a.reverse()
print(a)

# sorting of a list
a = [3,1,4,2]
a.sort()
print(a)

#copy list
a = [1,2,3]
b = a.copy()
print(b)

# list length
a = [1,2,3,4]
print(len(a))

# even number 
a = [1,2,3,4,5]
even = [x for x in a if x % 2 == 0]
print(even)

# square in list
a = [1,2,3,4]
square  = [x**2 for x in a]
print(square)

# list mein odd
a = [1,2,3,4,5]
odd = [x for x in a if x % 2 != 0]
print(odd)

#smallest number in list
a = [10,5,8,2]
print(min(a))

#average
a = [10,20,30]
avg = sum(a) / len(a)
print(avg)

