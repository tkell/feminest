import re
import requests
from pyechonest import artist
from names import male_names, female_names

def clean_tags(string):
    string = string.replace('<td>', '')
    string = string.replace('</td>', '')
    string = string.replace('<br />', '')
    string = string.replace('</a>', '')
    if '<a href' in string:
        string = re.search(r'<a href=.+?>(.+)', string, re.S).group(1)
    return string.strip()


for a in artist.top_hottt(start=20, results=10):
    # check their wiki page:  if they're a band, get members
    # if they're not, do pronoun search

    if a.urls.get('wikipedia_url', None):
        wiki_url = a.urls['wikipedia_url']
        res = requests.get(wiki_url)
        body = res.text
        infobox = re.search(r'<table class="infobox.+?</table>', body, re.S).group()
        if 'Members' not in infobox:
            print a, " has one member."
            # do the search from pronouns.py here


        else:
            print a, " has multiple members."
            men = 0
            women = 0
            members = re.search(r'<th scope="row" style="text-align:left;">Members</th>(.+?)</tr>', infobox, re.S).group(1)
            members = members.split('<br />')
            members = [clean_tags(m) for m in members]
            for name in members:
                if ' ' in name:
                    if name.split(' ')[0] in male_names():
                        men = men + 1
                    elif name.split(' ')[0] in female_names():
                        women = women + 1
                else:
                    if name in male_names():
                        men = men + 1
                    elif name in female_names():
                        women = women + 1
            print "men:  %d -- women:  %d" % (men, women)
    else:
        print a, "no wiki url found"
        continue


    