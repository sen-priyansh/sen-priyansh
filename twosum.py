def twoSum( nums: list[int], target: int) -> list[int]:
    a=tuple()
    
    for i in range(0,len(nums)):
        for j in range(0,len(nums)):
            if nums[i]+nums[j]==target:
                a=[i,j]
                break
    return a
print(twoSum(l,t))
