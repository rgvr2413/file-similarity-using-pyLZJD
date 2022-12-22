import pyLZJD
from os import listdir
from pyLZJD import digest, vectorize
from Levenshtein import *

# Function to create pairs of files
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


filepath = "" # Change to your directory 

# Read file - Sample tests
a = digest("d_stats.py") 
b = digest("sorel_stats.py")

# Read all files in a directory
dir = listdir(filepath)

print("Files found in directory......")
print(dir)

d = pairFile(dir)

similarity = []
similar = {}
#print(d)
#print(d[0][0], digest(d[0][0]))

# Checking for similarities with files
print("Comparing files...........")
for f in d:
	fpath1 = filepath + f[0]
	a = open(fpath1, 'rb').read()
	a1 = digest(a)
	fpath2 = filepath + f[1]
	b = open(fpath2, 'rb').read()
	#a_src = filepath + "/" + a
	#b_src = filepath + "/" + f[1]
	#print(a_src)
	#print(b_src)
	#a2 = open(a_src, errors = 'ignore').read()
	#b2 = open(f[1], errors = 'ignore').read()
	b1 = digest(b)
	print(fpath1, fpath2, "Similarity - ",pyLZJD.sim(a1, b1))
	print(fpath1, fpath1, "Similarity - ",pyLZJD.sim(a1, a1))
	#print( "Levenshtein Distance - ", distance(a2, b2))
	similar[f[1]] = pyLZJD.sim(a1, digest(f[1]))
	similarity.append(similar[f[1]])
	#similarity.append(pyLZJD.sim(a1, digest(f[1])))
	
similarity.sort(reverse = True)		
print("Sorted similarity -")
print(similarity)
'''
for i in d:
	a = i[0]
	a1 = vectorize(a)
	print(a, i[1], "Similarity - ", pyLZJD.sim(a1, vectorize(i[1])))

'''
'''
print(a)
print(b)
'''

#Calculate the similarity index
#How similar are the files ?  0 < sim < 1, when sim = 1 it means the files are identical
'''print("Cosine similarity -", pyLZJD.sim(a,a))'''

#from Levenshtein import *

#print("Levenshtein distance - ", dir[1], dir[2], distance(dir[1], dir[2]))

# Term Document Matrix

import pandas as pd
from pprint import pprint

#with open(dir[0]) as f:
#	lines = f.readlines()
#	data = []
#	response_id = []
#	score = []
	#for line in lines[1:]:
