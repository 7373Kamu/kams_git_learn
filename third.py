def Narcissistic(num):
    Ans = 0
    loop = len(str(num))
    while(num > 0):
        sum = 1

        tem = num % 10
        for i in range(loop):
            sum =sum * tem
        Ans +=sum
        num = num // 10

    return Ans
num = int(input())
Armstrong = "Yes" if Narcissistic(num) == num else "No"
print(Armstrong)
