import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def teranslate(word):

	word = word.lower()
	if word in data:
		return data[word]
	elif word.title() in data:
		return data[word.title()]
	elif word.upper() in data:
		return data[word.upper()]
	elif len(get_close_matches(word, data.keys())) > 0:
		print("did you mean {} instead".format(get_close_matches(word, data.keys())[0]))
		decide = input("press y for yes : ")
		if decide == "y":
			return data[get_close_matches(word, data.keys())[0]]
		else:
			return word + " not found"
	else:
		return word + " not found"

word = input("Enter the word you want to search: ")
output = teranslate(word)

if type(output) == list:
	for each in output:
		print(each)
else:
	print(output)

input()
