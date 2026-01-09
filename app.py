import streamlit as st
import pandas as pd

# Page setup
st.set_page_config(page_title="WellSense", layout="wide")

# Header
st.title("🧠 WellSense")
st.caption("A non-clinical well-being awareness tool")

st.divider()

# Layout
left, right = st.columns([2, 1])

with left:
    st.subheader("📊 Behaviour Trends")

    # Sample behavioural data
    data = pd.DataFrame({
        "Day": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
        "Routine Consistency Score": [82, 80, 78, 65, 60, 58, 62]
    })

    st.line_chart(data.set_index("Day"))


with right:
    st.subheader("🚦 Well-Being Indicator")

    # Simple logic based on last routine score
    latest_score = data["Routine Consistency Score"].iloc[-1]

    if latest_score >= 75:
        st.success("Low change from your usual routine")
        confidence = "High"
    elif latest_score >= 60:
        st.warning("Moderate change from your usual routine")
        confidence = "Medium"
    else:
        st.error("Higher change from your usual routine")
        confidence = "Low"

    st.caption(f"Confidence level: {confidence}")


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



