# 🤖 CIFAR-10 AI Analytics Platform
## Advanced Multi-Page Streamlit Application – Task 7

A professional multi-page Streamlit application for **CIFAR-10 image classification**, developed as part of **Task 7: Advanced Multi-Page Streamlit Application**.

The application integrates a trained deep learning model with an interactive dashboard, image prediction, model performance analysis, dataset exploration, visualizations, and downloadable project reports.

---

## 📌 Project Overview

Deep learning models are often developed and evaluated in notebooks. This project extends the trained CIFAR-10 image classification model into a complete interactive web application using **Streamlit**.

The application provides a user-friendly interface where users can:

- Explore the project
- View CIFAR-10 dataset statistics
- Upload images for classification
- View prediction confidence
- See Top-3 predictions
- Analyze model performance
- View training and validation accuracy
- Explore the confusion matrix
- Explore dataset information
- Generate and download project reports

---

## 🎯 Task Objective

The objective of Task 7 is:

> **To develop a professional deep learning application with multiple pages and interactive visualizations.**

### Task Requirements

- ✅ Create a multi-page Streamlit architecture
- ✅ Add dashboards and visualizations
- ✅ Display model performance metrics
- ✅ Integrate charts and reports
- ✅ Improve navigation and user experience

---

## 📊 Dataset

The project uses the **CIFAR-10 image classification dataset**.

### Dataset Information

| Property | Details |
|---|---|
| Dataset | CIFAR-10 |
| Total Images | 60,000 |
| Training Images | 50,000 |
| Testing Images | 10,000 |
| Number of Classes | 10 |
| Image Size | 32 × 32 pixels |
| Channels | RGB |
| Problem Type | Multi-class Image Classification |

### CIFAR-10 Classes

1. ✈️ Airplane
2. 🚗 Automobile
3. 🐦 Bird
4. 🐱 Cat
5. 🦌 Deer
6. 🐕 Dog
7. 🐸 Frog
8. 🐎 Horse
9. 🚢 Ship
10. 🚚 Truck

---

# 🧠 Model

The application uses a trained **Convolutional Neural Network (CNN)** model developed for CIFAR-10 image classification.

The trained model is integrated into the Streamlit application and used as the prediction engine.

### Prediction Workflow

```text
User Uploads Image
        ↓
Image Converted to RGB
        ↓
Image Resized to 32 × 32
        ↓
Pixel Normalization
        ↓
CNN Model
        ↓
Class Probabilities
        ↓
Predicted Class
        ↓
Confidence Score
        ↓
Top-3 Predictions
