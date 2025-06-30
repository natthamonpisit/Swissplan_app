import streamlit as st
import pandas as pd

# --- ตั้งค่าหน้าเว็บ ---
st.set_page_config(page_title="แผนเที่ยวสวิตฯ", layout="wide")

# --- หัวเรื่อง ---
st.title("🇨🇭 แผนเที่ยวสวิตเซอร์แลนด์ของพี่อุ๊ก & บิว 🤍")
st.markdown("เลือกวันที่จะดูแผนได้เลยค่ะ")

# --- อ่าน Excel และเอาชื่อชีตมาเป็น options ---
excel_path = "Plan/Swiss_plan_app.xlsx"
xls = pd.ExcelFile(excel_path)
sheet_names = xls.sheet_names

selected_day = st.selectbox("เลือกวัน", sheet_names)

# --- อ่านเฉพาะ sheet ที่เลือก ---
df = pd.read_excel(excel_path, sheet_name=selected_day)

# --- สร้างตาราง HTML พร้อม CSS สำหรับ wrap text ---
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
            word-wrap: break-word;
            white-space: pre-wrap;
            max-width: 250px;
            text-align: left;
        }
    </style>
    """
    return style + html

# --- แสดงตารางที่ wrap text แล้ว ---
st.markdown(f"### 📅 ข้อมูลสำหรับ {selected_day}", unsafe_allow_html=True)
st.markdown(render_html_table(df), unsafe_allow_html=True)
