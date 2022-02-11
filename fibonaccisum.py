a=list(range(1,21))
sum=0
fibonacci=[1]
fibosum = 0

for i in a:
    if i == 1:
        fibonacci.append(i)
    elif i != 1:
        fibonacci.append(fibonacci[i-1] + fibonacci[i-2])

for i in fibonacci:
    if fibonacci[i] <= 20:
        sum += fibonacci[i]

print(sum)