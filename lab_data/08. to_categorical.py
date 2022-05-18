import tensorflow as tf

data = [39, 12, 40, 6, 3]

categorical_data = tf.keras.utils.to_categorical(data, num_classes=41)
print(categorical_data)