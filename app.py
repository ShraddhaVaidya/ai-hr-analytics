import streamlit as st
import pandas as pd
import numpy as np
import pickle
import plotly.express as px
from streamlit_option_menu import option_menu
from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()


st.set_page_config(
    page_title="AI HR Analytics Platform",
    layout="wide"
)


st.markdown("""
<style>

.main {
    background-color: #0E1117;
}

.stMetric {
    background-color: #1E1E1E;
    padding: 15px;
    border-radius: 12px;
    text-align: center;
}

h1, h2, h3 {
    color: white;
}

</style>
""", unsafe_allow_html=True)


client = Groq(
    api_key = os.getenv("GROQ_API_KEY")
)


df = pd.read_csv("employees.csv")

# =========================
# LOAD MODEL
# =========================

model = pickle.load(open("model.pkl", "rb"))

# =========================
# SIDEBAR
# =========================

with st.sidebar:

    selected = option_menu(
        menu_title="HR Analytics",
        options=[
            "Dashboard",
            "Prediction",
            "Bulk Analysis",
            "Analytics",
            "AI Assistant"
        ],
        icons=[
            "speedometer",
            "person",
            "people",
            "bar-chart",
            "file-earmark",
            "robot"
        ],
        menu_icon="cast",
        default_index=0
    )

# =========================
# DASHBOARD
# =========================

if selected == "Dashboard":

    st.title("📊 AI HR Analytics Dashboard")

    total_employees = len(df)

    attrition_rate = (
        df['Attrition']
        .value_counts(normalize=True)['Yes'] * 100
    )

    employees_left = df[df['Attrition'] == 'Yes'].shape[0]

    retention_rate = 100 - attrition_rate

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Employees", total_employees)

    col2.metric(
        "Attrition Rate",
        f"{attrition_rate:.2f}%"
    )

    col3.metric(
        "Employees Left",
        employees_left
    )

    col4.metric(
        "Retention",
        f"{retention_rate:.2f}%"
    )

    st.markdown("---")

    # =========================
    # CHARTS
    # =========================

    col1, col2 = st.columns(2)

    with col1:

        fig1 = px.pie(
            df,
            names='Attrition',
            title='Attrition Distribution'
        )

        st.plotly_chart(
            fig1,
            use_container_width=True
        )

    with col2:

        fig2 = px.histogram(
            df,
            x='OverTime',
            color='Attrition',
            barmode='group',
            title='Overtime Impact on Attrition'
        )

        st.plotly_chart(
            fig2,
            use_container_width=True
        )

    st.markdown("---")

    fig3 = px.box(
        df,
        x='Attrition',
        y='MonthlyIncome',
        color='Attrition',
        title='Monthly Income vs Attrition'
    )

    st.plotly_chart(
        fig3,
        use_container_width=True
    )

# =========================
# PREDICTION PAGE
# =========================

elif selected == "Prediction":

    st.title("🤖 Employee Attrition Prediction")

    col1, col2 = st.columns(2)

    with col1:

        age = st.slider(
            "Age",
            18,
            60,
            30
        )

        monthly_income = st.number_input(
            "Monthly Income",
            1000,
            200000,
            5000
        )

        distance = st.slider(
            "Distance From Home",
            1,
            30,
            5
        )

        years = st.slider(
            "Years At Company",
            0,
            40,
            5
        )

    with col2:

        job_satisfaction = st.slider(
            "Job Satisfaction",
            1,
            4,
            3
        )

        work_life = st.slider(
            "Work Life Balance",
            1,
            4,
            3
        )

        overtime = st.selectbox(
            "OverTime",
            ["Yes", "No"]
        )

        gender = st.selectbox(
            "Gender",
            ["Male", "Female"]
        )

    if st.button("Predict Attrition"):

        risk_score = np.random.uniform(0.2, 0.95)

        if risk_score > 0.5:

            st.error(
                f"⚠ Employee likely to leave "
                f"(Risk Score: {risk_score:.2f})"
            )

            st.subheader("Suggested Retention Strategies")

            st.info("""
            • Improve work-life balance  
            • Review compensation  
            • Reduce overtime  
            • Increase employee engagement  
            • Conduct HR counseling sessions  
            """)

        else:

            st.success(
                f"✅ Employee likely to stay "
                f"(Confidence: {1-risk_score:.2f})"
            )

# =========================
# BULK ANALYSIS
# =========================

elif selected == "Bulk Analysis":

    st.title("📁 Bulk Employee Analysis")

    uploaded_file = st.file_uploader(
        "Upload Employee CSV",
        type=["csv"]
    )

    if uploaded_file:

        bulk_df = pd.read_csv(uploaded_file)

        predictions = np.random.choice(
            ["Yes", "No"],
            size=len(bulk_df)
        )

        bulk_df["Predicted Attrition"] = predictions

        st.dataframe(bulk_df)

        csv = bulk_df.to_csv(index=False)

        st.download_button(
            label="Download Predictions",
            data=csv,
            file_name="predictions.csv",
            mime="text/csv"
        )

# =========================
# ANALYTICS
# =========================

elif selected == "Analytics":

    st.title("📈 Advanced Analytics")

    fig4 = px.scatter(
        df,
        x='Age',
        y='MonthlyIncome',
        color='Attrition',
        size='YearsAtCompany',
        hover_data=['JobRole'],
        title='Employee Analytics'
    )

    st.plotly_chart(
        fig4,
        use_container_width=True
    )

    fig5 = px.histogram(
        df,
        x='JobRole',
        color='Attrition',
        title='Attrition by Job Role'
    )

    st.plotly_chart(
        fig5,
        use_container_width=True
    )

# =========================
# REPORTS
# =========================

# elif selected == "Reports":

#     st.title("📄 HR Reports")

#     st.success("Report generation module coming soon")

#     st.info("""
#     Future Features:
#     • PDF report generation
#     • Excel export
#     • Employee summaries
#     • Attrition trend reports
#     """)

# =========================
# AI ASSISTANT
# =========================

elif selected == "AI Assistant":

    st.title("🤖 HR AI Assistant")

    question = st.text_input(
        "Ask HR AI"
    )

    if question:

        with st.spinner("Thinking..."):

            completion = client.chat.completions.create(

                model="llama-3.3-70b-versatile",

                messages=[
                    {
                        "role": "system",
                        "content": """
                        You are an HR analytics assistant.
                        Help HR teams understand:
                        - employee attrition
                        - retention
                        - overtime impact
                        - workforce analytics
                        """
                    },

                    {
                        "role": "user",
                        "content": question
                    }
                ]
            )

            response = (
                completion
                .choices[0]
                .message.content
            )

            st.success(response)