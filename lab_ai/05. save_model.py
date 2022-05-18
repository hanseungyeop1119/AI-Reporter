import tensorflow as tf
import os

model = tf.keras.models.Sequential([
    tf.keras.layers.Embedding(3, 5),
    tf.keras.layers.SimpleRNN(4),
    tf.keras.layers.Dense(6),
    tf.keras.layers.Softmax()
])
model.summary()

if not os.path.exists('../models'):
    # 폴더를 만들어 준다
    os.mkdir('../models')
model.save('../models/softmax.h5')