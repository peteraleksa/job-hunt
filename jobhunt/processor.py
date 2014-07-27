import nltk, re, pprint

class PostProcessor(object):

	def process(item):
		tokenized_text = []
		tokenized_text.extend(nltk.word_tokenize(item['text']))
		keywords = getKeywords(tokenized_text, 4)
		return keywords

	def extract_keywords(text, limit):
		common = open("common.txt").read().split('\n')
		word_dict = {}
		for word in text:
			if word not in common and word.isalnum() :
				if word not in word_dict:
					word_dict[word] = 1
				if word in word_dict:
					word_dict[word] += 1
		top_words = sorted(word_dict.items(), key=lambda(k,v):(v,k), reverse=True)[0:limit]
		top = []
		for w in top_words:
			top.append(w[0])
		return top