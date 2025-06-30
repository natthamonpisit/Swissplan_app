import streamlit as st
import pandas as pd

# ... (โค้ดเตรียมข้อมูล timeline เดิม) ...

# --- CSS + JS สำหรับการ์ตูนลอยและหยุดที่ปลายเส้น ---
st.markdown("""
<style>
.chibi-sticky {
    position: fixed;
    top: 180px;
    left: 50%;
    transform: translateX(-50%);
    z-index: 10;
    width: 80px;
    pointer-events: none;
    transition: top 0.2s;
}
.chibi-absolute {
    position: absolute !important;
    left: 50%;
    transform: translateX(-50%);
    width: 80px;
    z-index: 10;
}
#timeline-end-anchor {
    position: absolute;
    left: 50%;
    transform: translateX(-50%);
    height: 1px;
    width: 1px;
    bottom: 0;
}
</style>
<script>
window.addEventListener('DOMContentLoaded', function() {
    const chibi = document.querySelector('.chibi-sticky');
    const anchor = document.getElementById('timeline-end-anchor');
    function onScroll() {
        if (!chibi || !anchor) return;
        const anchorRect = anchor.getBoundingClientRect();
        const chibiHeight = chibi.offsetHeight;
        // ถ้า anchor ขึ้นมาอยู่บนจอ (ถึงปลาย timeline)
        if (anchorRect.top < (180 + chibiHeight)) {
            chibi.classList.add('chibi-absolute');
            chibi.style.top = (anchorRect.top - chibiHeight) + 'px';
        } else {
            chibi.classList.remove('chibi-absolute');
            chibi.style.top = '180px';
        }
    }
    window.addEventListener('scroll', onScroll);
    onScroll();
});
</script>
""", unsafe_allow_html=True)

# --- แสดงรูปการ์ตูนลอยบนเส้น (ใช้ Raw URL จาก GitHub) ---
st.markdown(
    '<img class="chibi-sticky" src="https://github.com/natthamonpisit/Swissplan_app/blob/main/images/ouk_bew_chibi.png?raw=true">',
    unsafe_allow_html=True
)

# --- สร้าง timeline HTML (เพิ่ม anchor ที่ปลาย timeline) ---
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

# --- เพิ่ม anchor ที่ปลาย timeline ---
timeline_html += '<div id="timeline-end-anchor"></div></div></div>'
timeline_html = timeline_html.strip()

st.markdown(timeline_html, unsafe_allow_html=True)
