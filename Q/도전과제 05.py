import tensorflow as tf
import os

# 1
model = tf.keras.models.Sequential([
    tf.keras.layers.Embedding(3, 5)
])

if not os.path.exists('../models'):
    os.mkdir('../models')
model.save('../models/Embedding.h5')

# 2
model = tf.keras.models.Sequential([
    tf.keras.layers.Input(shape=(None, 8)),
    tf.keras.layers.SimpleRNN(4)
])

if not os.path.exists('../models'):
    os.mkdir('../models')
model.save('../models/SimpleRNN.h5')

# 3
model = tf.keras.models.Sequential([
    tf.keras.layers.Input(shape=(4)),
    tf.keras.layers.Dense(6)
])

if not os.path.exists('../models'):
    os.mkdir('../models')
model.save('../models/Dense.h5')

# 4
model = tf.keras.models.Sequential([
    tf.keras.layers.Input(shape=(6)),
    tf.keras.layers.Softmax()
])
model.summary()
if not os.path.exists('../models'):
    os.mkdir('../models')
model.save('../models/Softmax.h5')
