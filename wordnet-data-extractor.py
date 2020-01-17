import json
from collections import defaultdict
from nltk.corpus import wordnet as wn


PARTS_OF_SPEECH_MAPPER = {
    'n': 'noun',
    'v': 'verb',
    'a': 'adjective',
    's': 'satellite',
    'r': 'adverb',
}


def clean_word(word):
    return word.replace('_', ' ')


def get_name_and_pos(word):
    try:
        name, pos, _ = word.split('.')
        return name.replace("_", " "), PARTS_OF_SPEECH_MAPPER[pos]
    except:
        print(word)
    return None, None


def save_to_file(keys, synonyms, hyponyms, hypernyms, output_file_name='wordnet30-eng.json'):
    data = dict()
    for key in keys:
        data[key] = dict()
        if key in synonyms:
            data[key]['synonyms'] = list(synonyms[key])
        if key in hyponyms:
            data[key]['hyponyms'] = list(hyponyms[key])
        if key in hypernyms:
            data[key]['hypernyms'] = list(hypernyms[key])

    with open(output_file_name, "w") as write_file:
        json.dump(data, write_file)


def remove_name(name: str, values: {set}):
    candidates = set()
    for value in values:
        if value.lower() == name.lower():
            candidates.add(value)
    for candidate in candidates:
        values.remove(candidate)
    return values


synonyms = defaultdict(set)
hyponyms = defaultdict(set)
hypernyms = defaultdict(set)
keys = set()
for synset in wn.all_synsets():
    cur_synonyms = {clean_word(l) for l in synset._lemma_names}
    cur_hyponyms = {
        clean_word(syn._name.split('.')[0])
        for syn in synset.hyponyms()
        if len(syn._name.split('.')) == 3
    }
    cur_hypernyms = {
        clean_word(syn._name.split('.')[0])
        for syn in synset.hypernyms()
        if len(syn._name.split('.')) == 3
    }
    name, pos = get_name_and_pos(synset._name)
    if name is not None:
        key = f'{name}:{pos}'
        cur_synonyms = remove_name(name, cur_synonyms)
        if cur_synonyms:
            synonyms[key] = synonyms[key].union(cur_synonyms)
        cur_hyponyms = remove_name(name, cur_hyponyms)
        if cur_hyponyms:
            hyponyms[key] = hyponyms[key].union(cur_hyponyms)
        cur_hypernyms = remove_name(name, cur_hypernyms)
        if cur_hypernyms:
            hypernyms[key] = hypernyms[key].union(cur_hypernyms)
        if cur_synonyms or cur_hyponyms or cur_hypernyms:
            keys.add(key)


save_to_file(keys, synonyms, hyponyms, hypernyms)
