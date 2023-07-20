def max_profit(array):
    maxi=0
    for i in range(len(array)-1):
        maxi=max(maxi,max(array[i+1::])-array[i])
    return maxi

array = list(map(int,input().split()))
print(max_profit(array))
