import tensorflow as tf

model = tf.keras.models.Sequential([
    tf.keras.layers.Embedding(15, 8)
])

model.summary()