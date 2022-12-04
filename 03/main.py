import string

file = open("./03/input.txt", "r")
rucksacks = file.readlines()

item_priority = list(string.ascii_lowercase + string.ascii_uppercase)


def find_duplicates_in_rucksack():
    duplicates = list()
    
    for rucksack in rucksacks:
        rucksack = rucksack.strip()
        mid_point = int(len(rucksack)/2)
        
        compartment_one = rucksack[:mid_point]
        compartment_two = rucksack[mid_point:]
        
        for item in compartment_one:
            if (item in compartment_two):
                duplicates.append(item)
                break
                
    return duplicates
        

def find_badges():
    badges = list()
    groups = list()
    group_of_rucksacks = list()
    
    for rucksack in rucksacks:
        rucksack = rucksack.strip()
        group_of_rucksacks.append(rucksack)
        if (len(group_of_rucksacks) == 3):
            groups.append(group_of_rucksacks)
            group_of_rucksacks = list()
            
    for group in groups:
        rucksack = group[0]
        for item in rucksack:
            if (item in group[1] and item in group[2]):
                badges.append(item)
                break
            
    return badges


def calc_score(items):
    total = 0
    for item in items:
        total = total + item_priority.index(item) + 1
    return total
    
        
print(calc_score(find_duplicates_in_rucksack()))
print(calc_score(find_badges()))
    
