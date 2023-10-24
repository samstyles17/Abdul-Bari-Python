email = input('Enter the email address:')
list1 = email.split('@')

print('username:',str(list1[0]))
print('domain:',str(list1[1]))