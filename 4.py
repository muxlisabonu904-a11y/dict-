
import os
os.system("cls")
lst = [('yellow', 1),('blue', 2),('yellow', 3),('blue', 4),('red', 1)]
r = {}
for k,v in lst:
    if k not in r:
        r[k] = []
    r[k].append(v)
print(r)
