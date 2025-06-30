import streamlit as st
import pandas as pd

st.set_page_config(page_title="แผนเที่ยวสวิต", layout="wide")
st.title("🇨🇭 แผนเที่ยวสวิตเซอร์แลนด์ของพี่อุ๊ก & บิว 🤍")
st.markdown("เลือกวันที่จะดูแผนได้เลยค่ะ")

# โหลด Excel
excel_path = "Plan/Swiss_plan_app.xlsx"
xls = pd.ExcelFile(excel_path)
sheet_names = xls.sheet_names

selected_day = st.selectbox("เลือกวัน", sheet_names)
df = pd.read_excel(excel_path, sheet_name=selected_day)

# ฟังก์ชันสำหรับแสดงตาราง HTML แบบสวยงาม
def render_html_table(df):
    html = df.to_html(index=False, escape=False)
    styled = """
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
            border: 1px solid #ccc;
            padding: 10px;
            white-space: pre-wrap;
            word-break: break-word;
            vertical-align: top;
        }
    </style>
    """
    return styled + html

# แสดงผล
st.markdown(f"### 📅 ข้อมูลสำหรับ {selected_day}")
st.markdown(render_html_table(df), unsafe_allow_html=True)
