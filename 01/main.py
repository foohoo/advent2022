def top_total (places, array):
    sorted_array = sorted(array)
    total = 0
    
    for i in range(places, 0, -1):
        total = total + sorted_array[len(sorted_array)-i]
    
    return total


file = open("./01/input.txt", "r")

lines = file.readlines()

elfs_calories = []
current = 0

for line in lines:
    if line == "\n":
        elfs_calories.append(current)
        current = 0
    else:
        current = current + int(line)

# print(max(elfs_calories)) 
print(top_total(3, elfs_calories))