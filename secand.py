def Watch(num):
    sec = num % 60
    mim = num // 60
    hour = num // 3600
    print(f"{hour}:{mim%60}:{sec}")
num = int(input())
Watch(num)

