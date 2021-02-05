a=0
b=0
for i in range(len(L)):
    a = L(i)[0]+L(i)[1]
    b = L(i)[2]+L(i)[3]
    if a>b:
        print(L[i])