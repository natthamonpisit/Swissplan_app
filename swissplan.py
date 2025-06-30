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

# --- CSS: เส้นแนวตั้งกลางหน้าจอแบบแยก ---
css_code = """
<style>
.vertical-line {
    position: fixed;
    top: 320px; /* <-- เดิม 100px ตอนนี้เลื่อนลง */
    bottom: 0;
    left: 50%;
    width: 6px;
    background-color: pink;
    z-index: 0;
}
.timeline-item {
    position: relative;
    width: 50%;
    padding: 10px;
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
    z-index: 1;
}
</style>
<div class="vertical-line"></div>
"""
st.markdown(css_code, unsafe_allow_html=True)

# --- หัวข้อ ---
st.markdown(f"### 🗓️ ข้อมูลสำหรับ {selected_day}")

# --- Loop แสดงแต่ละกิจกรรมแบบฟันปลา ---
for i, row in df.iterrows():
    if pd.isna(row["Time"]):
        continue
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
