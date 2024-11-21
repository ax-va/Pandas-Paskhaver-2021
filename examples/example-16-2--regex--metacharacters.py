#!/usr/bin/python3
"""
-- Appendix E
---- Regular expressions
------ Metacharacters
"""

import re

sentence = "I went to the store and bought 5 apples, 4 oranges, and 15 plums."

print(re.findall(r"\d", sentence))
# ['5', '4', '1', '5']

# \d - match any digit
# \D - match any nondigit
print(re.findall(r"\D", sentence))
# ['I', ' ', 'w', 'e', 'n', 't', ' ', 't', 'o', ' ', 't', 'h', 'e', ' ', 's', 't', 'o', 'r', 'e', ' ', '
# a', 'n', 'd', ' ', 'b', 'o', 'u', 'g', 'h', 't', ' ', ' ', 'a', 'p', 'p', 'l', 'e', 's', ',', ' ',
# ' ', 'o', 'r', 'a', 'n', 'g', 'e', 's', ',', ' ', 'a', 'n', 'd', ' ', ' ', 'p', 'l', 'u', 'm', 's', '.']

# \w - match any word character
print(re.findall(r"\w", sentence))
# ['I', 'w', 'e', 'n', 't', 't', 'o', 't', 'h', 'e', 's', 't', 'o', 'r', 'e', 'a', 'n', 'd', 'b', 'o',
# 'u', 'g', 'h', 't', '5', 'a', 'p', 'p', 'l', 'e', 's', '4', 'o', 'r', 'a', 'n', 'g', 'e', 's', 'a', '
# n', 'd', '1', '5', 'p', 'l', 'u', 'm', 's']

# \W - match any nonword character
print(re.findall(r"\W", sentence))
# [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ',', ' ', ' ', ',', ' ', ' ', ' ', '.']

# \s - match any whitespace character
print(re.findall(r"\s", sentence))
# [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

# \S - match any nonwhitespace character
print(re.findall(r"\S", sentence))
# ['I', 'w', 'e', 'n', 't', 't', 'o', 't', 'h', 'e', 's', 't', 'o', 'r', 'e',
# 'a', 'n', 'd', 'b', 'o', 'u', 'g', 'h', 't', '5', 'a', 'p', 'p', 'l', 'e',
# 's', ',', '4', 'o', 'r', 'a', 'n', 'g', 'e', 's', ',', 'a', 'n', 'd', '1',
# '5', 'p', 'l', 'u', 'm', 's', '.']

print(re.findall(r"t", sentence))
# ['t', 't', 't', 't', 't']

print(re.findall(r"to", sentence))
# ['to', 'to']

# \b - a word boundary
# \bt - any t character after a word boundary
print(re.findall(r"\bt", sentence))
# ['t', 't']

# t\b - any t character before a word boundary, any t character before a space
print(re.findall(r"t\b", sentence))
# ['t', 't']

# \B - a nonword boundary
# \Bt - any t character that does not come after a word boundary
print(re.findall(r"\Bt", sentence))
# ['t', 't', 't']
