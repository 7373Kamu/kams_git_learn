def factorial(num):
    sum = 1
    i=1
    while(i <=num):
        sum = sum * i
        i+=1
    return sum
num = int(input())
print(factorial(num))

