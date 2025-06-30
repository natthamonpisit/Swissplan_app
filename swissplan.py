import streamlit as st
import pandas as pd
# Header -------------------------------------------------------------------
st.title("🌄 Hello from พี่อุ๊ก & บิว")
st.write("ยินดีต้อนรับสู่แอป Streamlit อันแรกของเรา! 🎒💕")
st.title("🇨🇭 แผนเที่ยวสวิตเซอร์แลนด์ของพี่อุ๊ก & บิว")
# End Header -------------------------------------------------------------------

# อ่านข้อมูลจาก Excel
df = pd.read_excel("Plan/Swiss_plan_app.xlsx", sheet_name=None)  # sheet_name=None คืออ่านทุกชีต

# สร้างตัวเลือกวันจากชื่อชีต (sheet names)
day_options = list(df.keys())
selected_day = st.selectbox("เลือกวัน", day_options)

# ดึงเฉพาะข้อมูลของวันนั้น
day_data = df[selected_day]

# แสดงผลแบบตารางธรรมดาก่อน (เอาไว้เช็คว่าอ่านถูก)
st.write(f"📅 ข้อมูลสำหรับ {selected_day}")
st.dataframe(day_data)


