import streamlit as st
import pandas as pd

# --- ตั้งค่าหน้าเว็บ ---
st.set_page_config(page_title="แผนเที่ยวสวิต", layout="wide")
st.title("🇨🇭 แผนเที่ยวสวิตเซอร์แลนด์ของพี่อุ๊ก & บิว 🤍")
st.markdown("เลือกวันที่จะดูแผนได้เลยค่ะ")

# --- โหลด Excel ---
excel_path = "Plan/Swiss_plan_app.xlsx"
xls = pd.ExcelFile(excel_path)
sheet_names = xls.sheet_names
selected_day = st.selectbox("เลือกวัน", sheet_names)
df = pd.read_excel(excel_path, sheet_name=selected_day)
df.columns = df.columns.str.strip()

# --- ล้าง HTML tag ที่อาจมาจาก Excel ---
def sanitize(text):
    if pd.isna(text):
        return ""
    return str(text).replace("<", "&lt;").replace(">", "&gt;")

# --- CSS + เปิด div container ---
timeline_html = """
<style>
.timeline-container {
    position: relative;
    width: 100%;
    margin-top: 40px;
}
.vertical-line {
    position: absolute;
    top: 0;
    bottom: 0;
    left: 50%;
    width: 6px;
    background-color: pink;
    transform: translateX(-50%);
    z-index: 0;
}
.timeline-item {
    position: relative;
    width: 50%;
    padding: 10px;
    z-index: 1;
}
.timeline-left {
    margin-right: 55%;
    text-align: right;
}
.timeline-right {
    margin-left: 55%;
    text-align: left;
}
.timeline-box {
    background: white;
    color: black;
    padding: 15px;
    border-radius: 12px;
    display: inline-block;
    max-width: 90%;
    box-shadow: 0 2px 10px rgba(0,0,0,0.2);
}
</style>
<div class="timeline-container">
    <div class="vertical-line"></div>
"""

# --- วนลูปแสดงกล่องใน timeline ---
for i, row in df.iterrows():
    if pd.isna(row["Time"]): continue
    side = "timeline-left" if i % 2 == 0 else "timeline-right"

    time = sanitize(row["Time"])
    loc = sanitize(row["Location"])
    dest = sanitize(row["Destination"])
    act = sanitize(row["Activity"])

    timeline_html += f"""
    <div class="timeline-item {side}">
        <div class="timeline-box">
            <b>🕒 เวลา:</b> {time}<br>
            <b>📍 ต้นทาง:</b> {loc}<br>
            <b>🏁 ปลายทาง:</b> {dest}<br>
            <b>🎯 กิจกรรม:</b> {act}
        </div>
    </div>
    """

# --- ปิด div timeline-container ---
timeline_html += "</div>"

# --- แสดงข้อมูลสำหรับวัน ---
st.markdown(f"### 🗓️ ข้อมูลสำหรับ {selected_day}")
st.markdown(timeline_html, unsafe_allow_html=True)
