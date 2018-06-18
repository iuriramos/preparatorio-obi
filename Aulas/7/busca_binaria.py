import time 
import random

def find_target(array, target): # [0, 1, 2, 5, 8], 8
    # print ('array=', array, 'target=', target)
    start, end = 0, len(array)-1 # 0, 4
    while start <= end:
        mid = (start + end)//2
        val = array[mid]
        # print ('start=', start, 'end=', end, end=' ')
        # print ('mid=', mid, 'val=', val)
        if val == target:
            return mid
        elif val < target:
            start = mid+1
        else: # val > target
            end = mid-1
    # start > end
    return -1
    
def find_target_rec(array, target, start, end):
    if start > end:
        return -1
    mid = (start + end) // 2
    val = array[mid]
    print ('start=', start, 'end=', end, end=' ')
    print ('mid=', mid, 'val=', val)
    if val == target:
        return mid
    elif val < target: 
        return find_target_rec(array, target, mid+1, end)
    else: # val > target
        return find_target_rec(array, target, start, mid-1)
    
def find_target_linear(array, target):
    for num in array:
        if num == target:
            return
    
def search_linear(N):
    array = list(range(N))
    random.shuffle(array)
    for num in range(N):
        find_target_linear(array, num)
    
def search_binary(N):
    array = list(range(N))
    for num in range(N):
        find_target(array, num)

N = int(input())

# busca linear
print('# busca linear')
start = time.time()
search_linear(N)
end = time.time()
secs = end-start
print(secs, 'segundos')

# busca binária
print('# busca binária')
start = time.time()
search_binary(N)
end = time.time()
secs = end-start
print(secs, 'segundos')

# array = input().split()
# array = [int(num) for num in array]
# target = int(input())
# print(find_target_rec(array, target, 0, len(array)-1))
