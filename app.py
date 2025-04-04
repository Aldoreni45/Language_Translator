import streamlit as st
import google.generativeai as genai
import pandas as pd
import plotly.express as px
from datetime import datetime

# Initialize Gemini Model with your API Key
genai.configure(api_key="AIzaSyAex9EGrl5TlhLZcWY1yNQLuG3Vqt2TBys")  # Replace with your actual API key
model = genai.GenerativeModel('gemini-1.5-flash')

# Set page configuration
st.set_page_config(
    page_title="EcoSynth AI - Energy Transition Platform",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for enhanced UI
st.markdown("""
<style>
/* Page background and layout */
body {
    background-color: #0E1117;
}
[data-testid="stAppViewContainer"] {
    background: linear-gradient(to bottom right, #1a1c1e, #2e3b4e);
    color: white;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background-color: #1c1f26;
}
.sidebar .sidebar-content {
    color: white;
}

/* Heading style fix */
h1, h2, h3, h4 {
    color: #00d4ff !important;
    font-weight: 700;
}

/* Description text */
.description {
    color: #cccccc;
    font-size: 16px;
    margin-bottom: 10px;
}

/* Chat text area and button */
textarea {
    background-color: #1e1f22;
    color: white;
    font-size: 16px;
}
button {
    background-color: #000000;
    color: white;
    border-radius: 8px;
    padding: 10px 20px;
}
</style>
""", unsafe_allow_html=True)


# Title Header
st.markdown('<div class="header">EcoSynth AI 🌿 - Energy Transition Intelligence</div>', unsafe_allow_html=True)

# Sidebar Navigation
with st.sidebar:
    st.header("🔍 Navigation")
    page = st.selectbox("Go to", ["Dashboard", "Chat with EcoSynth AI", "About"])

# Dashboard Page
if page == "Dashboard":
    st.subheader("📊 Energy Usage Dashboard")
    
    # Dummy Data for Visualization
    data = {
        'Year': [2018, 2019, 2020, 2021, 2022, 2023],
        'Renewable': [18, 22, 28, 34, 40, 47],
        'Non-Renewable': [82, 78, 72, 66, 60, 53]
    }
    df = pd.DataFrame(data)
    
    fig = px.line(df, x='Year', y=['Renewable', 'Non-Renewable'],
                  labels={'value': 'Energy (%)', 'variable': 'Type'},
                  title='Renewable vs Non-Renewable Energy Usage Over Years')
    
    with st.container():
        st.plotly_chart(fig, use_container_width=True)

    with st.container():
        st.markdown("### 🔍 Insights")
        st.markdown("""
        - *Renewable energy* has been steadily increasing.
        - There is a clear transition trend away from non-renewables.
        - Projected continuation based on policy initiatives and tech advancements.
        """)

# Chatbot Page
elif page == "Chat with EcoSynth AI":
    st.subheader("🤖 Ask EcoSynth AI about the Energy Transition")

    # Input from user
    user_query = st.text_area("Ask a question about renewable energy, sustainability, or transition policies:")
    
    if st.button("Get Answer"):
        if user_query.strip() != "":
            with st.spinner("Thinking..."):
                response = model.generate_content(user_query)
                st.markdown("### ✅ Response:")
                st.write(response.text)
        else:
            st.warning("Please enter a question before clicking the button.")

# About Page
elif page == "About":
    st.subheader("ℹ About EcoSynth AI")
    st.markdown("""
    *EcoSynth AI* is a smart assistant for understanding and analyzing energy transition trends.  
    This platform combines *data visualization, **AI-powered insights, and **user interaction* to drive awareness and policy discussion.
    
    *Features:*
    - Interactive dashboards 📊  
    - Gemini-powered smart Q&A 🤖  
    - Easy-to-use UI 🌿  
    """)

    st.markdown("Created by [Your Name or Team] 💡")