import streamlit as st
import numpy as np
from PIL import Image
import tensorflow as tf

st.set_page_config(
    page_title="Image Prediction",
    page_icon="🔍",
    layout="wide"
)

st.title("🔍 Image Classification")

st.write(
    "Upload an image and use the trained deep learning model "
    "to generate a prediction."
)

# -------------------------
# CLASSES
# -------------------------

classes = [
    "airplane",
    "automobile",
    "bird",
    "cat",
    "deer",
    "dog",
    "frog",
    "horse",
    "ship",
    "truck"
]

# -------------------------
# LOAD MODEL
# -------------------------

MODEL_PATH = "model/cifar10_model.keras"

@st.cache_resource
def load_model():

    try:
        model = tf.keras.models.load_model(MODEL_PATH)
        return model

    except Exception as e:

        return None


model = load_model()

if model is None:

    st.warning(
        "Model file not found. Please place your trained model at:"
    )

    st.code(
        "model/cifar10_model.keras"
    )

# -------------------------
# UPLOAD
# -------------------------

uploaded_file = st.file_uploader(
    "📤 Upload an image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file:

    image = Image.open(uploaded_file).convert("RGB")

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("Uploaded Image")

        st.image(
            image,
            use_column_width=True
        )

    with col2:

        st.subheader("Prediction")

        if model is not None:

            input_shape = model.input_shape
            if (
                isinstance(input_shape, list)
                or len(input_shape) != 4
                or input_shape[1] is None
                or input_shape[2] is None
                or input_shape[3] not in (1, 3)
            ):
                st.error(
                    "The model must accept fixed-size RGB or grayscale images."
                )
            else:
                image_height = input_shape[1]
                image_width = input_shape[2]
                channels = input_shape[3]
                model_image = image.convert("L") if channels == 1 else image
                model_image = model_image.resize((image_width, image_height))

                img_array = np.array(model_image, dtype="float32") / 255.0
                if channels == 1:
                    img_array = np.expand_dims(img_array, axis=-1)
                img_array = np.expand_dims(img_array, axis=0)

                prediction = model.predict(img_array, verbose=0)
                probabilities = prediction[0]

                if len(probabilities) != len(classes):
                    st.error(
                        "The model output does not match the configured class list."
                    )
                else:
                    predicted_index = np.argmax(probabilities)
                    predicted_class = classes[predicted_index]
                    confidence = probabilities[predicted_index] * 100

                    st.success(f"### {predicted_class.upper()}")
                    st.metric("Confidence", f"{confidence:.2f}%")
                    st.caption(
                        "Image automatically resized to "
                        f"{image_width} × {image_height} to match the model."
                    )

                    top_indices = np.argsort(probabilities)[-3:][::-1]
                    st.subheader("🏆 Top 3 Predictions")

                    for index in top_indices:
                        st.write(
                            f"**{classes[index]}** — "
                            f"{probabilities[index] * 100:.2f}%"
                        )
                        st.progress(float(probabilities[index]))

        else:

            st.error(
                "Model could not be loaded."
            )