import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Interactive Dashboard")

st.markdown(
    "### CIFAR-10 Dataset & Model Analytics"
)

# -------------------------
# KPI CARDS
# -------------------------

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Total Images",
        "60,000"
    )

with col2:
    st.metric(
        "Training Images",
        "50,000"
    )

with col3:
    st.metric(
        "Testing Images",
        "10,000"
    )

with col4:
    st.metric(
        "Classes",
        "10"
    )

st.markdown("---")

# -------------------------
# DATA
# -------------------------

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

images = [
    6000,
    6000,
    6000,
    6000,
    6000,
    6000,
    6000,
    6000,
    6000,
    6000
]

df = pd.DataFrame({
    "Class": classes,
    "Images": images
})

# -------------------------
# CHART 1
# -------------------------

st.subheader("📦 Class Distribution")

fig = px.bar(
    df,
    x="Class",
    y="Images",
    text="Images",
    title="CIFAR-10 Class Distribution"
)

fig.update_layout(
    xaxis_title="Class",
    yaxis_title="Number of Images"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# -------------------------
# CHART 2
# -------------------------

col1, col2 = st.columns(2)

with col1:

    fig_pie = px.pie(
        df,
        values="Images",
        names="Class",
        title="Dataset Composition"
    )

    st.plotly_chart(
        fig_pie,
        use_container_width=True
    )

with col2:

    fig_bar = px.bar(
        df.sort_values("Images"),
        x="Images",
        y="Class",
        orientation="h",
        title="Images per Category"
    )

    st.plotly_chart(
        fig_bar,
        use_container_width=True
    )

# -------------------------
# MODEL METRICS
# -------------------------

st.markdown("---")

st.subheader("🧠 Model Summary")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Accuracy", "—")

with col2:
    st.metric("Precision", "—")

with col3:
    st.metric("Recall", "—")

with col4:
    st.metric("F1 Score", "—")

st.info(
    "Replace the metric values above with the actual results "
    "from your Task 6 model."
)