import tensorflow as tf
import pandas as pd

data = pd.read_csv('../data/titles.cvs')
titles = data['title'].values

tokenizer = tf.keras.preprocessing.text.Tokenizer()
tokenizer.fit_on_texts(titles)
# print(tokenizer.word_index)

# 수열,
sequence = tokenizer.texts_to_sequences(titles)
# print(titles[0])
print(sequence)
