"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv

with open('texts.csv', 'r') as f:
  reader = csv.reader(f)
  texts = list(reader)

with open('calls.csv', 'r') as f:
  reader = csv.reader(f)
  calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

telephone_duration = {}
max_time = 0
tele = ''
for call in calls:
  for i in range(2):
    if call[i] not in telephone_duration:
      telephone_duration[call[i]] = 0
    telephone_duration[call[i]] += int(call[3])
    if max_time < telephone_duration[call[i]]:
      max_time = telephone_duration[call[i]]
      tele = call[i]

print(tele + ' spent the longest time, ' + str(max_time) +
      ' seconds, on the phone during September 2016.')
