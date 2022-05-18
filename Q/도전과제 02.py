import tensorflow as tf
import pandas as pd

data = pd.read_csv('../data/titles.cvs')
titles = data['title'].values

# print(titles)

# 가공 과정, 전처리
tokenizer = tf.keras.preprocessing.text.Tokenizer()
tokenizer.fit_on_texts(titles)
word_count = len(tokenizer.word_index) + 1

print(tokenizer.word_index)
print(word_count)
