import cv2
import numpy as np
from tensorflow import keras
import streamlit as st
import pandas as pd
import requests


img_height = 224
img_width = 224

def decode_image(img, name):
    image = cv2.imdecode(
        np.frombuffer(img, dtype=np.uint8), -1)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    path = f"img/{name}"
    cv2.imwrite(path, cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    return path

@st.experimental_singleton()
def load_model():
    path = 'data/flower_classification.h5'
    try:
        url = 'https://machine-learning-services.s3.amazonaws.com/flower_classification/flower_classification.h5'
        print("Downloading from S3")
        r = requests.get(url)

        with open(path, 'wb') as file:
            file.write(r.content)

        print("Downloaded from S3")
        return keras.models.load_model(path)
    except:
        return keras.models.load_model(path)


def predict(image_path):
    image = keras.preprocessing.image.load_img(image_path, target_size=(img_height, img_width))
    input_arr = keras.preprocessing.image.img_to_array(image)
    input_arr = np.array([input_arr])  # Convert single image to a batch.
    y_pred = st.session_state['model'].predict(input_arr)
    y_pred = pd.DataFrame(y_pred, columns=['Margarita', 'Diente de Leon', 'Rosa', 'Girasol', 'Tulipan'])
    y_pred = y_pred * 100
    return image, y_pred