import numpy as np
import tensorflow as tf
import pandas as pd
import os

if not os.path.exists('../classification_data'):
    os.mkdir('../classification_data')

data = pd.read_csv('../data/titles.cvs')
titles = data['title'].values

tokenizer = tf.keras.preprocessing.text.Tokenizer()
tokenizer.fit_on_texts(titles)

sequence = tokenizer.texts_to_sequences(titles)
d = np.array(sequence)
e = len(sequence)
x = []
y = []

for i in range(e):
    for j in range(len(sequence[i])):
        x.append(sequence[0:j + 1])
        y.append(d[1:].tolist())

data = pd.DataFrame({'x': x})
data2 = pd.DataFrame({'y': y})
# 한글이 포함되어 있다면 인-코딩이 필요.!
data.to_csv('../classification_data/x.cvs', encoding='utf-8')
data2.to_csv('../classification_data/y.cvs', encoding='utf-8')
# print(x, '\n')
# print()
# print()
# print('y :', y)
