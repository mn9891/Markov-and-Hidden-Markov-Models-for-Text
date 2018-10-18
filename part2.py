#~ Amen Memmi
#~ AI Assignement 2
import random
import numpy as np
import editdistance


def closestDistance(prev,testWord):
	""" Selects the closest (in Levenshtein distance) word from the possible next words (bigram conditional probabilities) """
	possibleNext = []
	for line in biLines:
		if int(line.split()[0]) == prev:
			possibleNext.append([line])
			
	distanceVect = []																# This vector will contain distances of testWord to all possible next word 
	for line in possibleNext:										
		distanceVect.append(editdistance.eval(testWord,vocabLines[int(line[0].split()[1])-1].split()[1]))	# editdistance.eval(x,y) returns the Levenshtein distance between x and y
		line.append(editdistance.eval(testWord,vocabLines[int(line[0].split()[1])-1].split()[1]))
	minDistance=min(distanceVect)
	codeCorrected=int(possibleNext[np.argmin(distanceVect)][0].split()[1])						# Chosing the closest (returning its line number in vocab file)
	corrected=vocabLines[codeCorrected-1].split()[1]										# The corrected word
	prob=10**(float(possibleNext[np.argmin(distanceVect)][0].split()[2])/10)
	return codeCorrected, corrected, minDistance


def vertebiCorrection(s):										
	""" Corrects the input sentence (string) whose words contains typos using closestDistance to possibe next words """
	prev=153
	sentence=s.split()
	corSentence=[]
	distances=[]
	for word in sentence:
		aux=closestDistance(prev,word)
		corSentence.append(aux[1])
		prev=aux[0]
		distances.append(aux[2])
	correctedSentence = ' '.join(word for word in corSentence)
	return correctedSentence, distances


# loading files
with open('vocab.txt') as vocab:
    vocabLines = vocab.readlines()
with open('unigram_counts.txt') as unigramCounts:
    uniLines = unigramCounts.readlines()
with open('bigram_counts.txt') as bigramCounts:
    biLines = bigramCounts.readlines()
with open('trigram_counts.txt') as trigramCounts:
    triLines = trigramCounts.readlines()




"""Corretion of the proposed sentences"""
s=['I think hat twelve thousand pounds','she haf heard them','She was ulreedy quit live','John Knightly wasn\'t hard at work','he said nit word by']
for i in range(5):
	print(''.join((s[i],'\n => ',vertebiCorrection(s[i])[0])))
	print (vertebiCorrection(s[i])[1])
#~ print(vertebiCorrection(s[1]))	
#~ print closestDistance(153,'Ske')
