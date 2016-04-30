import re
import requests
from pyechonest import artist

for a in artist.top_hottt(start=0, results=1):
    discogs_id = a.get_foreign_id('discogs').split(':')[2]
    url = 'http://api.discogs.com/artists/%s/releases' % discogs_id
    r = requests.get(url)
    for release in r.json()['releases']:
        format = release.get('format', '')
        if 'single' in format.lower():
            print release['title'], release['thumb']

