nums = [3,2,1]

def nums_max(nums):
    unique_nums = sorted(list(nums), reverse=True)
    
    if len(unique_nums) < 3:
        return unique_nums[0]
    else:
        return unique_nums[2]
    
print(nums_max(nums))