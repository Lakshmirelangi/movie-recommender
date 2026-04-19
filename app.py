import streamlit as st
import pandas as pd
from model import get_recommendations

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(page_title="🎬 Movie Recommender", layout="wide")

# -----------------------------
# Custom Styling
# -----------------------------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(to right, #141e30, #243b55);
    color: white;
}
.title {
    text-align: center;
    font-size: 40px;
    font-weight: bold;
}
.subtitle {
    text-align: center;
    font-size: 18px;
    margin-bottom: 20px;
}
.card {
    background-color: #1f2937;
    padding: 15px;
    border-radius: 10px;
    margin: 10px;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# Title Section
# -----------------------------
st.markdown('<div class="title">🎬 Movie Recommendation System</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">KNN + Cosine Similarity</div>', unsafe_allow_html=True)

# -----------------------------
# Load Data
# -----------------------------
df = pd.read_csv("movies.csv")
user_ids = df["userId"].unique()

# -----------------------------
# Layout (Columns)
# -----------------------------
col1, col2 = st.columns(2)

with col1:
    selected_user = st.selectbox("👤 Select User", user_ids)

with col2:
    st.write("")
    st.write("")
    get_button = st.button("🚀 Get Recommendations")

# -----------------------------
# Output Section
# -----------------------------
if get_button:
    recommendations = get_recommendations(selected_user)

    st.markdown("## 🎯 Recommended Movies")

    if recommendations:
        for movie in recommendations:
            st.markdown(f'<div class="card">✅ {movie}</div>', unsafe_allow_html=True)
    else:
        st.warning("No recommendations found")