N = int(input())
nums = [int(s) for s in input().split()]

def linhas(nums):
    extra = [0 for _ in nums]
    return mergesort(nums, extra, 0, len(nums))
    
def mergesort(nums, extra, start, end):
    length = end - start
    if length < 2:
        return 0
    sum_ = 0
    mid = (start + end) // 2
    sum_ += mergesort(nums, extra, start, mid)
    sum_ += mergesort(nums, extra, mid, end)
    sum_ += merge(nums, extra, start, mid, end)
    return sum_

def merge(nums, extra, start, mid, end):
    i, j, k = start, mid, start
    sum_ = 0
    while i < mid and j < end:
        if nums[i] <= nums[j]:
            extra[k] = nums[i]
            i += 1
        else:
            extra[k] = nums[j]
            j += 1
            sum_ += (mid - i)
        k += 1
    while i < mid:
        extra[k] = nums[i]
        i += 1
        k += 1
    while j < end:
        extra[k] = nums[j]
        j += 1
        k += 1
    for k in range(start, end):
        nums[k] = extra[k]
    return sum_

print(linhas(nums))
