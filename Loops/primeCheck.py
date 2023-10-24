num = int(input('Enter the number:'))
count = 0
for i in range(1,num+1):
    if num % i ==0:
        count += 1
        
if count == 2:
    print('Number is prime')
else:
    print('Number is not prime')