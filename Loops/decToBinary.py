# num = int(input('Enter a number:'))
# bin  = rev_bin = 0

# while num!=0:
#     num2 = num % 2
#     print(num2)
#     bin = bin*10 + num2
#     print(bin)
#     num = num // 2
#     print(num)
    
    
# print(bin)   
# # while bin!=0:
# #     bin2 = bin % 10
# #     rev_bin = rev_bin*10 + bin2
# #     bin = bin // 10
 

# # print(rev_bin)

import random

n = int(input('Enter a number'))

binary = ""


while n > 0:
    r = n % 2
    n = n // 2
    binary = str(r)  + binary 
print(binary)
# brev = 0
# while binary > 0:
#     r = binary % 10
#     binary = binary //10
#     brev = brev *10 +r

# print(brev)
