def busca_menor_indice(nums, val):
    s = 0
    e = len(nums) -1

    while s < e:
        mid = (s + e) // 2
        x = nums[mid]
        if x == val:
            s = mid
        elif x < val:
            s = mid + 1
        else:
            e = mid -1
    
    # s == e
    if nums[e] == val:
        return e
    
    return -1
    
    
def busca_maior_indice(nums, val):
    s = 0
    e = len(nums) -1

    while s < e:
        mid = (s + e + 1) // 2
        x = nums[mid]
        if x == val:
            s = mid
        elif x < val:
            s = mid + 1
        else:
            e = mid -1
    
    # s == e
    if nums[e] == val:
        return e
    
    return -1


nums = [1, 2, 3, 5, 5, 5, 7, 8, 9]
val = 5

print(busca_menor_indice(nums, val))
print(busca_maior_indice(nums, val))

