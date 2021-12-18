"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
  reader = csv.reader(f)
  texts = list(reader)

with open('calls.csv', 'r') as f:
  reader = csv.reader(f)
  calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

incoming_calls = set()
outgoing_calls = set()
use_texts = set()

for text in texts:
  for i in range(2):
    use_texts.add(text[i])

for call in calls:
  outgoing_calls.add(call[0])
  incoming_calls.add(call[1])

telemarkerters = []

for call in outgoing_calls:
  if call not in use_texts and call not in incoming_calls:
    telemarkerters.append(call)

telemarkerters.sort()

print('These numbers could be telemarketers: ')

for telemarkerter in telemarkerters:
  print(telemarkerter)
