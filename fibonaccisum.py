a=list(range(1,21))
sum=0
fibonacci=[1]
fibosum = 0

for i in a:
    if i == 1:
        fibonacci.append(i)
    elif i != 1:
        fibonacci[i] = fibonacci[i-1] + fibonacci[i-2]
        if fibosum <= 20:
            fibonacci.append(fibosum)

print(fibonacci)