"""
-- Appendix E
---- Regular expressions
------ Advanced search patterns
"""

import re

soda = "coca cola."

# . - any one character
print(re.findall(r".", soda))
# ['c', 'o', 'c', 'a', ' ', 'c', 'o', 'l', 'a', '.']

print(re.findall(r"c.", soda))
# ['co', 'ca', 'co']

# \. - the dot literal
print(re.findall(r"\.", soda))
# ['.']

print(re.findall(r"[co]", soda))
# ['c', 'o', 'c', 'c', 'o']
print(re.findall(r"[oc]", soda))
# ['c', 'o', 'c', 'c', 'o']

print(re.findall(r"[cdefghijkl]", soda))
# ['c', 'c', 'c', 'l']

print(re.findall(r"[c-l]", soda))
# ['c', 'c', 'c', 'l']

word = "bookkeeper"

print(re.findall(r"ee", word))
# ['ee']

print(re.findall(r"e{2}", word))
# ['ee']

print(re.findall(r"e{3}", word))
# []

print(re.findall(r"e{1,3}", word))
# ['ee', 'e']

transcription = "I can be reached at 555-123-4567. Look forward to talking to you soon."

print(re.findall(r"\d{3}-\d{3}-\d{4}", transcription))
# ['555-123-4567']

# + - one or more
print(re.findall(r"\d+-\d+-\d+", transcription))
# ['555-123-4567']
