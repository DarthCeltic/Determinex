import re

with open('C:\\Dev\\Determinex\\scripts\\quickstart.ps1', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace any fancy quotes with standard quotes
content = content.replace('\u201c', '"').replace('\u201d', '"').replace('\u2018', "'").replace('\u2019', "'")
# Replace em-dashes
content = content.replace('\u2014', '-')
# Strip any stray non-ascii
content = content.encode('ascii', 'ignore').decode('ascii')

with open('C:\\Dev\\Determinex\\scripts\\quickstart.ps1', 'w', encoding='ascii') as f:
    f.write(content)
