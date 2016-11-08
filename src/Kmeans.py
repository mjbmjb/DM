# -*- coding: utf-8 -*- 
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import CountVectorizer as CV
from sklearn.feature_extraction.text import  TfidfVectorizer
import numpy

def load_data(file_path):
    data = []
    with open(file_path, 'r') as f:
        firstline = f.readline()

        for line in f.readlines():
            data.append(line)
    return data

def main():
    pass
    # kmeans.fit(new_X[0:100,:])
    # print kmeans.labels_


data = load_data('../dataset/a89_problem_name.txt')

count_vec = TfidfVectorizer(binary = False, decode_error = 'ignore', stop_words = 'english')# max_features=50000)
new_X = count_vec.fit_transform(data)

print new_X.shape
# with open('../dataset/x_to_vec.txt', 'w') as f:
# 	for row in range(new_X.shape[0]):
# 		for item in new_X[row]:
# 			f.write(str(item) + '\t')
# 		f.write('\n')
# f.close()

# numpy.savetxt('problem2vec.txt', new_X.toarray())

kmeans = KMeans(n_clusters=8, init='k-means++', max_iter=50, tol=0.1, random_state=None)
kmeans.fit(new_X)

lbs = kmeans.labels_