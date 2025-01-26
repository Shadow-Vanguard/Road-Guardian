import numpy as np
import tensorflow as tf

   # Load the model
model = tf.keras.models.load_model('path/to/image_classifier.h5')  # Update this path

def classify_image(image_path):
       img = tf.keras.preprocessing.image.load_img(image_path, target_size=(128, 128))
       img_array = tf.keras.preprocessing.image.img_to_array(img) / 255.0
       img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
       prediction = model.predict(img_array)
       return 'AI-generated' if prediction[0][0] > 0.5 else 'Real'