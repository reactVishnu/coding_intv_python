def unique_entry(customerIDs):
    unique_id = 0
    for customer_id in customerIDs:
        print(f'Unique Id {unique_id} and customer_di is {customer_id}')
        unique_id ^= customer_id
        print(f'Result {unique_id}')
    return unique_id


a = unique_entry([70, 80, 90, 80, 70])
print(a)