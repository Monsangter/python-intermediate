a=list(range(1,21))
sum=0
fibonacci=[1]
fibosum = 0

for i in a:
    if i == 1:
        fibonacci.append(i)
    elif i != 1:
        fibonacci.append(fibonacci[i-1] + fibonacci[i-2])

for k in fibonacci:
    if fibonacci[k] <= 20:
        sum += fibonacci[k]

print(sum)