def prime(num):
    i = 1
    sum = 0
    while(i<=num):
        sum = sum + 1
        i+=1
    return sum
num = int(input())
print(prime(num))

