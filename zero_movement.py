def zero_movement(x):
    n = []
    for i in x:
        if i == 0:
            n.insert(0, 0)
        else:
            n.append(i)
    return n


l = [1, 0, 1, 0, 1, 0]
print(zero_movement(l))
