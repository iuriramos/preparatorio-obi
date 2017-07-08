def subsets(nums, index):
    # caso base
    if index == len(nums): # lista vazia
        return [[]]
    # recursão
    val = nums[index]
    subsets_without = subsets(nums, index + 1) # todos os subconjuntos que não possuem val
    subsets_with = [] # todos os subconjuntos que possuem val
    for subset_without in subsets_without:
        subsets_with.append([val] + subset_without)
    return subsets_with + subsets_without
    
if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5]
    output = subsets(nums, 0)
    print (sorted(output))
    
    
