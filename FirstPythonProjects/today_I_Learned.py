"""
Another example of interfacing with the reddit "today I learned" API.  A good demonstration of
attempting to learn regex and different string manipulation methods.
"""
import requests
import re
import time
import json

headers = {'user-agent': 'Mozilla/5.0'}
TIL_url = 'https://www.reddit.com/r/todayilearned/new/.json'
TIL_data_file = requests.get(TIL_url, headers = headers)

data1 = TIL_data_file.json()
data1_str = json.dumps(data1)
data1_list_init = data1_str.split('created_utc')
data1_list = []
for string in data1_list_init:
    if "\"title\":" in string:
        data1_list.append(string.split('TIL'))

TIL_list=[]
i = 0
while i< len(data1_list):
    regex = re.compile(r'[,"\\:]')
    TIL = regex.sub('', data1_list[i][1])
    TIL_list.append("TIL "+TIL.strip())
    i+=1
match_fact = 0
for fact in TIL_list:
    print "new fact"
    with open('Today_I_Learned.txt', 'a+') as TILdoc:
        for line in TILdoc:
            if line[0:20] in fact[0:20]:
                match_fact = 1
                print "Matching"
                break
        if match_fact == 1:
            match_fact = 0
            print "iteration skipped"
            continue
        if match_fact == 0:
            TILdoc.write(fact+"\n")
            print fact
