# นำเข้าไลบรารีที่จำเป็น
import streamlit as st    # ใช้สร้างหน้าเว็บแบบ interactive
import pandas as pd       # ใช้โหลด/จัดการข้อมูลตาราง Excel

# --------------------- 1. ตั้งค่าหน้าเว็บ ---------------------
st.set_page_config(page_title="แผนเที่ยวสวิต", layout="wide")  # ตั้งชื่อแท็บและขนาดจอ
st.title("🇨🇭 แผนเที่ยวสวิตเซอร์แลนด์ของพี่อุ๊ก & บิว 🤍")  # หัวเรื่อง
st.markdown("เลือกวันที่จะดูแผนได้เลยค่ะ")                # ข้อความใต้หัวเรื่อง

# --------------------- 2. โหลด Excel ---------------------
excel_path = "Plan/Swiss_plan_app.xlsx"  # ตำแหน่งไฟล์

# โหลด Excel ที่มีหลายชีทเข้ามา
xls = pd.ExcelFile(excel_path)           # pd.ExcelFile ช่วยเปิด Excel แบบไม่โหลดทั้งหมด
sheet_names = xls.sheet_names            # เอาชื่อชีททั้งหมดออกมา (Day1, Day2, ...)

# --------------------- 3. ให้เลือกวัน ---------------------
selected_day = st.selectbox("เลือกวัน", sheet_names)  # กล่อง dropdown เลือกวัน

# --------------------- 4. อ่านชีทที่เลือก ---------------------
df = pd.read_excel(excel_path, sheet_name=selected_day)

# ล้าง space ที่ชื่อคอลัมน์ (ป้องกันชื่อแบบ " Time " ใช้ไม่ได้)
df.columns = df.columns.str.strip()

# --------------------- 5. แสดงหัวข้อของวัน ---------------------
st.markdown(f"### 📅 ข้อมูลสำหรับ {selected_day}")

# --------------------- 6. CSS สร้างเส้น Timeline ---------------------
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

# --------------------- 7. เตรียม HTML สำหรับ timeline ---------------------
timeline_html = '<div class="timeline">'  # เริ่ม div หลัก

# --------------------- 8. วนลูปสร้าง timeline แต่ละช่อง ---------------------
for i, row in df.iterrows():  # .iterrows() = วนอ่านแต่ละแถวใน DataFrame

    # --- ความรู้: pd.isna() ---
    # ใช้เช็คว่าค่าใน cell นั้นเป็นค่าว่าง (NaN) หรือเปล่า เช่น pd.isna("abc") = False, pd.isna(None) = True

    if pd.isna(row['Time']) and pd.isna(row['Location']) and pd.isna(row['Destination']) and pd.isna(row['Activity']):
        continue  # ข้ามถ้าไม่มีข้อมูลเลย

    # --- สลับซ้ายขวาแบบฟันปลา ---
    # i เป็นเลข index 0, 1, 2, ...
    # ถ้าเลขคู่ (0, 2, 4) ให้แสดงซ้าย / ถ้าเลขคี่ (1, 3, 5) ให้แสดงขวา
    side = "timeline-left" if i % 2 == 0 else "timeline-right"

    # --- สร้าง HTML ของกล่องแต่ละแถว ---
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

# ปิด tag div หลัก timeline
timeline_html += "</div>"

# --------------------- 9. แสดงผลบนเว็บ ---------------------
# unsafe_allow_html=True คือให้ HTML & CSS ที่เราเขียนแสดงผลได้
st.markdown(timeline_css + timeline_html, unsafe_allow_html=True)
