li1 = [12,13,12,14,18,19,22,16,19]
for x in li1:
    for y in range(x+1,len(li1)+1):
        if li1[x] == li1[y]:
            li1.remove(li1[y])
            
print(li1)