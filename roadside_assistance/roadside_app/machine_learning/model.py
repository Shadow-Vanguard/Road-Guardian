import tensorflow as tf
from tensorflow.keras import layers, models
import numpy as np
import os
from sklearn.model_selection import train_test_split

   # Load your dataset
def load_data(data_dir):
       images = []
       labels = []
       for label in os.listdir(data_dir):
           for img_file in os.listdir(os.path.join(data_dir, label)):
               img_path = os.path.join(data_dir, label, img_file)
               img = tf.keras.preprocessing.image.load_img(img_path, target_size=(128, 128))
               img_array = tf.keras.preprocessing.image.img_to_array(img)
               images.append(img_array)
               labels.append(0 if label == 'real' else 1)  # 0 for real, 1 for AI-generated
       return np.array(images), np.array(labels)

   # Load data
data_dir = 'path/to/your/dataset'  # Update this path
X, y = load_data(data_dir)

   # Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

   # Normalize the images
X_train = X_train / 255.0
X_test = X_test / 255.0

   # Create the model
model = models.Sequential([
       layers.Conv2D(32, (3, 3), activation='relu', input_shape=(128, 128, 3)),
       layers.MaxPooling2D(pool_size=(2, 2)),
       layers.Conv2D(64, (3, 3), activation='relu'),
       layers.MaxPooling2D(pool_size=(2, 2)),
       layers.Flatten(),
       layers.Dense(64, activation='relu'),
       layers.Dense(1, activation='sigmoid')  # Binary classification
   ])

   # Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

   # Train the model
model.fit(X_train, y_train, epochs=10, validation_data=(X_test, y_test))

   # Save the model
model.save('image_classifier.h5')