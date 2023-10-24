def toBinary(n):
    bin_list = []
    
    for x in n:
        while(n>=1):
            rem = n % 2
            bin_list.append(rem)
            n = n // 2
            
    

n = [1,2,3,4]