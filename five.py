def WatchingMoves(num1, num2):
    if(num1>num2):
        sum : int = num1 - num2
        did : int = num2 // 2
        return sum + did

num1 = int(input())
num2 = int(input())
print(WatchingMoves(num1,num2))
