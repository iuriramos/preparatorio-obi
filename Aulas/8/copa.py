k = int(input())
l = int(input())

# k < l
if k > l:
    k, l = l, k

if k <= 8 and l > 8:
    print('final')
elif (k <= 4 and l > 4) or (k <= 12 and l > 12):
    print('semifinal')
elif k % 2 == 1 and k + 1 == l:
    print('oitavas')
else:
    print('quartas')

''' 
def find(start, end, depth=0):
    mid = (start + end) // 2
    if k <= mid < l:
        return depth
    elif k < l <= mid:
        return find(start, mid, depth+1)
    else: # mid < k < l
        return find(mid+1, end, depth+1)
mapping = {
    0: 'final', 
    1: 'semifinal', 
    2:'quartas', 
    3:'oitavas'
}
key = find(1, 16)
print(mapping[key])
'''
