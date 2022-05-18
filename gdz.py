import pandas as pd

data = pd.read_csv('data/titles.cvs')
titles = data['title'].values


word_index = dict()
for title in titles:
    words = title.split()
    for word in words:
        if word not in word_index:
            word_index[word] = len(word_index)
print(word_index)
print(len(word_index))

