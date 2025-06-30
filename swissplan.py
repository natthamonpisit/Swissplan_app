st.markdown("""
<style>
.fixed-timeline-line {
    position: fixed;
    top: 0;
    bottom: 0;
    left: 50%;
    width: 6px;
    background-color: pink;
    transform: translateX(-50%);
    z-index: 0;
    height: 100vh;
}
</style>
<div class="fixed-timeline-line"></div>
""", unsafe_allow_html=True)
