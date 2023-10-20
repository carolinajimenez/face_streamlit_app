Emotion Recognition, and Age, Gender and Race Prediction App
==============================

This Python application leverages the power of DeepFace, a deep learning library, to perform multiple tasks related to facial analysis. With this app, you can upload an image, and it will:

* Detect Faces: Automatically identify and locate faces within the image.
* Emotion Recognition: Determine the dominant emotion expressed by the detected face(s).
* Age Prediction: Estimate the age of the person(s) in the image.
* Gender Identification: Recognize the gender of the person(s) in the image.
* Race Detection: Identify the dominant racial attributes of the person(s) in the image.

Project Organization
------------

      faceapp
      ├── LICENSE
      ├── README.md                 <- The top-level README for developers using this project.
      ├── data                      <- Images that represent emotions.
      │   ├── angry.jpg
      │   ├── disgust.jpg
      │   ├── fear.jpg
      │   ├── happy.jpg
      │   ├── neutral.jpg
      │   ├── sad.jpg
      │   └── surprise.jpg
      ├── notebooks                 <- Jupyter notebooks.
      │   └── deepface.ipynb
      ├── requirements.txt          <- The requirements file for reproducing the analysis environment.
      └── src                       <- Source code for use in this project.
         ├── __init__.py
         └── app.py                 <- Integrates DeepFace and creates a Streamlit app for face detection, emotion recognition, and age, gender and race prediction.

Usage
------------

1. Clone the repository:
```
git clone https://github.com/carolinajimenez/faceapp
cd recsys
```

2. Install the required packages:
```
pip install -r requirements.txt
```

3. Run the Streamlit app:
```
streamlit run src/app.py
```

--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
