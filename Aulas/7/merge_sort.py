array = input().split()
array = [int(num) for num in array]

def merge_sort(array, start, end):
    # caso base
    if start >= end:
        return 
    # recursão
    mid = (start + end) // 2
    merge_sort(array, start, mid)
    merge_sort(array, mid+1, end)
    # merge step
    # sorted left: ['start, mid]
    # sorted right: ['mid+1, end]
    i, j = start, mid+1
    helper = []
    while i <= mid and j <= end:
        if array[i] <= array[j]:
            helper.append(array[i])
            i += 1
        else:
            helper.append(array[j])
            j += 1
    while i <= mid:
        helper.append(array[i])
        i += 1
    while j <= end:
        helper.append(array[j])
        j += 1
    k = start
    for num in helper:
        array[k] = num
        k += 1

merge_sort(array, start=0, end=len(array)-1)
print(array)
