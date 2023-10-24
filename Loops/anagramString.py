s1 = input('Enter the string:')
s2  = input('Enter the string:')

if len(s1) == len(s2):
    for i in s1:
        if i not in s2:
            print('Not Anagram')
            break;
    else:
        print('Anagram')
 
else:
    print('Not Anagram')           