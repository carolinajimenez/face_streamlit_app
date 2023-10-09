"""
Face Detection, Emotion Recognition, and Age, Gender and Age Prediction App
DeepFace

https://github.com/serengil/deepface/tree/master
"""

import numpy as np
import cv2
from deepface import DeepFace
import streamlit as st


class FaceApp:
    """
    Face APP
    """

    def read_image(self, uploaded_file):
        """
        Read the image
        """
        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        image = cv2.imdecode(file_bytes, 1)
        return image

    def detect_faces(self, image):
        """
        Detect faces
        """
        try:
            faces = DeepFace.extract_faces(image)
            return faces
        except Exception:
            return None

    def detect_emotion_and_age(self, faces, image):
        """
        Detect emotion and age
        """

        data = {}
        # If no faces are detected
        if faces is None or len(faces) == 0:
            st.write("No faces detected in the image.")
            return data
        # If faces are detected
        else:
            # Specify age, gender, emotion, race
            analysis = DeepFace.analyze(image,
                                        actions = ["age", "gender", "emotion", "race"])[0]
            print("analysis", analysis)

            data["image"] = image
            data["emotions"] = analysis["dominant_emotion"]
            data["age"] = analysis["age"]
            data["gender"] = analysis["dominant_gender"]
            data["race"] = analysis["dominant_race"]
        return data

    def clasify_face(self, uploaded_file):
        image = self.read_image(uploaded_file)
        faces = self.detect_faces(image)
        results = self.detect_emotion_and_age(faces, image)
        return results, image


if __name__ == "__main__":
    # Set up the app
    st.title("Face Detection, Emotion Recognition, and Age, Gender and Age Prediction App")
    st.write("")

    faceapp = FaceApp()

    st.write("Upload an image and the app will detect faces, specify emotions, and predict age, gender and age.")
    # Upload the image
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    # If the user uploaded an image
    if uploaded_file is not None:
        result, image = faceapp.clasify_face(uploaded_file)
        if result:
            # Display the results
            img_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            st.image(img_rgb, caption="Detected face")
            st.write("Emotion:", result['emotions'])
            st.write("Age:", result['age'])
            st.write("Gender:", result['gender'])
            st.write("Race:", result['race'])