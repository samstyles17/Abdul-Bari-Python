n = int(input('Enter a number'))
sum = 0
while n != 0 :
    n2 = n%10
    sum = sum + n2
    n = n // 10
    
print(sum)