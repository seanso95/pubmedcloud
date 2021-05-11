from metapub import PubMedFetcher
<<<<<<< Updated upstream
import json
# import spacy
# import os

search_terms = input("Input search term:")
=======
import spacy

search_terms = input("Input search terms:")
>>>>>>> Stashed changes
fetch = PubMedFetcher()
pmids = fetch.pmids_for_query(search_terms, retmax=1000)

abstracts = {}
for pmid in pmids:
    abstracts[pmid] = fetch.article_by_pmid(pmid).abstract
<<<<<<< Updated upstream

with open(search_terms.replace(" ", "_") + ".log", "w") as f:
    f.write(json.dumps(abstracts))
=======
>>>>>>> Stashed changes
