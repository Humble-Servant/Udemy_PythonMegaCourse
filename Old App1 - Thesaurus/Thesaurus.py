# App #1 - Thesaurus

import json
from difflib import SequenceMatcher as sm, get_close_matches as get_close


filename = 'data.json'
data = json.load(open(filename, 'r'))


def define(key):
    if key in data:
        return key, data[key]
    elif key.lower() in data:
        return key.lower(), data[key.lower()]
    elif len(get_close(key, data.keys())) > 0:
        close_word = get_close(key, data.keys())[0]
        check = input(f'Did you mean {close_word}? (y/n)')
        return (close_word, data[close_word]) if check.lower() == 'y' else (None, None)
    else:
        return None, None


word = input('Enter a word: > ')

word, definitions = define(word)
if word:
    print(f'\n{word} - ')
    for index, definition in enumerate(definitions, 1):
        print(f'\t{index}. {definition}')
else:
    print(f'***************\nWord not found!\n***************\n')