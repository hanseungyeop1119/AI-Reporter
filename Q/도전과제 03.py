import numpy as np
import tensorflow as tf
import pandas as pd

data = pd.read_csv('../data/titles.cvs')
titles = data['title'].values

tokenizer = tf.keras.preprocessing.text.Tokenizer()
tokenizer.fit_on_texts(titles)
# print(tokenizer.word_index)
x = []
y = []
for i in range(2):
    sequence = tokenizer.texts_to_sequences([titles[i]])[0]
    d = np.array(sequence)
    e = len(sequence)
    for j in range(e):
        x.append(sequence[0:j + 1])
        y.append(d[1:])
print(x)
print(y)