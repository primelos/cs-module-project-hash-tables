## We can use to transform data, like a substitution cipher

### Like a Caesar cypher!

## Make a table, mapping every letter to another letter
## given a string, build a new string by looking up each letter in our transposition table

import string

encode_table = {}

for i in range(26):
    letter = string.ascii_uppercase[i]
    other_letter = string.ascii_uppercase[i - 13]

    encode_table[letter] = other_letter




def encode(s):
    s = s.upper()

    new_string = ""
    for letter in s:
        if letter.isspace():
            new_string += letter
        else:
            new_string += encode_table[letter]

    return new_string

print(encode("hello everyone"))