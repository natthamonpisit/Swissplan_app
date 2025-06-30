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

# --- CSS แบบแก้ให้เส้นยืดตามกล่องจริง ---
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
}
</style>
""", unsafe_allow_html=True)

# --- เริ่ม timeline ---
st.markdown('<div class="timeline-wrapper">', unsafe_allow_html=True)
st.markdown('<div class="timeline-line"></div>', unsafe_allow_html=True)
st.markdown('<div class="timeline-box-wrapper">', unsafe_allow_html=True)

# --- render box สลับซ้ายขวา ---
def safe_html(text):
    if pd.isna(text): return ""
    return str(text).replace("<", "&lt;").replace(">", "&gt;")

for i, row in df.iterrows():
    if pd.isna(row["Time"]): continue
    side = "timeline-left" if i % 2 == 0 else "timeline-right"
    box_html = f"""
    <div class="timeline-item {side}">
        <div class="timeline-box">
            <b>🕒 เวลา:</b> {safe_html(row["Time"])}<br>
            <b>📍 ต้นทาง:</b> {safe_html(row["Location"])}<br>
            <b>🏁 ปลายทาง:</b> {safe_html(row["Destination"])}<br>
            <b>🎯 กิจกรรม:</b> {safe_html(row["Activity"])}
        </div>
    </div>
    """
    st.markdown(box_html, unsafe_allow_html=True)

# --- ปิดกล่องและ wrapper ---
st.markdown("</div></div>", unsafe_allow_html=True)
