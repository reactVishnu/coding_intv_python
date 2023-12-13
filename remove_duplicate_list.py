l = [1, 2, 3, 4, 5, 6, 1]

"""
First Way
"""
l = set(l)
l = list(l)
print(l)

"""
Second Way
"""

k = list()
for i in l:
    if i not in k:
        k.append(i)
print(k)

"""
Third Way
"""
j = list()
j = [x for x in l if x not in j and not j.append(x)]
print(j)
