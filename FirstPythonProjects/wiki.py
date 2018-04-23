"""
Like Wikipedia but don't like actually controlling what you learn? Well then this is the app for you.
"""

import re
import json
import requests
import webbrowser

random_article = True
while random_article == True:
    wiki_url = 'https://en.wikipedia.org/w/api.php?action=query&list=random&rnnamespace=0&rnlimit=10&format=json'
    headers = {'user-agent': 'Mozilla/5.0'}
    wiki_data = requests.get(wiki_url, headers=headers)
    wiki_json = wiki_data.json()
    wiki_dict = wiki_json["query"]["random"]
    i = 0
    curious = ''
    while i < len(wiki_dict):
        title_query =  wiki_dict[i]['title']
        print title_query
        curious = raw_input("Do you want to open this article?(\'Yes\' to open)")
        if curious.lower() == 'yes':
            wiki_id = str(wiki_dict[i]['id'])
            chrome_path = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s'
            wiki_new_url = 'https://en.wikipedia.org/wiki?curid='+wiki_id
            webbrowser.open(wiki_new_url)
        if curious.lower() == 'exit':
            random_article = False
            break
        i+=1

    break
