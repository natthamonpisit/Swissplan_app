import streamlit as st
import pandas as pd

# -----------------------------
# 📌 ตั้งค่าหน้าเว็บ
# -----------------------------
st.set_page_config(page_title="แผนเที่ยวสวิต", layout="wide")
st.title("🇨🇭 แผนเที่ยวสวิตเซอร์แลนด์ของพี่อุ๊ก & บิว 🤍")
st.markdown("เลือกวันที่จะดูแผนได้เลยค่ะ")

# -----------------------------
# 📥 อ่านข้อมูลจาก Excel
# -----------------------------
excel_path = "Plan/Swiss_plan_app.xlsx"
xls = pd.ExcelFile(excel_path)
sheet_names = xls.sheet_names
selected_day = st.selectbox("เลือกวัน", sheet_names)

df = pd.read_excel(excel_path, sheet_name=selected_day)
df.columns = df.columns.str.strip()  # ลบช่องว่างจากหัวคอลัมน์

# -----------------------------
# 🎨 CSS สำหรับ Timeline
# -----------------------------
timeline_css = """
<style>
.timeline {
    position: relative;
    margin: 40px 0;
    padding: 0;
}
.timeline::before {
    content: '';
    position: absolute;
    left: 50%;
    top: 0;
    bottom: 0;
    width: 6px;
    background: #ff80b5;  /* เส้นกลางสีชมพู */
    margin-left: -3px;
}
.timeline-item {
    padding: 20px;
    position: relative;
    width: 50%;
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
    padding: 15px;
    border-radius: 12px;
    display: inline-block;
    max-width: 90%;
    box-shadow: 0 2px 15px rgba(0,0,0,0.1);
    font-size: 16px;
    line-height: 1.5;
}
</style>
"""

# -----------------------------
# 🖼️ แสดงผล
# -----------------------------
st.markdown(f"### 🗓️ ข้อมูลสำหรับ {selected_day}")
st.markdown(timeline_css, unsafe_allow_html=True)  # แสดง CSS แค่ครั้งเดียว

# เปิดแท็ก timeline กลาง
st.markdown('<div class="timeline">', unsafe_allow_html=True)

# วนแสดงแต่ละกล่อง
for i, row in df.iterrows():
    if pd.isna(row["Time"]):  # ถ้าไม่มีเวลา ให้ข้ามแถวนี้ไป
        continue

    # สลับตำแหน่งซ้ายขวาแบบฟันปลา
    side = "timeline-left" if i % 2 == 0 else "timeline-right"

    # กล่องแต่ละเหตุการณ์
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

# ปิดแท็ก timeline
st.markdown("</div>", unsafe_allow_html=True)
