def array_intersection(x1, y1):
    result = []
    for x in x1:
        if x in y1:
            result.append(x)

    return result


customers1 = [1, 2, 3, 4, 5]
customers2 = [4, 5, 6, 7, 8]


# Second Way
def common_customers(customers1: list[int], customers2: list[int]) -> list[int]:
    # Convert the input arrays to sets
    set1 = set(customers1)
    set2 = set(customers2)

    # Find the common customers using set intersection
    common_customers_set = set1.intersection(set2)

    # Sort the common customers in ascending order
    sorted_customers = sorted(common_customers_set)

    # Convert the sorted set back to a list and return it
    return list(sorted_customers)


print(array_intersection(customers1, customers2))
