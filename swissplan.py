import streamlit as st  # ใช้สร้างหน้าเว็บแอป
import pandas as pd     # ใช้จัดการไฟล์ Excel และตารางข้อมูล

# --- ตั้งค่าหน้าเว็บ ---
st.set_page_config(page_title="แผนเที่ยวสวิต", layout="wide")
st.title("🇨🇭 แผนเที่ยวสวิตเซอร์แลนด์ของพี่อุ๊ก & บิว 🤍")
st.markdown("เลือกวันที่จะดูแผนได้เลยค่ะ")

# --- โหลดไฟล์ Excel และรายชื่อชีททั้งหมด ---
excel_path = "Plan/Swiss_plan_app.xlsx"  # path ไปยังไฟล์แผนเที่ยว
xls = pd.ExcelFile(excel_path)            # โหลดไฟล์ Excel แบบหลายชีท
sheet_names = xls.sheet_names             # ดึงชื่อชีททั้งหมดในไฟล์

# --- ให้พี่เลือกวันจาก dropdown ---
selected_day = st.selectbox("เลือกวัน", sheet_names)

# --- อ่านข้อมูลจากชีทที่เลือก ---
df = pd.read_excel(excel_path, sheet_name=selected_day)
df.columns = df.columns.str.strip()  # ลบช่องว่างในชื่อคอลัมน์เผื่อเผลอพิมพ์มา

# --- หัวข้อของวันนั้น ---
st.markdown(f"### 📅 ข้อมูลสำหรับ {selected_day}")

# --- CSS สำหรับเส้น Timeline และกล่องข้อความ ---
timeline_css = """
<style>
.timeline {
    position: relative;
    max-width: 1200px;
    margin: 50px auto;
}
.timeline::after {
    content: '';
    position: absolute;
    width: 6px;
    background-color: pink;
    top: 0;
    bottom: 0;
    left: 50%;
    margin-left: -3px;
}
.timeline-item {
    padding: 10px 30px;
    position: relative;
    width: 50%;
}
.timeline-left {
    left: 0;
}
.timeline-right {
    left: 50%;
}
.timeline-box {
    padding: 15px;
    background: white;
    color: black;
    border-radius: 10px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.1);
    position: relative;
}
.timeline-left .timeline-box {
    margin-left: auto;
    text-align: right;
}
.timeline-right .timeline-box {
    margin-right: auto;
    text-align: left;
}
</style>
"""

# --- เริ่มสร้าง HTML แสดง Timeline ---
timeline_html = '<div class="timeline">'

# วนลูปแสดงข้อมูลแต่ละแถวในแนวตั้ง
for i, row in df.iterrows():
    # ถ้าแถวนั้นว่างทั้งหมด ไม่ต้องแสดง
    if pd.isna(row['Time']) and pd.isna(row['Location']) and pd.isna(row['Destination']) and pd.isna(row['Activity']):
        continue

    # สลับตำแหน่งซ้ายขวา (แบบฟันปลา)
    side = "timeline-left" if i % 2 == 0 else "timeline-right"

    # เพิ่ม HTML ของแต่ละบล็อกแผน
    timeline_html += f"""
    <div class="timeline-item {side}">
        <div class="timeline-box">
            <b>🕒 เวลา:</b> {row['Time'] or '-'}<br>
            <b>📍 ต้นทาง:</b> {row['Location'] or '-'}<br>
            <b>🏁 ปลายทาง:</b> {row['Destination'] or '-'}<br>
            <b>🎯 กิจกรรม:</b> {row['Activity'] or '-'}
        </div>
    </div>
    """

timeline_html += "</div>"

# --- แสดงผลบนหน้าเว็บ ---
st.markdown(timeline_css + timeline_html, unsafe_allow_html=True)
