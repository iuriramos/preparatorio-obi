'''Versao Nao Otimizada'''

def wifi(rooms):
    # sort rooms in decreasing order of area
    rooms.sort(key=get_room_area, reverse=True) 
    wifi_rooms = []
    for room in rooms:
        wifi_room = get_container_room(room, wifi_rooms)
        if wifi_room: # different than None, there is container room
           wifi_rooms.remove(wifi_room)
        wifi_rooms.append(room)
    return len(wifi_rooms)

def get_room_area(room):
    x1, y1, x2, y2 = room
    return (x2-x1) * (y1-y2)

def get_container_room(new_room, wifi_rooms):
    for wifi_room in wifi_rooms:
        if wifi_room_contains_new_room(wifi_room, new_room):
            return wifi_room
    return None # has not found any container room

def wifi_room_contains_new_room(wifi_room, new_room):
    wx1, wy1, wx2, wy2 = wifi_room
    nx1, ny1, nx2, ny2 = new_room
    return wx1 < nx1 < nx2 < wx2 and wy2 < ny2 < ny1 < wy1

N = int(input())

rooms = []
for _ in range(N):
    room = [int(val) for val in input().split()]
    rooms.append(room)

print(wifi(rooms))

