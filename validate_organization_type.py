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

# Iterate over returned organizations to check if they are organizations
for entry in wikientries["search"]: 
    item = pywikibot.ItemPage(repo, entry['id'])
    item.get()
    if item.claims:
        # if entry is an item, has an official website and headquarters, assume it is a company
        if 'P31' in item.claims and 'P856' in item.claims and 'P159' in item.claims:
            print(f'[{entry["label"]}]: is an organization')
