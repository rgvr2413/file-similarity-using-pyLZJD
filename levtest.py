from os import listdir
from Levenshtein import distance

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

filepath = '' # Change path to your directory

# Read all files in a directory
dir = listdir(filepath)

print("Files found in directory......")
print(dir)

d = pairFile(dir)

#print(distance('a', 'b'))
filepath = '' # Change path according to your directory 

filedir = listdir(filepath)
#print(filedir)

f = filepath + filedir[0]
#print(f)
file1 = open(f, 'rb').read()

f = filepath + filedir[1]

file2 = open(f, 'rb').read()
#print(file1)

print("Comparing files...........")
for f in d:
    a = f[0]
    a_src = filepath + a
    a1 = open(a_src, 'rb').read()
    b_src = filepath + f[1]
    b1 = open(b_src, 'rb').read()
    print(a, f[1], "Levenshtein Distance - ", distance(a1, b1))
	
#print(distance(file1, file2))



