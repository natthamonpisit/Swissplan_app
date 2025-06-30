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

# --- CSS สำหรับ timeline ---
st.markdown("""
<style>
.timeline-container {
    position: relative;
    margin-top: 40px;
    padding-bottom: 50px;
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
""", unsafe_allow_html=True)

# --- เปิด timeline-container ---
st.markdown('<div class="timeline-container"><div class="vertical-line"></div>', unsafe_allow_html=True)

# --- แสดงแต่ละกล่อง ---
def safe_html(text):
    if pd.isna(text):
        return ""
    return str(text).replace("<", "&lt;").replace(">", "&gt;")

for i, row in df.iterrows():
    if pd.isna(row["Time"]): continue

    side = "timeline-left" if i % 2 == 0 else "timeline-right"
    html = f"""
    <div class="timeline-item {side}">
        <div class="timeline-box">
            <b>🕒 เวลา:</b> {safe_html(row["Time"])}<br>
            <b>📍 ต้นทาง:</b> {safe_html(row["Location"])}<br>
            <b>🏁 ปลายทาง:</b> {safe_html(row["Destination"])}<br>
            <b>🎯 กิจกรรม:</b> {safe_html(row["Activity"])}
        </div>
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)

# --- ปิด timeline container ---
st.markdown('</div>', unsafe_allow_html=True)
