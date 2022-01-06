import re


with open("2021/day22/input.txt") as file:
    data = file.read().splitlines()

pattern_for_instructions = '^(on|off) x=(-?\d+)..(-?\d+),y=(-?\d+)..(-?\d+),z=(-?\d+)..(-?\d+)'
cuboids = []


def split_cuboids(cuboid):
    return cuboid[-2:]

def intersect_cuboids(cuboids):
    if len(cuboids) > 1:
        return (cuboids[1][0] <= cuboids[0][1] and cuboids[0][0] <= cuboids[1][1]) \
                and (cuboids[1][2] <= cuboids[0][3] and cuboids[0][2] <= cuboids[1][3]) \
                and (cuboids[1][4] <= cuboids[0][5] and cuboids[0][4] <= cuboids[1][5])

    return None

divided_cuboids = []
on_off = []

def divide_cuboids(second, divided_cuboids, on_off):
    final_cuboids = []

    if len(divided_cuboids) == 0:
        final_cuboids.append(second)
    
    if len(divided_cuboids) > 0:
        for first in divided_cuboids:
            if not intersect_cuboids([first, second]):
                final_cuboids.append(first)
            else:
                #x
                if first[0] <= second[0] <= first[1]:
                    temp = first.copy()
                    temp[1] = second[0]-1
                    new = temp
                    final_cuboids.append(new)
                    first[0] = second[0]
                
                if first[0] <= second[1] <= first[1]:
                    temp = first.copy()
                    temp[0] = second[1]+1
                    new = temp
                    final_cuboids.append(new)
                    first[1] = second[1]

                #y
                if first[2] <= second[2] <= first[3]:
                    temp = first.copy()
                    temp[3] = second[2]-1
                    new = temp
                    final_cuboids.append(new)
                    first[2] = second[2]

                if first[2] <= second[3] <= first[3]:
                    temp = first.copy()
                    temp[2] = second[3]+1
                    new = temp
                    final_cuboids.append(new)
                    first[3] = second[3]
                   
                
                #z
                if first[4] <= second[4] <= first[5]:
                    temp = first.copy()
                    temp[5] = second[4]-1
                    new = temp
                    final_cuboids.append(new)
                    first[4] = second[4]

                
                if first[4] <= second[5] <= first[5]:
                    temp = first.copy()
                    temp[4] = second[5]+1
                    new = temp
                    final_cuboids.append(new)
                    first[5] = second[5]

        if on_off == 'on':
            final_cuboids.append(second)
    
    
    divided_cuboids = final_cuboids[:]
    return final_cuboids, divided_cuboids
     
        

for line in data:
    result = re.match(pattern_for_instructions, line)
    merged_data = list(result.groups())
    if min(list(int(item) for item in merged_data[1:])) >= -50 \
         and max(list(int(item) for item in merged_data[1:])) <= 50:
         on_off.append(merged_data[0])
         cuboid = list(int(item) for item in merged_data[1:])
         cuboids.append(cuboid)


for line in data:
    result = re.match(pattern_for_instructions, line)
    merged_data = list(result.groups())
    on_off.append(merged_data[0])
    cuboid = list(int(item) for item in merged_data[1:])
    cuboids.append(cuboid)



for i, cuboid in enumerate(cuboids):
    final, divided_cuboids =  divide_cuboids(cuboid, divided_cuboids, on_off[i])


volume = 0


for cuboid_coord in divided_cuboids:
    volume += (cuboid_coord[1] - cuboid_coord[0]+1) * (cuboid_coord[3] - cuboid_coord[2]+1) * (cuboid_coord[5] - cuboid_coord[4]+1)

print(volume)
   
  
    
    
    


    
    
    