nos = int(input('Enter the number of inputs:'))
max = 0
min = 0
for i in range(0,nos):
    num = int(input('Enter the number:'))
    if num > max:
        max = num
        
    if min > num:
        min = num
        
print(max)
print(min)