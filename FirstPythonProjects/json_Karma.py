"""
Use the reddit user API and find out the number of upvotes and down votes.  Interested to find out if your friends
are huge trolls? Look no further.
"""
import json
import requests
import re

print "Welcome to the json analysis of reddit."
print "I will give you the ability to analyze up votes and down votes of certain users."

#user1 = raw_input("What is the first user you want to see.")
user2 = 'clockwork8'
user_list = []
user_name = []

user_enter = True

while user_enter==True:
    user2 = raw_input("What is the second user you want to see.\nEnter Blank if want to exit")
    if (user2 == ' '):
        break
    user_list.append("https://www.reddit.com/user/"+ user2 + ".json")
    user_name.append(user2)
print user_list

headers = {'user-agent': 'Mozilla/5.0'}
user = 0
user_votes = []
for url_usr1 in user_list:
    user1_json = requests.get(url_usr1, headers = headers)

    data1 = user1_json.json()
    data1_str = json.dumps(data1)
    data1_list = data1_str.split()

    i = 0
    ups_found = False
    total_ups = 0
    ups_vote = 0

    while i < len(data1_list):
        if ups_found== True:
            regex = re.compile(r'[,]')
            ups_vote = regex.sub('', data1_list[i])
            total_ups+= int(ups_vote)
            i+=1
            ups_found = False
            continue
        if "ups" in data1_list[i]:
            ups_found = True
        else:
            ups_found = False
            i+=1
            continue
        i+=1
    user_votes.append(total_ups)
print user_votes
