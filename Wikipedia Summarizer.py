import wikipedia

# Search for a page
search_query = input("Enter your search query: ")
search_results = wikipedia.search(search_query)

if not search_results:
    print("No results found.")
else:
    # Select the first search result
    page_title = search_results[0]
    
    # Load the page
    page = wikipedia.page(page_title)
    
    # Print the entire page text
    print("Title:", page.title)

# importing libraries 
import nltk 
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize, sent_tokenize 
print("Summary : ")
# Input text - to summarize 
text = page.content
# Tokenizing the text 
stopWords = set(stopwords.words("english")) 
words = word_tokenize(text) 

# Creating a frequency table to keep the 
# score of each word 

freqTable = dict() 
for word in words: 
	word = word.lower() 
	if word in stopWords: 
		continue
	if word in freqTable: 
		freqTable[word] += 1
	else: 
		freqTable[word] = 1

# Creating a dictionary to keep the score 
# of each sentence 
sentences = sent_tokenize(text) 
sentenceValue = dict() 

for sentence in sentences: 
	for word, freq in freqTable.items(): 
		if word in sentence.lower(): 
			if sentence in sentenceValue: 
				sentenceValue[sentence] += freq 
			else: 
				sentenceValue[sentence] = freq 



sumValues = 0
for sentence in sentenceValue: 
	sumValues += sentenceValue[sentence] 

# Average value of a sentence from the original text 

average = int(sumValues / len(sentenceValue)) 

# Storing sentences into our summary. 
summary = '' 
for sentence in sentences: 
	if (sentence in sentenceValue) and (sentenceValue[sentence] > (1.2 * average)): 
		summary += " " + sentence 
print(summary[:1000]) #to adjust the length of summary
print("End Of Summary")
