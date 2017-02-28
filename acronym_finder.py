#!/usr/bin/python3

import re

def getWords():
	print ('Enter a list of words you may want to represent with each character of your acronym.')
	possibles = []
	while True:
		print("Enter a comma-separated list of words, enter a blank line to continue:")
		words = input("> ").lower().split(",")
		words = [w.strip() for w in words]
		if words == ['']: break
		possibles.append(words)
	# print(possibles)
	return(possibles)

"""
This creates an array of dicts to store the possible first letters
for each position and the words associated with them
"""
def makeInitials(possibles):
	initals = []
	for pos in possibles:
		# of the form: {"x":["words"]} where words are all the words beginning with 
		words = {}
		for term in pos:
			if term[0] in words.keys():
				words[term[0]].append(term)
			else:
				words[term[0]]=[term]
		initals.append(words)
	# print(initals)
	return(initals)


def makeRegexp (initials):
	regexp = "^"
	for entry in initials:
		regexp += "["
		for letter in entry.keys():
			regexp += letter
		regexp += "]"
	regexp += "$"
	# print(regexp)
	regexp = re.compile(regexp)
	return(regexp)

def findMatches(regexp):
	matches = []
	with open('/usr/share/dict/words', 'r') as language:
		i = 0
		for line in language:
			m = regexp.fullmatch(line.lower().strip())
			if m:
				matches.append(m.string)
			i += 1
	print (str(len(matches)) + " found")
	return(matches)

def backMatch(matches, initials):
	for m in matches:
		print("--- ---")
		m = list(m)
		for c in m:
			print(c + " -- " + str(initials[m.index(c)][c]))
	return

def makeInput():
	possibles = getWords()
	initials = makeInitials(possibles)
	return(initials)

def search (initials):
	regexp = makeRegexp(initials)
	matches = findMatches(regexp)
	return(matches)

initials = makeInput()
matches = search(initials)
backMatch(matches, initials)
