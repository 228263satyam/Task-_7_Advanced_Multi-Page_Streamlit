import streamlit as st

st.set_page_config(
    page_title="CIFAR-10 AI Analytics",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------- CUSTOM CSS ----------
st.markdown("""
<style>

.main {
    background-color: #f5f7fb;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}

.hero {
    padding: 35px;
    border-radius: 20px;
    background: linear-gradient(135deg, #667eea, #764ba2);
    color: white;
    margin-bottom: 30px;
}

.hero h1 {
    font-size: 42px;
    margin-bottom: 10px;
}

.hero p {
    font-size: 18px;
}

.metric-card {
    padding: 20px;
    border-radius: 15px;
    background: white;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.08);
    text-align: center;
}

.metric-value {
    font-size: 30px;
    font-weight: bold;
}

.metric-label {
    color: #666;
}

</style>
""", unsafe_allow_html=True)

# ---------- SIDEBAR ----------
st.sidebar.title("🤖 AI Analytics")
st.sidebar.markdown("---")

st.sidebar.info(
    """
    **Task 7**

    Advanced Multi-Page Streamlit Application

    Dataset: CIFAR-10

    Model: Deep Learning CNN
    """
)

# ---------- HOME ----------
st.markdown("""
<div class="hero">

<h1>🤖 CIFAR-10 AI Analytics Platform</h1>

<p>
Advanced Multi-Page Deep Learning Application
</p>

<p>
Explore predictions, model performance, dataset analytics
and interactive visualizations.
</p>

</div>
""", unsafe_allow_html=True)

# ---------- KPI ----------
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Dataset Images", "60,000")

with col2:
    st.metric("Classes", "10")

with col3:
    st.metric("Image Size", "32 × 32")

with col4:
    st.metric("Problem Type", "Classification")

st.markdown("---")

st.header("📌 Project Overview")

st.write("""
This application demonstrates an advanced multi-page Streamlit
interface for a deep learning image classification project.

The application provides:

- Interactive dashboard
- Image prediction
- Model performance analysis
- Confusion matrix
- Classification metrics
- Dataset exploration
- Interactive visualizations
- Prediction reports
""")

st.header("🚀 Application Navigation")

col1, col2, col3 = st.columns(3)

with col1:
    st.info("🏠 **Home**\n\nProject overview and key information.")

with col2:
    st.info("📊 **Dashboard**\n\nInteractive project statistics.")

with col3:
    st.info("🔍 **Prediction**\n\nUpload an image and classify it.")

col1, col2, col3 = st.columns(3)

with col1:
    st.info("📈 **Performance**\n\nAnalyze model metrics.")

with col2:
    st.info("🖼️ **Dataset Explorer**\n\nExplore CIFAR-10 images.")

with col3:
    st.info("📋 **Reports**\n\nGenerate project summaries.")

st.success(
    "Use the pages from the sidebar to explore the complete application."
)