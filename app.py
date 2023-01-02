import streamlit as st
from pathlib import Path
from PIL import Image
from datetime import date

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "anupan_cv.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"

#-------------------- General Setting ---
PAGE_TITLE = "Digital CV | Anupan Sueppeng"
PAGE_ICON = ":wave:"
NAME = "Mr. Anupan Sueppeng"
DESCRIPTION = "Product Development"
EMAIL = "aps.bk201@gmail.com"
GITHUB = "https://github.com/apsbk201"

EXPERIENCE = """
ความรับผิดชอบ :
- ⏺ ️ออกแบบโปรแกรมควบคุมการทำงาน 
- ⏺ ️ออกแบบวงจรอิเล็คทรอนิกส์
- ⏺ อ️อกแบบโครงสร้างเครื่อง
- ⏺ จัดทำเอกสารการใช้งานเครื่อง
- ⏺ ดูแลระบบคอมพิวเตอร์ของบริษัท
"""
SKILLS = """
💻 คอมพิวเตอร์
- ⏺ Windows สามารถใช้งานพื้นฐาน และติดตั้งโปรแกรมได้
- ⏺ Linux สามารถติดตั้งระบบปฏิบัติการ งานพื้นฐาน samba share, backup files
🛠️ โปรแกรม
- ⏺ MS Word, MS Excel 
- ⏺ Arduino สามารถใช้งานไมโครคอนโทรเลอร์ ส่งข้อมูลไปยังชุดหน้าจอ Nextion ได้
- ⏺ Nextion สามารถออกแบบหน้าจอควบคุมและแสดงผล
- ⏺ Photoshop CS6 สามารถตัดต่อ ตกแต่งรูปภาพขั้นพื้นฐาน
- ⏺ Altium Designer สามารถออกแบบวงจรในระดับ 2 layer สร้าง footprint ของอุปกรณ์ได้
- ⏺ SolidWorks สามารถออกแบบโครงสร้าง 3D model และ drawing
- ⏺ Python 
	- ⏺ streamlit สร้างเว็ปไซต์อย่างง่าย
	- ⏺ sqlite3 สร้างฐานข้อมูลอย่างง่าย ใช้งานผ่าน web browser และ สร้างเป็นไฟล์ Excel
"""

STUDY = """
🎓 การศึกษา
- ปริญญาตรี คณะ วิศวกรรมศาสตร์
- สาขาเอก วิศวกรรมเมคคาทรอนิกส์
- 2556, มหาวิทยาลัยมหาสารคาม GPA 2.68
"""
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

#---------- Load css file etc
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file,"rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

column1, column2 = st.columns(2, gap="small")
with column1:
    st.image(profile_pic, width=230)

with column2:
    st.title("อนุพันธ์ สืบเพ็ง")
    st.subheader(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label= " 📥 Download Resume",
        data= PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write(" 📧️ ",EMAIL)
    st.write(" 😺 ", GITHUB)

with st.container():
    try:
        begin = date(2015, 9, 1)
        noww = date.today()
        if noww.month < begin.month:
            m = (noww.month + 12) - begin.month
            y = (noww.year - 1) - begin.year
        else:
            m = noww.month - begin.month
            y = noww.year - begin.year
    except:
        pass
    st.subheader(f'ประสบการณ์ในการทำงาน : {y} ปี {m} เดือน')
    st.write("บริษัท เซนนิเทค จำกัด")
    st.write("ธุรกิจของบริษัท : ผลิตเครื่องส่องไฟรักษาภาวะตัวเหลืองในทารกแรกเกิด")
    st.write("ตำแหน่งล่าสุด : ออกแบบและพัฒนาผลิตภัณฑ์ และช่างเทคนิค")
    st.write(EXPERIENCE)

with st.container():
    st.subheader("ทักษะประสบการณ์")
    st.write(SKILLS)

with st.container():
    st.subheader("การศึกษา")
    st.write(STUDY)