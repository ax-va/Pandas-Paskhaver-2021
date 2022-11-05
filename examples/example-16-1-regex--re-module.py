#!/usr/bin/python3
"""
-- Appendix E
---- Regular expressions
------ Introduction to Python’s re module
"""

import re

print(re.search("flower", "field of flowers"))
# <re.Match object; span=(9, 15), match='flower'>

# Found from index positions 9 (inclusive) to 15 (exclusive) for only the first match

print(re.search("flower", "Picking flowers in the flower field"))
# <re.Match object; span=(9, 15), match='flower'>

print(re.search("flower", "Barney the Dinosaur"))  # None

print(re.findall("flower", "Picking flowers in the flower field"))
# ['flower', 'flower']
print(repr(re.findall("flower", "Picking flowers in the flower field")))
# ['flower', 'flower']
