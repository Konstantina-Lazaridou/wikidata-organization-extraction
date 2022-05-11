from pywikibot.data import api
import pywikibot
from fuzzywuzzy import fuzz
import pprint

# Login to wikidata
site = pywikibot.Site("wikidata", "wikidata")
repo = site.data_repository()
# Search for an organization
org = 'N26'  # 'researchgate'
request = api.Request(site=site, parameters={'action' :'wbsearchentities' , 'format' : 'json' , 'language' : 'en', 'type' : 'item', 'search': org})
wikientries = request.submit()
# pprint.pprint(wikientries, indent=4)


descriptions = []
language = 'de'
boilerplate_descriptions = ['Wikimedia-Begriffsklärungsseite']
# Iterate over returned organizations
for entry in wikientries["search"]: 
    # if found organization matches queried organization, get descriptions for given language
    if fuzz.ratio(entry['label'], org) >= 83:
        print(f'[{entry["label"]}]: Match score with {org}: {fuzz.ratio(entry["label"], org)}')
        request = api.Request(site=site,
                          parameters={'action': 'wbgetentities', 'format': 'json', 'ids': entry['id']}).submit()
        try:
            for entity in request['entities']:
                if request['entities'][entity]['descriptions'][language]['value'].strip() and request['entities'][entity]['descriptions'][language]['value'].strip() not in boilerplate_descriptions:
                    descriptions.append(request['entities'][entity]['descriptions'][language]['value'].strip())
                    print(f'[{entry["label"]}]: descriptions : {descriptions}')
        except KeyError as e:
            print(f'[{entry["label"]}]: No description found')
