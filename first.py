def divisible(num):
    if(num%2==0):
        print("YES")
        if(num%4==0):
            print("YES")
            if(num%8==0):
                print("YES")
            else:
                print("NO")
        else:
            print("NO")
    else:
        print("NO")
num = int(input())
divisible(num)
