from metapub import PubMedFetcher  # NB: requires my fork of metapub to remove HTMl parsing errors
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import spacy
import json
import os

search_terms = input("Input search terms:").lower()
file_name = search_terms.replace(" ", "_")

# for now, save abstracts as .log files
if os.path.isfile(file_name + ".log"):
    with open(file_name + ".log", "r") as f:
        abstr = json.loads(f.read())
else:
    fetch = PubMedFetcher()
    pmids = fetch.pmids_for_query(search_terms, retmax=1000)
    abstr = {}
    for pmid in pmids:
        abstr[pmid] = fetch.article_by_pmid(pmid).abstract
        
    with open(file_name + ".log", "w") as f:
        f.write(json.dumps(abstr))

sp = spacy.load("en_core_web_sm")
# sp.max_length = 2000000  # default limit is 100,000  words @ 1GB RAM consumption per 100k words
test_abstract = sp(str(abstr.values()).lower())
disallowed_terms = [search_terms, "receptor", "express",\
                    "expression", "g", "protein", "gpr37",\
                    "cell", "study", "result", "conclude"]  # rudimentary exclusion based on GPCR field common terms
disallowed_tags = ["VERB", "ADV", "ADJ"]  # maybe keep only NOUN and PNOUN?
words = [token.lemma_ for token in test_abstract\
            if not token.is_stop | token.is_space | token.is_punct | token.is_digit\
            and token.lemma_ not in disallowed_terms\
            and token.pos_ not in disallowed_tags]

counts = Counter(words)  # count freq of lemma
wc = WordCloud(background_color="white").generate_from_frequencies(dict(counts))  # I think WordCloud has a counter func inside...
plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
plt.savefig(f"{file_name}.png")
