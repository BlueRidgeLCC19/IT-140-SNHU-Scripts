import re
#The string to search for the regular expression occurrence (This is provided to the student)
pattern = r'\b[regular].[expression] .+\b'

search_string ='''This is a string to search for a regular expression like regular expression or 
regular-expression or regular:expression or regular&expression'''

match1 = re.findall(search_string, pattern)
if match1 is not None:
  print(pattern + 'matched')
else:
  print(pattern + 'did not match')