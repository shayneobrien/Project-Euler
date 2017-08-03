# PE problem 22
# Using names.txt , a 46K text file containing over five-thousand first names, begin by sorting 
# it into alphabetical order. Then working out the alphabetical value for each name, multiply this 
# value by its alphabetical position in the list to obtain a name score.

import os, csv
os.chdir("/Users/sob/Desktop/") # change directory

def quick_sort(the_list): # quick sort algorithm
    less_than, equal_to, greater_than = [], [], []
    if len(the_list) > 1: # lists of length 1 are trivial
        pivot = the_list[0]
        for entry in the_list:
            if entry < pivot:
                less_than.append(entry)
            if entry == pivot:
                equal_to.append(entry)
            if entry > pivot:
                greater_than.append(entry)
        # Don't forget to return something!
        return quick_sort(less_than) + equal_to + quick_sort(greater_than) # join the lists
    else:  
        return the_list
        
with open('PE22.txt', 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"') # open the file
    for names in reader:
        ', '.join(names) # join all names to a list
        
names = quick_sort(names) # sort the list
position, total = 0, 0
for name in names: # for each name
    namescore = 0
    position += 1 # keep track of the position
    for character in name:
        namescore += (ord(character) - ord('A') + 1) # convert A-Z (capitals matter) to 1-26
    total += (namescore * position)

print 'TOTAL: ', total
