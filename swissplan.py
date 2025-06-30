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

# --- CSS ฟันปลา timeline และกล่องชิดเส้น (กล่องแรกซ้าย) ---
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
    display: flex;
    flex-direction: column;
    position: relative;
    z-index: 1;
    gap: 40px;
}
.timeline-item {
    width: 100%;
    display: flex;
    justify-content: center;
    position: relative;
}
.timeline-item.timeline-left {
    justify-content: flex-start;   /* ซ้าย */
}
.timeline-item.timeline-right {
    justify-content: flex-end;     /* ขวา */
}
.timeline-box {
    background: white;
    color: black;
    padding: 15px;
    border-radius: 12px;
    max-width: 45%;
    min-width: 220px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.2);
    text-align: left;
    word-break: break-word;
}
.timeline-item.timeline-left .timeline-box {
    margin-left: 30px;
    margin-right: 0;
}
.timeline-item.timeline-right .timeline-box {
    margin-right: 30px;
    margin-left: 0;
}
</style>
""", unsafe_allow_html=True)

# --- เตรียมข้อมูล row ที่จะแสดงจริง ---
rows_to_show = []
for _, row in df.iterrows():
    if all(pd.isna(row[col]) or str(row[col]).strip() == "" for col in ["Time", "Location", "Destination", "Activity"]):
        continue
    if pd.isna(row["Time"]) or str(row["Time"]).strip() == "":
        continue
    rows_to_show.append(row)

# --- สร้าง timeline HTML ---
timeline_html = (
    '<div class="timeline-wrapper">'
    '<div class="timeline-line"></div>'
    '<div class="timeline-box-wrapper">'
)

for idx, row in enumerate(rows_to_show):
    side = "timeline-left" if idx % 2 == 0 else "timeline-right"
    timeline_item_class = f'timeline-item {side}'
    box_html = (
        f'<div class="{timeline_item_class}">'
        f'<div class="timeline-box">'
        f'<b>🕒 เวลา:</b> {safe_html(row["Time"])}<br>'
        f'<b>📍 ต้นทาง:</b> {safe_html(row["Location"])}<br>'
        f'<b>🏁 ปลายทาง:</b> {safe_html(row["Destination"])}<br>'
        f'<b>🎯 กิจกรรม:</b> {safe_html(row["Activity"])}'
        f'</div>'
        f'</div>'
    )
    timeline_html += box_html

timeline_html += '</div></div>'
timeline_html = timeline_html.strip()

st.markdown(timeline_html, unsafe_allow_html=True)
