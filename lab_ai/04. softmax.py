import tensorflow as tf

model2 = tf.keras.models.Sequential([
    tf.keras.layers.Embedding(3, 5),
    tf.keras.layers.SimpleRNN(4),
    tf.keras.layers.Dense(6),
    tf.keras.layers.Softmax()
])
model2.summary()