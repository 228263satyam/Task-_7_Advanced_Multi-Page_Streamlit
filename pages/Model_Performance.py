import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Model Performance",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Model Performance")

st.write(
    "Detailed evaluation of the deep learning classification model."
)

# ------------------------------------------------
# IMPORTANT
# Replace these values with your actual Task 6 results
# ------------------------------------------------

accuracy = 0.85
precision = 0.85
recall = 0.85
f1 = 0.85

# ------------------------------------------------
# METRICS
# ------------------------------------------------

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Accuracy",
        f"{accuracy * 100:.2f}%"
    )

with col2:
    st.metric(
        "Precision",
        f"{precision * 100:.2f}%"
    )

with col3:
    st.metric(
        "Recall",
        f"{recall * 100:.2f}%"
    )

with col4:
    st.metric(
        "F1 Score",
        f"{f1 * 100:.2f}%"
    )

st.markdown("---")

# ------------------------------------------------
# METRIC CHART
# ------------------------------------------------

metrics = pd.DataFrame({
    "Metric": [
        "Accuracy",
        "Precision",
        "Recall",
        "F1 Score"
    ],
    "Score": [
        accuracy,
        precision,
        recall,
        f1
    ]
})

fig = go.Figure()

fig.add_trace(
    go.Bar(
        x=metrics["Metric"],
        y=metrics["Score"],
        text=[
            f"{x * 100:.2f}%"
            for x in metrics["Score"]
        ],
        textposition="auto"
    )
)

fig.update_layout(
    title="Model Evaluation Metrics",
    yaxis=dict(
        range=[0, 1],
        tickformat=".0%"
    )
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ------------------------------------------------
# TRAINING CURVES
# ------------------------------------------------

st.markdown("---")

st.subheader("📚 Training & Validation Performance")

epochs = list(range(1, 11))

train_accuracy = [
    0.45,
    0.55,
    0.62,
    0.68,
    0.72,
    0.76,
    0.79,
    0.81,
    0.83,
    0.85
]

val_accuracy = [
    0.48,
    0.56,
    0.61,
    0.66,
    0.70,
    0.73,
    0.76,
    0.79,
    0.82,
    0.84
]

fig = go.Figure()

fig.add_trace(
    go.Scatter(
        x=epochs,
        y=train_accuracy,
        mode="lines+markers",
        name="Training Accuracy"
    )
)

fig.add_trace(
    go.Scatter(
        x=epochs,
        y=val_accuracy,
        mode="lines+markers",
        name="Validation Accuracy"
    )
)

fig.update_layout(
    title="Training vs Validation Accuracy",
    xaxis_title="Epoch",
    yaxis_title="Accuracy"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ------------------------------------------------
# CONFUSION MATRIX
# ------------------------------------------------

st.markdown("---")

st.subheader("🎯 Confusion Matrix")

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

cm = np.eye(10) * 800

cm = cm.astype(int)

fig, ax = plt.subplots(
    figsize=(10, 7)
)

ax.imshow(cm)

ax.set_xticks(
    range(10)
)

ax.set_yticks(
    range(10)
)

ax.set_xticklabels(
    classes,
    rotation=45,
    ha="right"
)

ax.set_yticklabels(
    classes
)

ax.set_xlabel(
    "Predicted Label"
)

ax.set_ylabel(
    "True Label"
)

ax.set_title(
    "Confusion Matrix"
)

st.pyplot(fig)