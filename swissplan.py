import streamlit as st
import pandas as pd

# -------------------------------
# 🛠️ ตั้งค่าหน้าเว็บ
# -------------------------------
st.set_page_config(page_title="แผนเที่ยวสวิต", layout="wide")
st.title("🇨🇭 แผนเที่ยวสวิตเซอร์แลนด์ของพี่อุ๊ก & บิว 🤍")
st.markdown("เลือกวันที่จะดูแผนได้เลยค่ะ")

# -------------------------------
# 📥 โหลด Excel และดึงชื่อชีท
# -------------------------------
excel_path = "Plan/Swiss_plan_app.xlsx"
xls = pd.ExcelFile(excel_path)
sheet_names = xls.sheet_names
selected_day = st.selectbox("เลือกวัน", sheet_names)

# โหลดเฉพาะชีทที่เลือก
df = pd.read_excel(excel_path, sheet_name=selected_day)
df.columns = df.columns.str.strip()  # ลบช่องว่างจากชื่อคอลัมน์

# -------------------------------
# 💅 CSS สำหรับ timeline สองฝั่ง
# -------------------------------
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
}

.timeline-item {
    position: relative;
    width: 50%;
    padding: 20px;
    box-sizing: border-box;
}

.timeline-left {
    left: 0;
    text-align: right;
}

.timeline-right {
    left: 50%;
    text-align: left;
    position: absolute;
}

.timeline-box {
    background: white;
    color: black; /* ✅ ทำให้ตัวอักษรไม่จาง */
    padding: 15px;
    border-radius: 10px;
    display: inline-block;
    max-width: 90%;
    box-shadow: 0 2px 10px rgba(0,0,0,0.2);
    font-size: 16px;
}
</style>
"""

# -------------------------------
# 🧱 สร้าง HTML timeline ทีละกล่อง
# -------------------------------
timeline_html = '<div class="timeline">'

for i, row in df.iterrows():
    # ข้ามแถวที่ไม่มีเวลา และไม่มีข้อความอื่นเลย
    if pd.isna(row.get("Time")) and pd.isna(row.get("Location")) and pd.isna(row.get("Destination")) and pd.isna(row.get("Activity")):
        continue

    # สลับฝั่งซ้ายขวาตาม index
    side = "timeline-left" if i % 2 == 0 else "timeline-right"

    # ดึงข้อมูลแต่ละช่อง และ fallback ถ้าค่าว่าง
    time = row["Time"] if pd.notna(row["Time"]) else "-"
    location = row["Location"] if pd.notna(row["Location"]) else "-"
    destination = row["Destination"] if pd.notna(row["Destination"]) else "-"
    activity = row["Activity"] if pd.notna(row["Activity"]) else "-"

    box = f"""
    <div class="timeline-item {side}">
        <div class="timeline-box">
            <b>🕒 เวลา:</b> {time}<br>
            <b>📍 ต้นทาง:</b> {location}<br>
            <b>🏁 ปลายทาง:</b> {destination}<br>
            <b>🎯 กิจกรรม:</b> {activity}
        </div>
    </div>
    """
    timeline_html += box

timeline_html += "</div>"

# -------------------------------
# ✅ แสดงผล
# -------------------------------
st.markdown(f"### 🗓️ ข้อมูลสำหรับ {selected_day}")
st.markdown(timeline_css + timeline_html, unsafe_allow_html=True)
