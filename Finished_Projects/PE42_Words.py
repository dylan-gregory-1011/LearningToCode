file_path = 'C:\\Users\\dylan smith\\Documents\\Learnin\\Python\\Intermediate_Python'

#download the file and replace each quotation mark with a blank space
with open(file_path+'\\p42_words.txt' , 'r') as p42:
    for line in p42:
        words = line.replace('"','').split(',')

letters = ['A','B','C','D','E','F','G', 'H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
#build dictionary with associated values, apply a value to each letter
i = 1
l_dict = {}
while i<=26:
    l_dict[letters[i-1]] = i
    i+=1

#create a triangle up to t20
n = 0
tn = []
while n<=20:
    t = 0.5*n*(n+1)
    tn.append(t)
    n+=1

final_count = 0
#go through each word in the list and initialize each word sum to zero
for word in words:
    word_sum = 0
    #go through each letter and append the value to wordsum
    for letter in word:
        word_sum+= l_dict.get(letter)
    if word_sum in tn:
        final_count+=1

print final_count
