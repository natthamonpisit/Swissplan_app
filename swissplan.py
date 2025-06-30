import streamlit as st
import pandas as pd

# ตั้งค่าหน้า Streamlit
st.set_page_config(page_title="แผนเที่ยวสวิตฯ", layout="wide")

st.title("Test")
st.markdown("เลือกวันที่จะดูแผนได้เลยค่ะ")

# โหลด Excel และชื่อชีต
excel_path = "Plan/Swiss_plan_app.xlsx"
xls = pd.ExcelFile(excel_path)
sheet_names = xls.sheet_names

# ให้ผู้ใช้เลือกวัน
selected_day = st.selectbox("เลือกวัน", sheet_names)

# โหลดข้อมูลใน sheet ที่เลือก
df = pd.read_excel(excel_path, sheet_name=selected_day)

# แสดงตารางพร้อม wrap text สวยงาม
def render_html_table(df):
    html = df.to_html(index=False, escape=False)
    style = """
    <style>
        table {
            border-collapse: collapse;
            width: 100%;
            font-size: 16px;
        }
        th {
            background-color: #f0f0f0;
        }
        td, th {
            border: 1px solid #ddd;
            padding: 10px;
            white-space: pre-wrap;
            word-break: break-word;
            text-align: left;
            vertical-align: top;
            max-width: 300px;
        }
    </style>
    """
    return style + html

# แสดงผล
st.markdown(f"### 📅 ข้อมูลสำหรับ {selected_day}")
st.markdown(render_html_table(df), unsafe_allow_html=True)
