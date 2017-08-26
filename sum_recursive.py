def sum(nums):
    if len(nums) == 1:
        return nums[0]
    else:
        return nums[0] + sum(nums[1:])

print sum([1, 3, 5, 7, 9])
