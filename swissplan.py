import streamlit as st
import pandas as pd

# ตั้งค่าหน้าเว็บ
st.set_page_config(page_title="แผนเที่ยวสวิต", layout="wide")
st.title("🇨🇭 แผนเที่ยวสวิตเซอร์แลนด์ของพี่อุ๊ก & บิว 🤍")

df = pd.read_excel("Plan/Swiss_plan_app.xlsx")
df.columns = df.columns.str.strip()  # Remove extra spaces
st.write(df.columns.tolist())  # Show column names for debugging

# Use HTML/CSS to overlay the character on the rail track
st.markdown(
    """
    <div style="position: relative; width: 600px; height: 150px;">
        <img src="images/rail_track.png" style="width: 100%; position: absolute; left: 0; top: 50px; z-index: 1;">
        <img src="images/ouk_bew_chibi.png" style="width: 100px; position: absolute; left: 250px; top: 0; z-index: 2;">
    </div>
    """,
    unsafe_allow_html=True
)

# Display your travel plan as before
for idx, row in df.iterrows():
    st.markdown(f"### {row['Location']} to {row['Destination']}")
    st.write(f"**Time:** {row['Time']}")
    st.write(f"**Activity:** {row['Activity']}")
    st.markdown("---")
