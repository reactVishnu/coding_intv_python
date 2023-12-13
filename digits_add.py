def increment_large_integer(digits: list[int]) -> list[int]:
    carry = 1  # Start with a carry of 1
    result = []

    for digit in reversed(digits):
        new_digit = digit + carry
        print(f'New Digit {new_digit % 10}')

        carry = new_digit // 10  # Determine the carry for the next digit
        print(carry)
        result.insert(0, new_digit % 10)  # Append the digit to the result

    # If there is still a carry after processing all digits, insert it at the beginning
    if carry:
        result.insert(0, carry)

    return result


print(increment_large_integer([2]))
