import streamlit as st

st.set_page_config(
    page_title="About",
    page_icon="ℹ️",
    layout="wide"
)

st.title("ℹ️ About the Project")

st.markdown("""
## Advanced Multi-Page Streamlit Application

This project was developed as part of **Task 7:
Advanced Multi-Page Streamlit Application**.

### 🎯 Objective

The objective is to transform a deep learning image
classification model into an interactive and professional
web application.

### 🧠 Machine Learning

The application uses a trained deep learning model for
CIFAR-10 image classification.

### 🛠 Technology Stack

| Technology | Purpose |
|---|---|
| Python | Programming |
| TensorFlow | Deep Learning |
| Keras | Model Development |
| Streamlit | Web Application |
| Plotly | Interactive Visualization |
| Pandas | Data Analysis |
| NumPy | Numerical Processing |
| Matplotlib | Visualization |
| Scikit-learn | Model Evaluation |

### 📌 Application Modules

- Home
- Dashboard
- Image Prediction
- Model Performance
- Dataset Explorer
- Reports
- About

### 👨‍💻 Developer

**Satyam Yadav**

M.Sc. Data Science & Big Data Analyst

### 📚 Academic Task

**Task 7 – Advanced Multi-Page Streamlit Application**
""")

st.success(
    "Thank you for exploring the application! 🚀"
)