Face Detection, Emotion Recognition, and Age, Gender and Race Prediction App
==============================

This Python application leverages the power of DeepFace, a deep learning library, to perform multiple tasks related to facial analysis. With this app, you can upload an image, and it will:

* Detect Faces: Automatically identify and locate faces within the image.
* Emotion Recognition: Determine the dominant emotion expressed by the detected face(s).
* Age Prediction: Estimate the age of the person(s) in the image.
* Gender Identification: Recognize the gender of the person(s) in the image.
* Race Detection: Identify the dominant racial attributes of the person(s) in the image.

Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment.
    ├── data               <- Images that represent emotions.
    │
    ├── notebooks          <- Jupyter notebooks.
    │
    └── src                <- Source code for use in this project.
        ├── __init__.py    <- Makes src a Python module
        │
        └── app.py         <- Integrates DeepFace and creates a Streamlit app for face detection, emotion recognition, and age, gender and age prediction.


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
