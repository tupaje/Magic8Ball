import sys
import json
import random

print('~~~~~ Magic 8 Ball ~~~~~')

args = None
if 1 < len(sys.argv):
    args = sys.argv[1]

# Opening JSON file
f = open('answers.json')

# returns JSON object as a dictionary
data = json.load(f)

# Closing file
f.close()
# https://docs.python.org/3/library/random.html#examples
index = random.randrange(len(data['answers']))

if args:
    print(data['answers'][index])
else:
  print('Ask me anything.')
