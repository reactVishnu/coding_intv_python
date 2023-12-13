from typing import List
def shift_array(arr: List[int], n: int) -> List[int]:
    # Calculate the effective shift value
    n = n % len(arr)

    # Perform the rotation by slicing the array
    shifted_array = arr[-n:] + arr[:-n]

    return shifted_array


# Example usage:
ans = shift_array([1, 2, 3, 4, 5], -3)
print(ans)
