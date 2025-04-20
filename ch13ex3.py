"""In a previous section, we used the shelve module to make a key-value store that maps from a sorted string of letters
to a list of anagrams. To finish the example, write a function called add_word that takes as arguments a string and
a shelf object.  It should sort the letters of the word to make a key, then check whether the key
is already in the shelf. If not, it should make a list that contains the new word and add it to the
shelf. If so, it should append the new word to the
existing value"""
import shelve

def sort_word(word):
    return ''.join(sorted(word))

def add_word(word, db):
    key = sort_word(word)

    if key in db:
        word_list = db[key]
        word_list.append(word)
        db[key] = word_list
    else:
        db[key] = [word]

# create new shelf
db = shelve.open('anagram_map', 'n')

# add words
add_word('pots', db)
add_word('tops', db)
add_word('stop', db)
add_word('spot', db)
add_word('post', db)

for key in db:
    print(key, '->', db[key])

db.close()