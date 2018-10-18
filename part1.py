#~ Amen Memmi
#~ AI Assignement 2
import random
import numpy as np
import editdistance


def NextFromBigram(previous, nChoices=10):	
	""" Selects the next word from the nChoices possible next words using bigram conditional probabilities """	
	possibleNext = []
	for line in biLines:
		if int(line.split()[0]) == previous:
			possibleNext.append([line])						#list of possible next words
	probs = []
	for line in possibleNext:  									# list of the probabilities of possible next words
		probs.append(float(line[0].split()[2]))

	selectedPossibeNext = []
	for k in np.argsort(probs)[-nChoices:]:  						# np.argsort(probs)[-nChoices:] => the nChoices highest probs
		selectedPossibeNext.append([vocabLines[int(possibleNext[k][0].split()[1]) - 1].split()[1],
					int(possibleNext[k][0].split()[1])]) 			# generate the nChoices most probable words
	r = random.randint(0, len(selectedPossibeNext) - 1)
	prob = 10**(float(possibleNext[r][0].split()[2])/10)
	return (selectedPossibeNext[r][0], selectedPossibeNext[r][1],prob)


def NextFromTrigram(p_previous, previous, nChoices=10):
	""" Selects the next word from the nChoices possible next words using bigram conditional probabilities """
	possibleNext = []
	for line in triLines:
		if int(line.split()[0]) == p_previous and int(line.split()[1]) == previous:
			possibleNext.append([line])						#list of possible next words
	probs = []				
	for line in possibleNext:  									# list of the probabilities of possible next words
		probs.append(float(line[0].split()[2]))

	selectedPossibeNext = []
	for k in np.argsort(probs)[-nChoices:]:  						# np.argsort(probs)[-nChoices:] => the nChoices highest probs
		selectedPossibeNext.append([vocabLines[int(possibleNext[k][0].split()[2]) - 1].split()[1],
					int(possibleNext[k][0].split()[2])])			# generate the nChoices most probable words
	r = random.randint(0, len(selectedPossibeNext) - 1)
	prob = 10**(float(possibleNext[r][0].split()[3])/10)
	return (selectedPossibeNext[r][0], selectedPossibeNext[r][1],prob)


def generateSentence(nChoices=10):
	""" Generates a sentence from the vocabulary acording to the trigram probabilities, next word is chosen from the nChoices most
	probables next words """
	sentence = [[vocabLines[152].split()[1]]]
	sentenceC = [[153]]
	x1 = NextFromBigram(153, nChoices)
	prob=1
	sentenceC.append([x1[1]])
	sentence.append([x1[0]])
	x = (-1, -1)
	while x[1] != 152:			#<\s> (whose number is 153)  is the stop condition
		x = NextFromTrigram(sentenceC[len(sentenceC) - 2][0], sentenceC[len(sentenceC) - 1][0], nChoices)
		sentenceC.append([x[1]])
		sentence.append([x[0]])
		prob*=x[2]			#cumulative prior sample probability

	randSentence= ' '.join(word[0] for word in sentence)
	return randSentence, round(prob, 7)

# loading files
with open('vocab.txt') as vocab:
    vocabLines = vocab.readlines()
with open('unigram_counts.txt') as unigramCounts:
    uniLines = unigramCounts.readlines()
with open('bigram_counts.txt') as bigramCounts:
    biLines = bigramCounts.readlines()
with open('trigram_counts.txt') as trigramCounts:
    triLines = trigramCounts.readlines()



"""Generating a sentence"""
print(generateSentence(5))


