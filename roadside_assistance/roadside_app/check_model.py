from tensorflow.keras.models import load_model
import os

   # Specify the path to your model
model_path = 'E:/24-7-Roadside-Assistance--main (1)/roadside_assistance/roadside_app/model.h5'  # Adjust the path as necessary

   # Check if the model file exists
if os.path.exists(model_path):
       try:
           model = load_model(model_path)
           print("Model loaded successfully.")
       except OSError as e:
           print(f"Error loading model: {e}")
else:
       print("Model file does not exist.")