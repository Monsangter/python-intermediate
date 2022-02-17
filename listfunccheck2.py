
a = [1,2,3]
a.extend([1,2])
print(a)

b= [6,7]
b.extend(a)
print(b)
b += a
print(b)
b -= a