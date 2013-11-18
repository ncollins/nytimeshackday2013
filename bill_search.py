import re
import string

words = ["United States Code", "Federal Register", "U.S.C.",
         "Public Law", "Private Law"]

def get_matches(words, text):
    return re.findall(r'title \d+, United States Code', text)

def count_matches(words, text):
    return sum(len(m) for m in (re.findall(w, text) for w in words))

def find_key_words(text):
    return []

def strip_punc(phrase):
    for punc in string.punctuation:
        phrase = phrase.replace(punc, '')
    return phrase

def title_phrases(title):
    phrases, current = [], []
    for w in title.split():
        if w.istitle():
            current.append(w)
        elif current != []:
            phrases.append(current)
            current = []
    if current != []:
        phrases.append(current)
    return (p for p in (strip_punc(' '.join(p)) for p in phrases if len(p) < 5) if len(p) > 3)


test = '''

[Congressional Bills 113th Congress]
[From the U.S. Government Printing Office]
[H.R. 2327 Introduced in House (IH)]

113th CONGRESS
  1st Session
                                H. R. 2327

 To amend title 38, United States Code, to establish in the Department 
of Veterans Affairs a Veterans Economic Opportunity Administration, and 
                          for other purposes.
'''
