# NLP code snippets
* [WordNet data extractor](#wordnet-data-extractor)
* [Generation of inflected form of a word](#generation-of-inflected-form-of-a-word)

## [WordNet data extractor](https://github.com/duketemon/nlp-snippets/blob/master/wordnet-data-extractor.py)
Extracts all synonyms, hyponyms, hypernyms from WordNet lexical database

### Dependencies
```bash
pip3 install nltk
```

## [Generation of inflected form of a word](https://github.com/duketemon/nlp-snippets/blob/master/inflected-form.py)
Returns the the inflected form of a word based on a supplied Penn Treebank part-of-speech tag

### Dependencies
```bash
pip3 install spacy
pip3 install pyinflect
python3 -m spacy download en_core_web_sm
```
