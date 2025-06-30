import streamlit as st
import pandas as pd

# ตั้งค่าหน้าเว็บ
st.set_page_config(page_title="แผนเที่ยวสวิต", layout="wide")
st.title("🇨🇭 แผนเที่ยวสวิตเซอร์แลนด์ของพี่อุ๊ก & บิว 🤍")
st.markdown("เลือกวันที่จะดูแผนได้เลยค่ะ")

# โหลดชื่อชีททั้งหมดจากไฟล์ Excel
excel_path = "Plan/Swiss_plan_app.xlsx"
xls = pd.ExcelFile(excel_path)
sheet_names = xls.sheet_names

# ให้พี่เลือกวันจากชีท
selected_day = st.selectbox("เลือกวัน", sheet_names)

# อ่านข้อมูลจากชีทที่เลือก
df = pd.read_excel(excel_path, sheet_name=selected_day)

# แสดงหัวข้อ
st.markdown(f"### 📅 ข้อมูลสำหรับ {selected_day}")

# ---- CSS และ HTML ----
table_style = """
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

# สร้าง HTML จาก DataFrame
html_table = df.to_html(index=False, escape=False)

# แสดง HTML + CSS ด้วย markdown (เปิดให้ HTML ทำงานได้)
st.markdown(table_style + html_table, unsafe_allow_html=True)
