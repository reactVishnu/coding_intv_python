def detect_duplicates(l):
    k = []
    for i in l:
        if i in k:
            return True
        else:
            k.append(i)
    return False


a = detect_duplicates([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(a)