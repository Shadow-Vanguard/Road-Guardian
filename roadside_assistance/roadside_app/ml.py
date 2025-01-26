# import tensorflow as tf
# from tensorflow.keras import layers, models
# import numpy as np
# from PIL import Image
# import os

# # Step 1: Load and preprocess the dataset
# def load_data(image_dir):
#     images = []
#     labels = []
#     for label in ['real', 'ai_generated']:
#         for filename in os.listdir(os.path.join(image_dir, label)):
#             img_path = os.path.join(image_dir, label, filename)
#             img = Image.open(img_path).resize((128, 128))  # Resize images
#             images.append(np.array(img) / 255.0)  # Normalize
#             labels.append(0 if label == 'real' else 1)  # 0 for real, 1 for AI-generated
#     return np.array(images), np.array(labels)

# # Step 2: Create the model
# def create_model():
#     model = models.Sequential([
#         layers.Conv2D(32, (3, 3), activation='relu', input_shape=(128, 128, 3)),
#         layers.MaxPooling2D(pool_size=(2, 2)),
#         layers.Conv2D(64, (3, 3), activation='relu'),
#         layers.MaxPooling2D(pool_size=(2, 2)),
#         layers.Flatten(),
#         layers.Dense(64, activation='relu'),
#         layers.Dense(1, activation='sigmoid')  # Binary classification
#     ])
#     model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
#     return model

# # Step 3: Train the model
# def train_model(images, labels):
#     model = create_model()
#     model.fit(images, labels, epochs=10, validation_split=0.2)
#     return model

# # Step 4: Convert the model to TensorFlow Lite
# def convert_to_tflite(model):
#     converter = tf.lite.TFLiteConverter.from_keras_model(model)
#     tflite_model = converter.convert()
#     with open('model.tflite', 'wb') as f:
#         f.write(tflite_model)

# # Step 5: Analyze uploaded image
# def analyze_image(image_path, metadata):
#     img = Image.open(image_path).resize((128, 128))
#     img_array = np.array(img) / 255.0
#     img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension

#     # Load the TFLite model and perform inference
#     interpreter = tf.lite.Interpreter(model_path='model.tflite')
#     interpreter.allocate_tensors()
#     input_details = interpreter.get_input_details()
#     output_details = interpreter.get_output_details()

#     interpreter.set_tensor(input_details[0]['index'], img_array)
#     interpreter.invoke()
#     output_data = interpreter.get_tensor(output_details[0]['index'])

#     # Check the result
#     if output_data[0][0] > 0.5:  # AI-generated
#         print("Submission declined: AI-generated image detected.")
#     else:
#         print("Submission accepted. Incident report submitted.")

# # Example usage
# if __name__ == "__main__":
#     image_dir = 'path/to/your/dataset'
#     images, labels = load_data(image_dir)
#     model = train_model(images, labels)
#     convert_to_tflite(model)

#     # Analyze an uploaded image
#     uploaded_image_path = 'path/to/uploaded/image.jpg'
#     metadata = {
#         'location': 'example_location',
#         'phone_model': 'example_model',
#         'timestamp': '2023-10-01 12:00:00'
#     }
#     analyze_image(uploaded_image_path, metadata)