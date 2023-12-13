def target_hitter(nums, target):
    for index, item in enumerate(nums):
        y = target - item
        print(f'y = {y} and index is {index}')
        if y in nums[index+1:]:
            return [index, nums[index+1:].index(y) + index+1]
    return []


prices = [3, 3]
target = 6

print(target_hitter(prices, target))
