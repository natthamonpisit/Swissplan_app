import streamlit as st
import pandas as pd

# ตั้งค่าหน้าเว็บ
st.set_page_config(page_title="แผนเที่ยวสวิต", layout="wide")
st.title("🇨🇭 แผนเที่ยวสวิตเซอร์แลนด์ของพี่อุ๊ก & บิว 🤍")
st.markdown("เลือกวันที่จะดูแผนได้เลยค่ะ")

# โหลดชื่อชีททั้งหมดจากไฟล์ Excel
excel_path = "Plan/Swiss_plan_app.xlsx"
xls = pd.ExcelFile(excel_path)
sheet_names = xls.sheet_names

# ให้พี่เลือกวันจากชีท
selected_day = st.selectbox("เลือกวัน", sheet_names)

# อ่านข้อมูลจากชีทที่เลือก
df = pd.read_excel(excel_path, sheet_name=selected_day)

# แสดงหัวข้อ
st.markdown(f"### 📅 ข้อมูลสำหรับ {selected_day}")

# ---- CSS และ HTML ----
# HTML + CSS สำหรับ timeline
timeline_html = """
<style>
.timeline-container {
    position: relative;
    width: 100%;
    padding: 50px 0;
}
.timeline-line {
    position: absolute;
    left: 50%;
    top: 0;
    bottom: 0;
    width: 6px;
    background-color: #ff80b3;
    margin-left: -3px;
}
.timeline-item {
    position: relative;
    width: 50%;
    padding: 20px 40px;
    box-sizing: border-box;
}
.timeline-left {
    left: 0;
    text-align: right;
}
.timeline-right {
    left: 50%;
    text-align: left;
}
.timeline-box {
    background-color: #fff0f5;
    padding: 15px;
    border-radius: 10px;
    border: 1px solid #ffb6c1;
    font-size: 16px;
    line-height: 1.6;
    display: inline-block;
    max-width: 90%;
}
</style>
<div class="timeline-container">
    <div class="timeline-line"></div>
"""

# สร้าง timeline item จาก dataframe
for idx, row in df.iterrows():
    side = "timeline-left" if idx % 2 == 0 else "timeline-right"
    location = row.get("Location", "")
    destination = row.get("Destination", "")
    time = row.get("Time", "")
    activity = row.get("Activity", "")
    
    item_html = f"""
    <div class="timeline-item {side}">
        <div class="timeline-box">
            <b>🕒 เวลา:</b> {time}<br>
            <b>📍 ต้นทาง:</b> {location}<br>
            <b>🚉 ปลายทาง:</b> {destination}<br>
            <b>🎯 กิจกรรม:</b> {activity}
        </div>
    </div>
    """
    timeline_html += item_html

timeline_html += "</div>"

# แสดงผล
st.markdown(timeline_html, unsafe_allow_html=True)
