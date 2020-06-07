import pymorphy2
import random
import re
import volkifyParse

morph = pymorphy2.MorphAnalyzer()

def parseDot(phrase):
	return [i for i in re.split(r'[.!?]', phrase) if i != '']

def parseWords(arr):
	return re.split(r'\b', arr)

def parseNOUN(arr):
	return [i for i in range(len(arr)) if morph.parse(arr[i])[0].tag.POS in ['NOUN', 'NPRO', 'ADJF']]

def concatenationSentence(arr):
	sep = ''
	return sep.join(arr) + '.'

def declension(word, replace):
	case = morph.parse(word)[0].tag.case
	number = morph.parse(word)[0].tag.number
	return morph.parse(replace)[0].inflect({number, case}).word

def preProcStr(phrase):
	return phrase.replace('\"', '')

def volkify(phrase, volk):
	try:
		volk_str = ''
		sentences = parseDot(preProcStr(phrase))

		for i in sentences:
			sentence = parseWords(i)

			rand_volk = random.choice(parseNOUN(sentence))
			
			sentence[rand_volk] = declension(sentence[rand_volk], volk)
			volk_str = volk_str + concatenationSentence(sentence)

		return volk_str
	except:
		return volk
