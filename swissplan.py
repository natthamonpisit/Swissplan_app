import streamlit as st
import pandas as pd

# --- ตั้งค่าหน้าเว็บ ---
st.set_page_config(page_title="แผนเที่ยวสวิต", layout="wide")
st.title("🇨🇭 แผนเที่ยวสวิตเซอร์แลนด์ของพี่อุ๊ก & บิว 🤍")
st.markdown("เลือกวันที่จะดูแผนได้เลยค่ะ")

# --- โหลดไฟล์ Excel ---
excel_path = "Plan/Swiss_plan_app.xlsx"
xls = pd.ExcelFile(excel_path)
sheet_names = xls.sheet_names
selected_day = st.selectbox("เลือกวัน", sheet_names)
df = pd.read_excel(excel_path, sheet_name=selected_day)
df.columns = df.columns.str.strip()

# --- CSS ---
timeline_css = """
<style>
.timeline {
    position: relative;
    margin: 50px 0;
    padding: 0;
}
.timeline::before {
    content: '';
    position: absolute;
    left: 50%;
    top: 0;
    bottom: 0;
    width: 6px;
    background: pink;
    margin-left: -3px;
    z-index: 0;
}
.timeline-item {
    position: relative;
    width: 50%;
    padding: 10px;
}
.timeline-left {
    left: 0;
    text-align: right;
}
.timeline-right {
    left: 50%;
}
.timeline-box {
    background: white;
    color: black;
    padding: 15px;
    border-radius: 12px;
    display: inline-block;
    max-width: 90%;
    box-shadow: 0 2px 10px rgba(0,0,0,0.2);
    z-index: 1;
}
</style>
"""

# --- สร้าง HTML กล่องทั้งหมดไว้ก่อน ---
timeline_html = '<div class="timeline">'
for i, row in df.iterrows():
    if pd.isna(row["Time"]):
        continue
    side = "timeline-left" if i % 2 == 0 else "timeline-right"
    box = f"""
    <div class="timeline-item {side}">
        <div class="timeline-box">
            <b>🕒 เวลา:</b> {row["Time"]}<br>
            <b>📍 ต้นทาง:</b> {row["Location"]}<br>
            <b>🏁 ปลายทาง:</b> {row["Destination"]}<br>
            <b>🎯 กิจกรรม:</b> {row["Activity"]}
        </div>
    </div>
    """
    timeline_html += box
timeline_html += "</div>"

# --- แสดงผลทั้งหมดพร้อมกัน (เพื่อให้เส้นชมพูทำงาน) ---
st.markdown(f"### 🗓️ ข้อมูลสำหรับ {selected_day}")
st.markdown(timeline_css + timeline_html, unsafe_allow_html=True)
