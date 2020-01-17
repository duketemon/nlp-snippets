import spacy
# Don't remove pyinflect! It's an extension of the spacy
import pyinflect


def apply_tag(nlp, word: str, tag: str):
    token = nlp(word)[0]
    changed_word = token._.inflect(tag)
    return changed_word if changed_word is not None else word


nlp = spacy.load('en_core_web_sm')
source_word = 'making'
doc = nlp(source_word)
token = doc[0]

print(apply_tag(nlp, 'do', token.tag_))
print(apply_tag(nlp, 'did', token.tag_))
