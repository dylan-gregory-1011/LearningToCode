names = []
alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I','J','K','L','M','N', 'O', 'P','Q','R','S','T','U','V','W', 'X', 'Y', 'Z']
with open('C:\Users\\dylan smith\\Documents\\Learnin\\Python\\Project_Euler\\names.txt') as names_file:
    for line in names_file:
        name = line.replace("\"", "").split(',')
        for single in name:
            names.append(single)

sort_names = sorted(names)
i = 0
place = i+1
total = 0
#iterate over all the names and multiply the place in the list by the sum of the letters
while i<len(sort_names):
    #get the current name in the list
    name = sort_names[i]
    name_total = 0
    #get the sum of all the letters by getting each values
    for letter in name:
        name_total+=(alpha.index(letter)+1)
    score = place*name_total
    total += score
    place+=1
    i+=1
print total
