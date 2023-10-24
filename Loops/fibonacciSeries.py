n = int(input('Enter the number of terms for the Fibonacci series:'))
t1 = 0
t2 = 1
sum = 0
res= [t1,t2]
for i in range(3,n+1):
    new_term = t1 + t2
    # print('New Term = ',new_term)
    res.append(new_term)
    
    
    t1 = t2
    t2 = new_term
    
print(res)