# 🚀 AI HR Analytics Platform

## ✨ Overview
This project is a vibrant and interactive HR analytics web app built with Streamlit. It helps organizations understand employee attrition, predict potential turnover, explore insights through engaging visual dashboards, and get AI-powered guidance using a large language model.

## 🌟 What This Project Does
The platform gives HR teams a smart, user-friendly experience to:
- 📊 view key employee attrition metrics
- 📈 visualize employee trends and patterns
- 🤖 predict attrition for individual employees
- 📁 analyze bulk employee datasets in CSV format
- 💬 ask an AI assistant for HR-related insights

## 🧠 Models Used
- 🎯 Attrition Prediction Model: a pre-trained scikit-learn classification model loaded from model.pkl
- 🧩 Feature Alignment File: model_columns.pkl ensures incoming data matches the model’s expected input structure
- 🤖 AI Assistant: a Groq-powered language model for natural-language HR insights

## 🛠️ Tech Stack
- Python
- Streamlit
- Pandas
- NumPy
- scikit-learn
- Plotly
- Streamlit Option Menu
- Groq SDK
- python-dotenv

## 🔥 Key Features
- 📊 HR dashboard with attrition overview and visual charts
- 🎯 Employee attrition prediction for single records
- 📦 Bulk CSV prediction with downloadable results
- 📈 Advanced analytics visuals for employee trends
- 🤖 AI assistant for conversational HR analysis

## 📁 Project Structure
- app.py: main Streamlit application
- employees.csv: sample employee dataset
- hr_attrition_same_schema_dataset_updated.csv: additional dataset for analysis
- model.pkl: trained prediction model
- model_columns.pkl: expected features for model input
- requirements.txt: Python dependencies

## ⚙️ Installation
1. Create and activate a virtual environment
2. Install the dependencies:
   pip install -r requirements.txt
3. Set your Groq API key in a .env file or Streamlit secrets

## ▶️ Run the Application
Run the following command:

streamlit run app.py

## 🔐 Environment Variable
Create a .env file with:

GROQ_API_KEY=your_api_key_here
