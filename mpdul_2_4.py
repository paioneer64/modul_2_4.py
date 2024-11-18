numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
prims = []
not_prims = []
is_prim = "True"
for i in range(2,15):
    for j in range(2,i):
        if i % j == 0 and i != j:
            break
    else:
     prims.append(i)
print(prims)

for k in numbers:
    if not(k in prims) and k > 1:
       not_prims.append(k)
print(not_prims)









