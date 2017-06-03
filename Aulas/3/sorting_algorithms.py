import time
import math
import random

######## AUX METHOD ###########
def measure(sort_func):
    def inner(nums):
        #print(nums)
        start_time = time.time()
        nums_s = sort_func(nums)
        end_time = time.time()
        #print(nums_s)
        print('speed = {time} s'.format(time=(end_time - start_time)))
        return nums
    return inner        


def swap(nums, i, j):
    if i == j:
        return
    nums[i], nums[j] = nums[j], nums[i]

########### INSERTION SORT ###########

@measure    
def insertion_sort(nums):
    for i in range(1, len(nums)):
        for j in range(i, 0, -1):
            if nums[j - 1] > nums[j]:
                swap(nums, j - 1, j)
            else:
                break
    return nums
    

########### MERGESORT ###########

def merge(nums, aux, start, mid, end):
    # nums[start:mid] i
    # nums[mid + 1: end] j
    # aux k
    i, j, k = start, mid + 1, start
    while i <= mid and j <= end:
        if nums[i] < nums[j]:
            aux[k] = nums[i]
            i += 1
            k += 1
        else:
            aux[k] = nums[j]
            j += 1
            k += 1
    while i <= mid:
        aux[k] = nums[i]
        k += 1
        i += 1
    while j <= end:
        aux[k] = nums[j]
        k += 1
        j += 1
    for k in range(start, end + 1):
        nums[k] = aux[k]    
    
def merge_sort(nums, aux, start, end):
    n = end - start + 1
    if n < 2:
        return nums
    mid = (start + end) // 2
    merge_sort(nums, aux, start, mid)
    merge_sort(nums, aux, mid + 1, end)
    merge(nums, aux, start, mid, end)
    return nums

@measure
def mergesort(nums):
    aux = [0 for _ in nums]
    return merge_sort(nums, aux, 0, len(nums) -1)

########## main method ############

if __name__ == '__main__':
    print("Insertion sort para 10000 números ordenados")
    nums = []
    for n in range(10000):
        nums.append(n)
    insertion_sort(nums)
    
    print("Insertion sort para 10000 números aleatórios")
    nums = []
    for _ in range(10000):
        nums.append(random.random() * 10)
    insertion_sort(nums)

    print("Merge sort para 1000000 números aleatórios")
    numss = []
    for _ in range(1000000):
        numss.append(math.floor(random.random() * 10))
    mergesort(numss)

