import streamlit as st
import pandas as pd
import requests

# Backend configuration
BACKEND_URL = "https://YOUR-BACKEND-URL"
USER_ID = "demo_user"


# Page setup
st.set_page_config(page_title="WellSense", layout="wide")

# Header
st.title("🧠 WellSense")
st.caption("A non-clinical well-being awareness tool")
st.info("WellSense helps you reflect on routine changes over time.")


st.divider()

# Layout
left, right = st.columns([2, 1])

with left:
    st.subheader("📊 Behaviour Trends")

    try:
        response = requests.get(
            f"{BACKEND_URL}/risk_score/{USER_ID}",
            timeout=5
        )
        api_data = response.json()
    except Exception as e:
        api_data = {
            "risk_level": "Unknown",
            "confidence": "N/A",
            "explanation": "Backend not reachable"
        }

    st.subheader("📊 Behaviour Trends")

    trend_data = pd.DataFrame({
        "Day": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
        "Routine Consistency Score": [82, 80, 78, 65, 60, 58, 62]
    })

    st.line_chart(trend_data.set_index("Day"))



with right:
    st.subheader("🚦 Well-Being Indicator")

    risk_level = api_data["risk_level"]
    confidence = api_data.get("confidence", "N/A")


    risk_level = api_data["risk_level"]
    confidence = api_data.get("confidence", "N/A")

    if risk_level == "Low":
        st.success("Low change from your usual routine")
    elif risk_level == "Moderate":
        st.warning("Moderate change from your usual routine")
    else:
        st.error("Higher change from your usual routine")

    st.caption(f"Confidence level: {confidence}")


st.subheader("🧠 Why am I seeing this?")

st.write(
    "Over the past week, your routine consistency has shown more variation "
    "than usual. This comparison is made against your own recent patterns, "
    "not against other users."
)



st.divider()

# Explanation
st.info(
    "The indicator reflects how recent routine patterns compare to your "
    "personal baseline. Temporary changes may be caused by travel, workload, "
    "or schedule shifts. This insight is awareness-focused and non-clinical."
)


# User controls
st.subheader("🔐 Your Controls")

st.checkbox("I understand this is a non-clinical tool")

if st.button("⏸ Pause Monitoring"):
    st.warning("Monitoring paused.")

if st.button("🗑 Delete My Data"):
    st.error("Your data has been removed.")

st.markdown("---")
st.caption(
    "⚠️ This tool does not provide medical advice, diagnosis, or treatment."
)













