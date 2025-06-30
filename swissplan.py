import streamlit as st

st.title("🌄 Hello from พี่อุ๊ก & บิว")
st.write("ยินดีต้อนรับสู่แอป Streamlit อันแรกของเรา! 🎒💕")

st.title("🇨🇭 แผนเที่ยวสวิตเซอร์แลนด์ของพี่อุ๊ก & บิว")

st.header("📍 Day 1 - เดินทางถึง Zurich")

st.image("https://grazietravel.com/wp-content/uploads/2020/04/Lake-Z%C3%BCrich.jpg",
    caption="วิวเมือง Zurich",
    use_container_width=True  # ← ใช้อันนี้แทน
)
st.write("✅ เดินเล่นในเมือง พักผ่อนที่โรงแรมแถว Bahnhofstrasse")

# จบ Day 1 -------------------------------------------------------------------------------------------------
st.header("📍 Day 2 - ขึ้นรถไฟไป Lucerne")

col1, col2 = st.columns(2)

with col1:
    st.image("https://upload.wikimedia.org/wikipedia/commons/8/8b/LuzernKapellbruecke.jpg", 
             caption="สะพานไม้ Kapellbrücke", 
             use_container_width=True)

with col2:
    st.write("🚉 ออกเดินทางจาก Zurich เวลา 09:00 น.")
    st.write("🕰 ถึง Lucerne ประมาณ 10:00 น.")
    st.write("🌉 เดินเที่ยวสะพานไม้เก่า, Old Town")
    st.write("🏨 เข้าที่พักแถวริมทะเลสาบ Lucerne")

