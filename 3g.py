nie=0
tak=0
for i in range (len(L)):
    for b in range(len(L[0])):
        if L[i][b]%2==0:
            tak += 1
        else:
            nie += 1 
    if tak > nie:
        print(L[i])