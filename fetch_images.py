import pandas as pd
from duckduckgo_search import DDGS

# โหลดไฟล์แผนเที่ยว
plan_df = pd.read_excel("Plan/Swiss_plan_app.xlsx")

# ดึง destination ที่ไม่ซ้ำ
destinations = plan_df["Destination"].dropna().unique()

# เตรียม DataFrame สำหรับเก็บผลลัพธ์
result_rows = []

for dest in destinations:
    # ค้นหารูป 3 รูปแรก
    with DDGS() as ddgs:
        results = list(ddgs.images(dest, max_results=3))
    image_urls = [r["image"] for r in results[:3]]
    # เติมให้ครบ 3 ช่อง (ถ้าผลลัพธ์น้อยกว่า 3)
    while len(image_urls) < 3:
        image_urls.append("")
    result_rows.append({
        "Destination": dest,
        "ImageURL1": image_urls[0],
        "ImageURL2": image_urls[1],
        "ImageURL3": image_urls[2],
    })

# สร้าง DataFrame และบันทึกเป็น Excel
result_df = pd.DataFrame(result_rows)
result_df.to_excel("Plan/destination_images.xlsx", index=False)
print("สร้างไฟล์ Plan/destination_images.xlsx เรียบร้อยแล้ว")
