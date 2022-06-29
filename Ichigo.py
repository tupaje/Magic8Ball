import json

# Opening JSON file
f = open('answers.json')

# returns JSON object as
# a dictionary
data = json.load(f)

# Closing file
f.close()


# Iterating through the json
# list
# for i in data['answers']:
    # print(i)
  
# how to create a global constant variable
print(data['answers'][0])