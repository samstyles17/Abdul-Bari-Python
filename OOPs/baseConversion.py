# a = 10
# b = True
# print(bin(a))
# print(bin(b))
# print(int("125"))

num1 = int(input("Enter number 1:"))
num2 = int(input("Enter number 2:"))

# print(num1-num2)

if num1 - num2 >= 0:
    print(num1-num2)
else:
    print(num2-num1)
    
if(num1%2==0):
    print(num1, " is even")
else:
    print(num1," is odd")
    
if(num1 >= 18):
    print('Eligible')
else:
    print('Not Eligible')