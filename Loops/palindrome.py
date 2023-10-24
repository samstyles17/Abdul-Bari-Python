def funcPalindrome(num) -> bool:
    og_num = num
    rev = 0
    while num:
        num2 = num % 10
        print(num2)
        rev = rev*10 + num2
        print(rev)
        num = num//10
        print(num)
    
    print(rev)
    if og_num == rev:
        return True
    else:
        return False
        
    

def funcPal(strNum) -> bool:
    revStr = strNum[::-1]
    print(revStr)
    if revStr == strNum:
        return True
    else:
        return False

num = int(input('Enter a number:'))
stringNum = str(num)
print(type(num))
value = funcPal(stringNum)
if value is True:
    print("Palindrome")
else:
    print('Not Palindrome')

