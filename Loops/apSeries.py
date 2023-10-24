a = int(input('Enter the first term of the series: '))
d = int(input('Enter the common difference for the AP:'))
n = int(input('Enter the number of terms to be generated:'))

res = [a]
for i in range(2,n+1):
    term = a + (i-1)*d
    res.append(term)
    
print(res)

