counter=0
num = int(input('Enter a number:'))
while num != 0:
    num = num // 10
    counter += 1
    
print(counter) 