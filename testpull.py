from metapub import PubMedFetcher
import json
# import spacy
# import os

search_terms = input("Input search terms:")
fetch = PubMedFetcher()
pmids = fetch.pmids_for_query(search_terms, retmax=1000)

abstracts = {}
for pmid in pmids:
    abstracts[pmid] = fetch.article_by_pmid(pmid).abstract


with open(search_terms.replace(" ", "_") + ".log", "w") as f:
    f.write(json.dumps(abstracts))
