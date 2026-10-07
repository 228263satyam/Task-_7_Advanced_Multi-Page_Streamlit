import streamlit as st

st.set_page_config(
    page_title="Home - CIFAR-10",
    page_icon="🏠",
    layout="wide"
)

st.title("🏠 Project Home")

st.markdown("""
## Advanced CIFAR-10 Image Classification

This application provides a complete interactive interface
for exploring a deep learning image classification model.
""")

st.markdown("---")

col1, col2 = st.columns(2)

with col1:

    st.subheader("🎯 Objective")

    st.write("""
    The objective of this project is to develop a deep learning
    application capable of classifying images into one of the
    ten CIFAR-10 categories.
    """)

    st.subheader("🧠 Model")

    st.write("""
    A Convolutional Neural Network (CNN) based deep learning model
    is used for image classification.
    """)

with col2:

    st.subheader("📊 Dataset")

    st.write("""
    CIFAR-10 contains 60,000 colour images distributed across
    10 different object categories.

    Each image has a resolution of 32 × 32 pixels.
    """)

    st.subheader("⚙️ Technologies")

    st.write("""
    - Python
    - TensorFlow / Keras
    - Streamlit
    - NumPy
    - Pandas
    - Plotly
    - Matplotlib
    - Scikit-learn
    """)

st.markdown("---")

st.subheader("📌 CIFAR-10 Classes")

classes = [
    "Airplane",
    "Automobile",
    "Bird",
    "Cat",
    "Deer",
    "Dog",
    "Frog",
    "Horse",
    "Ship",
    "Truck"
]

cols = st.columns(5)

for i, name in enumerate(classes):

    with cols[i % 5]:

        st.success(f"**{i}**  {name}")