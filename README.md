# 🌸 Iris Species Prediction & Visualization App

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://ntiirisdatasetforapp-dpgeuqqvqnsrdi9dfwfdov.streamlit.app)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-orange.svg)](https://scikit-learn.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=Streamlit&logoColor=white)](https://streamlit.io)

An interactive, user-friendly web application built with **Streamlit** and **Scikit-Learn** that allows users to explore the classic **Iris Dataset**, visualize feature distributions across multiple chart types, and perform real-time botanical species predictions using a trained **Decision Tree Classifier**.

---

## 🚀 Live Demo

Experience the application live on Streamlit Community Cloud:

🔗 **[Launch the Iris Prediction App](https://ntiirisdatasetforapp-kmnbem7wpe8v4ueu4mny47.streamlit.app)**

---

## ✨ Key Features

* **📊 Dataset Exploration:** View the full raw Iris dataframe and instantly generate comprehensive statistical summaries (mean, standard deviation, quartiles, etc.) with a single click.
* **📈 Multi-Modal Visualizations:** Seamlessly switch between three dynamic visual representations using Streamlit tabs:
  * **Line Chart:** Compare trends between sepal length and sepal width.
  * **Scatter Chart:** Analyze feature correlations and clustering behavior across samples.
  * **Bar Chart:** View comparative feature distributions.
* **🤖 Real-Time Species Prediction:** Adjust custom sliders for petal and sepal measurements (in centimeters) to get instant predictions (`setosa`, `versicolor`, or `virginica`) powered by a machine learning model.
* **🎨 Responsive & Clean UI:** Optimized for both Dark and Light modes with custom status alerts and intuitive layout design.

---

## 🛠️ Tech Stack & Libraries

* **Frontend & UI:** [Streamlit](https://streamlit.io/)
* **Machine Learning:** [Scikit-Learn](https://scikit-learn.org/) (`DecisionTreeClassifier`)
* **Data Manipulation:** [Pandas](https://pandas.pydata.org/), [NumPy](https://numpy.org/)

---

## 📂 Project Structure

To ensure modularity and clean separation of concerns between frontend UI and backend machine learning logic, the project is structured as follows:

```text
iris_project/
│
├── app.py               # Main Streamlit application & UI components
├── requirements.txt     # Project dependencies for deployment
└── my_module/           # Backend machine learning package
    ├── __init__.py      # Package initialization
    └── model.py         # Decision Tree model training & prediction logic
