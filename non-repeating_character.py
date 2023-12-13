def non_repeating(x):
    for ind, char in enumerate(x):
        if char not in x[ind + 1:]:
            return ind
    return ''


s = 'longelgonr'
# print(non_repeating(s))


def non_repeating_sec(string):
    k = {}
    for ind, val in enumerate(string):
        if val in k:
            del k[val]
        else:
            k[val] = ind
    return k[list(k.keys())[0]]


s = 'nonrreemoval'
print(non_repeating_sec(s))