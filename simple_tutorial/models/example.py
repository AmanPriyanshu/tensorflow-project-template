import tensorflow as tf

### Do not duplicate or change the name of the function
### build_model and return the model defined by you.

def build_model():
	model = tf.keras.Sequential([
		tf.keras.Input(shape=(2,)),
		tf.keras.layers.Dense(4, activation='softmax')
	])
	model.compile(loss='categorical_crossentropy', metrics=['acc'], optimizer='adam')
	return model
