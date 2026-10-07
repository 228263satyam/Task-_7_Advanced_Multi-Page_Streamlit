import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(
    page_title="Reports",
    page_icon="📋",
    layout="wide"
)

st.title("📋 Project Reports")

st.write(
    "Generate and download a summary of the deep learning project."
)

# -------------------------
# PROJECT INFORMATION
# -------------------------

report = f"""
CIFAR-10 ADVANCED DEEP LEARNING APPLICATION
=============================================

Generated: {datetime.now().strftime("%d-%m-%Y %H:%M:%S")}

PROJECT OBJECTIVE
-----------------
Develop a deep learning image classification application
using the CIFAR-10 dataset and deploy the solution through
a multi-page Streamlit interface.

DATASET
-------
Dataset: CIFAR-10
Total Images: 60,000
Training Images: 50,000
Testing Images: 10,000
Number of Classes: 10
Image Size: 32 x 32 pixels
Channels: RGB

CLASSES
-------
Airplane
Automobile
Bird
Cat
Deer
Dog
Frog
Horse
Ship
Truck

APPLICATION FEATURES
--------------------
1. Home page
2. Interactive dashboard
3. Image prediction
4. Model performance analysis
5. Dataset explorer
6. Project reports
7. About page

TECHNOLOGIES
------------
Python
TensorFlow
Keras
Streamlit
NumPy
Pandas
Plotly
Matplotlib
Scikit-learn

CONCLUSION
----------
The project demonstrates how a trained deep learning model
can be integrated into a professional multi-page Streamlit
application with interactive dashboards, image prediction,
dataset exploration and model performance visualization.
"""

st.text_area(
    "Report Preview",
    report,
    height=500
)

st.download_button(
    label="📥 Download Project Report",
    data=report,
    file_name="CIFAR10_Project_Report.txt",
    mime="text/plain"
)

# -------------------------
# METRICS TABLE
# -------------------------

st.markdown("---")

st.subheader("📊 Project Summary")

df = pd.DataFrame({
    "Component": [
        "Dataset",
        "Images",
        "Classes",
        "Image Size",
        "Framework",
        "Interface"
    ],
    "Details": [
        "CIFAR-10",
        "60,000",
        "10",
        "32 × 32 × 3",
        "TensorFlow / Keras",
        "Streamlit"
    ]
})

st.dataframe(
    df,
    use_container_width=True,
    hide_index=True
)