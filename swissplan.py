import streamlit as st
import pandas as pd

# --- ฟังก์ชัน escape html ---
def safe_html(text):
    if pd.isna(text): return ""
    return str(text).strip().replace("<", "&lt;").replace(">", "&gt;").replace("\n", "<br>")

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

# --- CSS ปรับกล่องซ้าย/ขวา และข้อความชิดซ้าย ---
st.markdown("""
<style>
.timeline-wrapper {
    position: relative;
    width: 100%;
    margin-top: 40px;
    padding-bottom: 50px;
    min-height: 400px;
}
.timeline-line {
    position: absolute;
    top: 0;
    bottom: 0;
    left: 50%;
    width: 6px;
    background-color: pink;
    transform: translateX(-50%);
    z-index: 0;
}
.timeline-box-wrapper {
    position: relative;
    z-index: 1;
}
.timeline-item {
    width: 45%;
    padding: 10px;
}
.timeline-left {
    float: left;
    margin-left: 0;
    margin-right: 5%;
}
.timeline-right {
    float: right;
    margin-right: 0;
    margin-left: 5%;
}
.timeline-box {
    background: white;
    color: black;
    padding: 15px;
    border-radius: 12px;
    display: inline-block;
    max-width: 100%;
    box-shadow: 0 2px 10px rgba(0,0,0,0.2);
    text-align: left; /* จัดข้อความชิดซ้าย */
    word-break: break-word;
}
.timeline-box-wrapper:after {
    content: "";
    display: table;
    clear: both;
}
</style>
""", unsafe_allow_html=True)

# --- เริ่ม timeline ---
timeline_html = (
    '<div class="timeline-wrapper">'
    '<div class="timeline-line"></div>'
    '<div class="timeline-box-wrapper">'
)

for i, row in df.iterrows():
    # ข้าม row ที่ว่างจริงๆ
    if all(pd.isna(row[col]) or str(row[col]).strip() == "" for col in ["Time", "Location", "Destination", "Activity"]):
        continue
    if pd.isna(row["Time"]) or str(row["Time"]).strip() == "":
        continue
    side = "timeline-left" if i % 2 == 0 else "timeline-right"
    box_html = (
        f'<div class="timeline-item {side}">'
        f'<div class="timeline-box">'
        f'<b>🕒 เวลา:</b> {safe_html(row["Time"])}<br>'
        f'<b>📍 ต้นทาง:</b> {safe_html(row["Location"])}<br>'
        f'<b>🏁 ปลายทาง:</b> {safe_html(row["Destination"])}<br>'
        f'<b>🎯 กิจกรรม:</b> {safe_html(row["Activity"])}'
        f'</div>'
        f'</div>'
    )
    timeline_html += box_html

timeline_html += '</div></div>'  # ปิด div ไม่มีบรรทัดว่างต่อท้าย

timeline_html = timeline_html.strip()

st.markdown(timeline_html, unsafe_allow_html=True)
