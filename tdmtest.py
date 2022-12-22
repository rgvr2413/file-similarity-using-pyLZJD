import pandas as pd 
from pprint import pprint
from os import listdir 
import os
'''
def pairFile(dir):
	dir_pair = []
	for f in dir:
		for f1 in dir:
			if f == f1:
				continue
			if [f1, f] in dir_pair:
				continue
			dir_pair.append([f, f1])
	return dir_pair
'''

filepath = ""  # Change path to your directory

# Read all files in a directory
dir = listdir(filepath)

print("Files found in directory......")
print(dir)
'''
# Import file
for file in dir:
	fpath1 = filepath + file
	print(file)
	with open(fpath1, 'r', errors = 'ignore', encoding='utf-8') as f:
		lines = f.readlines()
		columns = lines[0].split('\t')
		print(columns)
		data = []
		response_id= []
		score = []
		for line in lines[1:]:
			temp = line.split('\t')
			temp[0] = temp[0].rstrip('\x00')
			print(temp)	
			if temp[0] == '1':
				data.append(temp[-1])
				response_id.append(int(temp[0]))
				score.append(int(temp[2]))
			else: 
				None

# Construct a dataframe ("doc") which includes the response_id, responses, and the score        
doc = pd.DataFrame(list(zip(response_id, data, score)))
doc.columns = ['id', 'response', 'score']

# Activate CountVectorizer
from sklearn.feature_extraction.text import CountVectorizer

# Count Vectorizer
vect = CountVectorizer()  
vects = vect.fit_transform(doc.response)

# Select the first five rows from the data set
td = pd.DataFrame(vects.todense()).iloc[:5]  
td.columns = vect.get_feature_names()
term_document_matrix = td.T
term_document_matrix.columns = ['Doc '+str(i) for i in range(1, 6)]
term_document_matrix['total_count'] = term_document_matrix.sum(axis=1)

# Top 25 words 
term_document_matrix = term_document_matrix.sort_values(by ='total_count',ascending=False)[:25] 

# Print the first 10 rows 
print(term_document_matrix.drop(columns=['total_count']).head(10))
'''


import textmining
import nltk.stem as stemmer
from pyLZJD import digest

tdm = textmining.TermDocumentMatrix()

file = filepath + dir[0]

with open(file, 'rb') as f:
	doc1 = f.read()

#print("Type-", type(doc1[1]))
#tdm.add_doc(doc1[0])
#tdm.add_doc(doc1[1])
#tdm.add_doc(doc1[2])
#print(tdm)
for d in doc1:
	print(d)

print(doc1)
'''
for d in dir:
	file = filepath + d
	with open(file, 'r', errors = 'ignore', encoding = 'utf-8') as f:
		doc1 = f.readlines()
	for doc in doc1:
		tdm.add_doc(doc)
		print(doc)

if os.path.exists('sample_tdm.csv'):
	os.remove('sample_tdm.csv')
	tdm.write_csv('sample_tdm.csv', cutoff = 1)
else:
	tdm.write_csv('sample_tdm.csv', cutoff = 1)
'''
