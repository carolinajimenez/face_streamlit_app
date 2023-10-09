Face Detection, Emotion Recognition, and Age, Gender and Age Prediction App
==============================

A short description of the project.

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
