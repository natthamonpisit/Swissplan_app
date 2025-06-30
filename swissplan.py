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
df.columns = df.columns.str.strip()  # ลบช่องว่างจากชื่อคอลัมน์

# --- แสดงหัวข้อ ---
st.markdown(f"### 🗓️ ข้อมูลสำหรับ {selected_day}")

# --- CSS สำหรับ Timeline ---
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

# --- แสดง CSS แค่ครั้งเดียวก่อนลูป ---
st.markdown(timeline_css + '<div class="timeline">', unsafe_allow_html=True)

# --- สร้างและแสดงกล่องทีละอันใน loop ---
for i, row in df.iterrows():
    if pd.isna(row["Time"]):
        continue  # ข้ามแถวที่ไม่มีเวลา
    side = "timeline-left" if i % 2 == 0 else "timeline-right"
    html_box = f"""
    <div class="timeline-item {side}">
        <div class="timeline-box">
            <b>🕒 เวลา:</b> {row["Time"]}<br>
            <b>📍 ต้นทาง:</b> {row["Location"]}<br>
            <b>🏁 ปลายทาง:</b> {row["Destination"]}<br>
            <b>🎯 กิจกรรม:</b> {row["Activity"]}
        </div>
    </div>
    """
    st.markdown(html_box, unsafe_allow_html=True)

# --- ปิด div timeline ---
st.markdown("</div>", unsafe_allow_html=True)
