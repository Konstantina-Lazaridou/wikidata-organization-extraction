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
