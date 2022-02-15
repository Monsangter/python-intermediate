a = ['a',1,'2',3,'b',3.4]

b = a[0]+a[4]
print(b)
#c = a[0]+a[1] TypeError: cannot concatenate 'str' and 'int' objects
#print(c) concatenate 사슬처럼 있다
d = a[1]+a[5]
print(d) #float 되네잉
#e = a[1]+a[4]
#print(e)TypeError: unsupported operand type(s) for +: 'int' and 'str'
f = a[0]+a[2]
print(f)

g = a[0]+str(a[1])
print(g)