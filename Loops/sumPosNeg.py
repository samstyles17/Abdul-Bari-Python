n = int(input('Enter the number of inputs:'))
sumPos = 0
sumNeg = 0
for i in range(0,n):
    num = int(input('Enter a number:'))
    if num >= 0:
        sumPos = sumPos + num
    elif num < 0:
        sumNeg = sumNeg + num;
        
print(sumPos)
print(sumNeg)
