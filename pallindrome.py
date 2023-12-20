""" With Slicing """


def is_palindrome(stringular):
    remove_alpha_num = "".join(filter(str.isalnum, stringular.lower()))
    return remove_alpha_num[::] == remove_alpha_num[::-1]


word_to_check = "0A man, a plan, a canal: Panama0"
print(is_palindrome(word_to_check))

"""
Without Slicing
"""


def palindrome_checker(s1):
    s1 = "".join(filter(str.isalnum, s1.lower()))
    result = [s1[ind] == val for ind, val in enumerate(reversed(s1))]
    return not False in result


print(palindrome_checker(word_to_check))

"""
Without .isalnum, without for loop, without slicing
"""


def remove_alphanumeric(input_str):
    result = ""
    for char in input_str:
        # Check if the character is a letter or a number
        if ('a' <= char <= 'z') or ('A' <= char <= 'Z') or ('0' <= char <= '9'):
            result += char
    reversed_str = "".join(reversed(result))
    if reversed_str.lower() == result.lower():
        return True
    return False


output_string = remove_alphanumeric(word_to_check)
print(output_string)
