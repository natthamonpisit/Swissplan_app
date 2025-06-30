import streamlit as st
import pandas as pd

# ตั้งค่าหน้าเว็บ
st.set_page_config(page_title="แผนเที่ยวสวิต", layout="wide")
st.title("🇨🇭 แผนเที่ยวสวิตเซอร์แลนด์ของพี่อุ๊ก & บิว 🤍")

# Read your travel plan from Excel
df = pd.read_excel("Plan/Swiss_plan_app.xlsx")

# Show the rail track image at the top
st.image("images/rail_track.png", use_column_width=True)

# Show your character and train images (one by one)
st.image("images/Train.png", width=100)
st.image("images/ouk_bew_chibi.png", width=100)

# Display each row from your travel plan
for idx, row in df.iterrows():
    st.markdown(f"### {row['Date']} - {row['Location']} to {row['Destination']}")
    st.write(f"**Time:** {row['Time']}")
    st.write(f"**Estimated Travel Time:** {row['EST Travel time (Minute)']} minutes")
    st.write(f"**Activity:** {row['Activity']}")
    st.write(f"**Transportation:** {row['Transportation']}")
    st.write(f"**Notes:** {row['Notes']}")
    st.markdown("---")
