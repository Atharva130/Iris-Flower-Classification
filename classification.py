import streamlit as st
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

# Apply custom CSS for styling
st.markdown(
    """
    <style>
    /* Sidebar Styling */
    [data-testid="stSidebar"] {
        background-color: #456 !important; /* Light Orange Sidebar */
    }
    /* Title Styling */
    .title {
        font-size: 36px;
        font-weight: bold;
        color: #1565C0;
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

@st.cache_data
def load_data():
    iris = load_iris()
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
    df['species'] = iris.target
    return df, iris.target_names

df, target_name = load_data()
model = RandomForestClassifier()
model.fit(df.iloc[:, :-1], df['species'])

# Title
st.markdown('<h1 class="title">🌸 Iris Flower Classification 🌸</h1>', unsafe_allow_html=True)

st.sidebar.title("🔧 Input Features")

# Sidebar sliders
sepal_length = st.sidebar.slider("Sepal length", float(df.iloc[:, 0].min()), float(df.iloc[:, 0].max()))
sepal_width = st.sidebar.slider("Sepal width", float(df.iloc[:, 1].min()), float(df.iloc[:, 1].max()))
petal_length = st.sidebar.slider("Petal length", float(df.iloc[:, 2].min()), float(df.iloc[:, 2].max()))
petal_width = st.sidebar.slider("Petal width", float(df.iloc[:, 3].min()), float(df.iloc[:, 3].max()))

# Convert input into DataFrame to avoid feature name warning
input_data = pd.DataFrame([[sepal_length, sepal_width, petal_length, petal_width]], columns=df.columns[:-1])
prediction = model.predict(input_data)
predicted_species = target_name[prediction[0]]

st.subheader("📌 Prediction")
st.write(f"🌿 **The predicted species is:** :red[{predicted_species}]")

