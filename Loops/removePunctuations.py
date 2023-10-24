string=input('Enter the string:')
lower = ''
upper = ''
for i in string:
    if i.islower():
        lower+= i
    elif i.isupper():
        upper+=i
        
final_str = lower+upper    