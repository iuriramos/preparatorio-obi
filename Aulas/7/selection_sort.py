import random

array = input().split()
array = [int(num) for num in array]

def selection_sort(array):
    N = len(array)
    start = 0
    
    while start < N:
        index = start
        min_index = start
        while index < N: # [start, ..., N-1]
            if array[index] < array[min_index]:
                min_index = index
            index += 1
        # swap elementos
        array[start], array[min_index] = array[min_index], array[start]
        start += 1
        
    # retorna array ordenado
    return array 
    
def array_is_sorted(array):
    N = len(array)
    for i in range(N-1):
        if array[i] > array[i+1]:
            return False
    return True
        
    
def brute_force_sort(array):
    while not array_is_sorted(array):
        random.shuffle(array)
    return array
    
    
print (brute_force_sort(array))
