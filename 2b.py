a = 0
for i in range (len(L)):
    for b in range(len(L[0])):
        while L(i)(b) > 499 and L(i)(b) < 600:
            a+=1
print(a) 