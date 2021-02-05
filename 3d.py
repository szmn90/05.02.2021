a=0
for i in range (len(L)):
    for b in range(len(L[0])):
        a += L[i][1], a += L[i][3], a += L[i][5], a += L[i][7], a += L[i][9]
            a+=L[i][b]
print(a)