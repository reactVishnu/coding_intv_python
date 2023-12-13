"""
First Way
"""


def max_profit(input_list):
    result = list()
    for ind in range(len(input_list) - 1):
        for j in input_list[ind:]:
            k = j - input_list[ind]
            print(f'{j} and {input_list[ind]}')
            result.append(k)

    if len(result)==0:
        return 0
    return max(result)




a = max_profit([])
print(a)
# print(range(len([7, 1, 5, 3, 6, 4])))
"""
Second Way
"""

# def max_profit(list_stock):
#     length_of_the_list = len(list_stock)
#     profit_holder = []
#     maximum_profit = None
#     index = 0
#     for i in list_stock:
#         if index == length_of_the_list - 1:
#             break
#         else:
#             profit = list_stock[index + 1] - i
#             profit_holder.append(profit)
#             if profit < 0:
#                 pass
#             else:
#                 if profit == max(profit_holder):
#                     maximum_profit = list_stock[index + 1]
#                 else:
#                     pass
#             index += 1
#     if maximum_profit is None:
#         return 0
#     return maximum_profit
