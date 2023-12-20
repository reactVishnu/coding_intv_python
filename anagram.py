"""
Easy Way
"""


def anagram(s1, s2):
    for i in s1:
        print(i)
        if str(i) not in s2:
            return False
    return True


str_1 = "hello "
str_2 = "world"

print(anagram(str_1, str_2))

"""
Medium way - which they can accept
"""


def anagram(s1, s2):
    return sorted(s1) == sorted(s2)
