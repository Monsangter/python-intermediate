a, b = ('python', 'life')
print(a)
print(b)
print(type(a))
(c, d)= 'python', 'life'
print(c)
print(d)
print(type(c))
[e,f] = ['python', 'life']
print(e)
print(d)
print(type(e))

#같은 값을 대입
a = b = 'python'

#이런 것도 가능하다.
a= 3
b= 5
a, b = b, a
print(a)
print(b)