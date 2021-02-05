a=0
b=0
for i in range (len(L)):
    for z in range(len(L[0])):
        if L[i][z]==0 or L[i][z]==9:
            a+=1
    if a>0:
        b+=1
    a=0
print(b)