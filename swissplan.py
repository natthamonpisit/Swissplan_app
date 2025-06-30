import streamlit as st
import pandas as pd

# ตั้งค่าหน้าเว็บ
st.set_page_config(page_title="แผนเที่ยวสวิต", layout="wide")
st.title("🇨🇭 แผนเที่ยวสวิตเซอร์แลนด์ของพี่อุ๊ก & บิว 🤍")
st.markdown("เลือกวันที่จะดูแผนได้เลยค่ะ")

# โหลด Excel
excel_path = "Plan/Swiss_plan_app.xlsx"
xls = pd.ExcelFile(excel_path)
sheet_names = xls.sheet_names
selected_day = st.selectbox("เลือกวัน", sheet_names)
df = pd.read_excel(excel_path, sheet_name=selected_day)

# หัวข้อวัน
st.markdown(f"### 📅 ข้อมูลสำหรับ {selected_day}")

# CSS
st.markdown("""
<style>
.timeline {
  position: relative;
  margin: 30px 0;
  padding-left: 50%;
}
.timeline::before {
  content: '';
  position: absolute;
  top: 0;
  bottom: 0;
  left: 50%;
  width: 6px;
  background: hotpink;
}
.timeline-item {
  position: relative;
  width: 50%;
  padding: 20px;
  box-sizing: border-box;
}
.timeline-left {
  left: -50%;
  text-align: right;
}
.timeline-right {
  left: 0%;
  text-align: left;
}
.timeline-box {
  background: #fff;
  color: #000;
  padding: 15px;
  border-radius: 10px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
  display: inline-block;
  max-width: 80%;
}
</style>
""", unsafe_allow_html=True)

# 🧠 สร้าง HTML timeline ทั้งหมด (รวมไว้ในตัวแปรเดียว)
timeline_html = '<div class="timeline">'

for i, row in df.iterrows():
    side = "timeline-left" if i % 2 == 0 else "timeline-right"
    timeline_html += f"""
    <div class="timeline-item {side}">
        <div class="timeline-box">
            <b>🕒 เวลา:</b> {row['Time']}<br>
            <b>📍 ต้นทาง:</b> {row['Location']}<br>
            <b>🛤️ ปลายทาง:</b> {row['Destination']}<br>
            <b>🎯 กิจกรรม:</b> {row['Activity']}
        </div>
    </div>
    """

timeline_html += '</div>'

# แสดงผล HTML timeline ทีเดียว
st.markdown(timeline_html, unsafe_allow_html=True)
