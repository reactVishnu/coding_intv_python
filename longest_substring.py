def longest_substring(string: list):
    print("runned")
    if not string:
        return ""
    if len(string) == 1:
        return string[0]
    reference_string = string[0]
    common_longest_substring = []
    for i in range(len(reference_string)):
        # print(f'i: {i} : {reference_string[:i + 1]}')
        # print(list(s in reference_string[:i + 1] for s in string))
        if all(reference_string[:i + 1] in s for s in string):
            common_longest_substring.append(reference_string[:i + 1])

        for j in range(i + 1, len(reference_string)):
            # print(f'range({i},{len(reference_string)}) and i:j = {i}:{j}')
            # print(f'j : {reference_string[i:j+1]}')
            if all(reference_string[i:j + 1] in s for s in string):
                common_longest_substring.append(reference_string[i:j + 1])

    if len(common_longest_substring) == 0:
        return ""
    return max(common_longest_substring, key=len)


x = ["raja", "janwar", "magaja", "japper", "jakrta"]
print(longest_substring(x))
