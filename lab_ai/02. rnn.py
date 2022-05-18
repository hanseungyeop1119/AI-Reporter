import tensorflow as tf

model = tf.keras.models.Sequential([
    tf.keras.layers.Embedding(1, 5),
    tf.keras.layers.SimpleRNN(40)

])