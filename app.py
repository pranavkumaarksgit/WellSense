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
    st.warning("Moderate change detected in routine")

st.divider()

# Explanation
st.info(
    "This indicator is based on changes in daily routines such as "
    "sleep and activity patterns. It is for awareness only."
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


