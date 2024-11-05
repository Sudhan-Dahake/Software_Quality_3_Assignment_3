"""
This module handles loading a pre-trained model, preprocessing images, and making predictions.
It includes two main functions: `preprocess_img` to prepare an image for prediction,
and `predict_result` to predict the class label for a given image input.
"""

from keras.models import load_model
from keras.utils import img_to_array
import numpy as np
from PIL import Image

# Loading model
model = load_model("digit_model.h5")


# Preparing and pre-processing the image
def preprocess_img(img_path):
    """Prepares and preprocesses the image for prediction.

    Args:
        img_path (string): The filepath of the image to be preprocessed.

    Returns:
        numpy.ndarray: Preprocessed image array reshaped for model input.
    """

    op_img = Image.open(img_path)
    img_resize = op_img.resize((224, 224))
    img2arr = img_to_array(img_resize) / 255.0
    img_reshape = img2arr.reshape(1, 224, 224, 3)
    return img_reshape


# Predicting function
def predict_result(predict):
    """Predicts the class label for the given preprocessed image.

    Args:
        image_array (numpy.ndarray): The preprocessed image array.

    Returns:
        int: The predicted class label.
    """

    pred = model.predict(predict)
    return np.argmax(pred[0], axis=-1)
