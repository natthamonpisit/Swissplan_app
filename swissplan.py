import streamlit as st              # เรียกใช้ไลบรารี Streamlit สำหรับทำเว็บแอป
import pandas as pd                # เรียกใช้ Pandas เพื่อโหลดและจัดการข้อมูล Excel

# ตั้งค่าหน้าเว็บให้มีชื่อและเป็น layout กว้าง
st.set_page_config(page_title="แผนเที่ยวสวิต", layout="wide")

# แสดงหัวข้อใหญ่ของหน้าเว็บ
st.title("🇨🇭 แผนเที่ยวสวิตเซอร์แลนด์ของพี่อุ๊ก & บิว 🤍")

# ข้อความนำสั้นๆ บอกให้ผู้ใช้เลือกวัน
st.markdown("เลือกวันที่จะดูแผนได้เลยค่ะ")

# --------------------------
# โหลดไฟล์ Excel และชื่อชีต
# --------------------------

excel_path = "Plan/Swiss_plan_app.xlsx"     # กำหนด path ของไฟล์ Excel ที่เก็บแผน
xls = pd.ExcelFile(excel_path)              # โหลดไฟล์แบบ ExcelFile เพื่อดูรายชื่อชีต
sheet_names = xls.sheet_names               # ดึงชื่อชีตทั้งหมด (เช่น Day1, Day2)

# ให้ผู้ใช้เลือกชีตที่จะดู (วันไหน)
selected_day = st.selectbox("เลือกวัน", sheet_names)

# อ่านข้อมูลจากชีตที่เลือกมาเก็บไว้ใน DataFrame
df = pd.read_excel(excel_path, sheet_name=selected_day)

# แสดงหัวข้อย่อยเป็นชื่อวัน เช่น "ข้อมูลสำหรับ Day1"
st.markdown(f"### 📅 ข้อมูลสำหรับ {selected_day}")

# --------------------------
# ใส่ CSS สำหรับจัดรูปแบบ timeline
# ------------------
