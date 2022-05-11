# wikidata-organization-extraction
Contains scripts to access Wikidata and get data for companies based on their name

## Requirements
- pywikibot
- fuzzywuzzy

## Get organization descriptions

- Create a virtual environment with `requirements.yml`. I have used Anaconda.
- Set `org` in `get_organization_descriptions.py` to a company name.
- Set `language` to the language you want to retrieve company descriptions in.
- If the language is not German, then change the `boilerplate_descriptions` accordingly (use "Wikimedia disambiguation page" for English).
- Run the script by executing `python get_organization_descriptions.py`.

The code will use the example of N26 to get and return German descriptions for this company.
The output will look like:

```
[N26]: Match score with N26: 100
[N26]: descriptions : ['Europäische Neobank mit Sitz in Deutschland']
[N26]: Match score with N26: 100
```
This means that out of all the Wikidata entries that were returned for our "N26" query, two entries matched sufficiently. Namely the matching score for both entries is 100%.

The first entry's name is "N26", with the description "Europäische Neobank mit Sitz in Deutschland". The second is also called "N26", but its description is not included in the output, because it does not provide relevant information (it is "Wikimedia-Begriffsklärungsseite").

With this script the results to consider from the Wikidata search are reduced and it is possible to avoid processing irrelevant entries that are not N26, e.g., the N26 road in Luxembourg.

## Validate organization type

- Create a virtual environment with `requirements.yml`. The `fuzzywuzzy` library is not necessary.
- Set `org` in `get_organization_descriptions.py` to a company name.
- Run the script by executing `python validate_organization_type.py`
- If the given organization name is indeed an organization, the output will print a confirmation

This script uses a very basic filter to check which of the returned Wikidata entries related to "N26" are indeed organizations. This is another way to avoid entries like the above, i.e., the N26 road in Luxembourg.
The company entries in Wikidata can be identified by checking their core properties. The full list of properties can be found [here](https://www.wikidata.org/wiki/Wikidata:WikiProject_Companies/Properties). 

This script is checking whether the returned Wikidata entry is an instance of "item", whether it has an official website and also contains headquarters/location information.
The output for the N26 example is:
```
[N26]: is an organization
```

This entry is the English Wikidata page for N26.

```
{'id': 'Q27479372', 'title': 'Q27479372', 'pageid': 29202592, 'display': {'label': {'value': 'N26', 'language': 'en'}, 'description': {'value': 'German bank', 'language': 'en'}}, 'repository': 'wikidata', 'url': '//www.wikidata.org/wiki/Q27479372', 'concepturi': 'http://www.wikidata.org/entity/Q27479372', 'label': 'N26', 'description': 'German bank', 'match': {'type': 'label', 'language': 'en', 'text': 'N26'}}
```



