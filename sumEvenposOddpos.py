def LargeSmallSum(arr):
    max_even = 0
    min_odd = max(arr)
    
    for i in range(1,len(list1)):
       if i % 2 == 0:
           if list1[i] > max_even:
               max_even = list1[i]
       elif i % 2 != 0:
           if list1[i] < min_odd:
               min_odd = list1[i]
               
    return max_even + min_odd
             

list1 = []
size = int(input('Enter the size of the array:'))
for i in range(size):
    ele = int(input())
    list1.append(ele)
    
if len(list1) == 0:
    print('0')

elif len(list1) <= 3:
    print('0')
    
else:
    result = LargeSmallSum(list1)
    print(result)
    
