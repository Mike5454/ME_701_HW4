import re

entry = raw_input ("Give an input   ") 
pattern = r'.*p.t.*'

x = re.search(pattern, entry)

print x.group(0)