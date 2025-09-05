import random

l1 = []
l2 = []
l3 = []

n1 = random.randint(1,20)
n2 = random.randint(1,20)

for i in range (1,n1+1):
    n = random.randint(1,100)
    l1.append(n)

for j in range (1,n2+1):
    n = random.randint(1,100)
    l2.append(n)
    
for i in l1:
    if i in l3:
        continue
    else:
        l3.append(i)

for j in l2:
    if j in l3:
        continue
    else:
        l3.append(j)
        
print(l1)
print(l2)
print(l3)
