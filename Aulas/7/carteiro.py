N, M = input().split()
houses = [int(house) for house in input().split()]
# houses = {house: index for index, house in enumerate(houses)}
packets = [int(packet) for packet in input().split()]

def get_next_position(houses, house):
    lo, hi = 0, len(houses)-1
    while lo <= hi:
        mid = (lo + hi)//2
        val = houses[mid]
        if val == house:
            return mid
        elif val < house:
            lo = mid+1
        else:
            hi = mid-1
    return -1

position = 0
distance = 0

for packet in packets:
    next_position = get_next_position(houses, packet)
    distance += abs(next_position-position)
    position = next_position
    
print(distance)



'''
distance = 0
position = 0

for packet in packets:
    next_position = houses[packet]
    distance += abs(next_position-position)
    position = next_position
    
print(distance)
'''
