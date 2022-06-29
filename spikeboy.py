import json
# To run this file in Shell, 
# type 'python spikeboy.py'
# press enter key

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
  
# always returns the first item in the list
print(data['answers'][0])