def differenceofSum(n,m) -> int:
    divisible = []
    non_divisible = []
    
    for i in range(1,n+1):
        if i%m == 0:
            divisible.append(i)
        else:
            non_divisible.append(i)
            
    if sum(divisible) > sum(non_divisible):
        return sum(divisible) - sum(non_divisible)
    else:
        return sum(non_divisible) - sum(divisible)

n = int(input('Enter the maximum number:'))
m = int(input('Enter the divisibilty check number:'))

result = differenceofSum(n,m)
print(result)