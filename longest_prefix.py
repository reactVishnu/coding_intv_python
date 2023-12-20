# first way

def longest_prefix(strs):
    if not strs:
        return ""
    if len(strs) == 1:
        return strs[0]
    strs.sort()
    print(f'Sorted list {strs}')
    prefix = ""
    for i in range(len(strs[0])):
        if strs[0][i] == strs[-1][i]:
            prefix += strs[0][i]
        else:
            break
    return prefix


print(longest_prefix(["Aharcodess", "Bharm", "Baarmes", "Dharlie"]))


# [""charcode"", ""charme"", ""charmes"", ""charlie""]

# Second Way

def longest_common_prefix(strings):
    if not strings:
        return ""

    # Take the first string as a reference
    reference_str = strings[0]
    common_prefix = []
    k = []
    for i in range(len(reference_str)):
        # Check if the current character is common in all strings
        for s in strings:
            if i < len(s):
                if s[i] == reference_str[i]:
                    k.append(True)
                else:
                    k.append(False)
        if all(k):
            common_prefix.append(reference_str[i])
        else:
            break

    return "".join(common_prefix)


# Example usage:
input_strings = ["charcode", "charme", "charmes", "charlie"]
output = longest_common_prefix(input_strings)
print(f"Input: {input_strings}\nOutput: {output}")


def longest_common_prefix(strings):
    if not strings:
        return ""

    # Take the first string as a reference
    reference_str = strings[0]
    common_prefix = []

    for i in range(len(reference_str)):
        # Check if the current character is common in all strings
        if all(i < len(s) and s[i] == reference_str[i] for s in strings):
            common_prefix.append(reference_str[i])
        else:
            break

    return "".join(common_prefix)


# Example usage:
input_strings = ["charcode", "charme", "charmes", "charlie"]
output = longest_common_prefix(input_strings)
print(f"Input: {input_strings}\nOutput: {output}")
