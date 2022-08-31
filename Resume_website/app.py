from pathlib import Path
from tkinter import Image
from turtle import st

import streamlit as st
from PIL import Image

# ----- Settings----
current_dir = Path(__file__).parent if "__file" in locals() else Path.cwd()
css_file = current_dir/"styles"/"main.css"
resume_file = current_dir/"assets"/"resume.pdf"
profile_pic = current_dir/"assets"/"profile-pic.png"

# --- GENERAL SETTINGS ---
PAGE_TITLE = "ChaitanyaBharadwaj"
PAGE_ICON = ":wave:"
NAME = "M.V.Chaitanya Bharadwaj"
DESCRIPTION = """
I am M.V.Chaitanya Bharadwaj. I am pursuing my bachelor’s from Kalasalingam Academy of Research and Education.
I am knowledgeable in Python programming languages and good at problem-solving, analysis, Data visualization, and Image processing. I have Solved different case studies in the business field.
I have also Worked on development Projects and made Some cool and Useful Projects on Web Development and AI.
"""
EMAIL = "venkatachaitanyametta@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/metta-venkata-chaitanya-bharadwaj-bb814b208/",
    "GitHub": "https://github.com/mvcb",
    "Twitter": "https://twitter.com/Chaitanya_metta",
    "Instagram": "https://www.instagram.com/cchaitanya_bharadwaj/"
}
PROJECTS = {
    "🏆 Movie Recommendation System": "https://github.com/mvcb/collaborative-filtering-movelens-100k-dataset",
    "🏆 Human Pose Estimation": "https://github.com/mvcb/MediaPipePoseEstimation",
    "🏆 Weather prediction": "https://github.com/mvcb/Weather_predictions_app",
}



st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)
with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write("#")
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write("#")
st.subheader("EDUCATION")
st.write(
"""
 ✔️ Kalasalingam Academy of Research and Education, India""")  
st.write("B.Tech Computer Science Engineering, June 2024")
st.write("Coursework: Data Structures, Design, and Analysis of Algorithms, Operating System, Machine learning.")

# --- SKILLS ---
st.write("#")
st.subheader("Techinical Skills")
st.write(
"""
- 👩‍💻 Programming Languages: Python (Proficient), C++.
- 💻 Framework:  Flask, TensorFlow
- 💻 Frontend: HTML5, CSS3, Bootstrap, JS.
- 📊 Data Science: NLP, Standard ML Algorithms (Regression, Classification, Clustering), Deep learning 
- 📊 BI Tools: Tableau
- 📚 Libraries: Numpy, Pandas, Matplotlib, Seaborn, NLTK, Sci-kit learn, Open CV.
"""
)


# --- WORK HISTORY ---
st.write("#")
st.subheader("Work Experience")
st.write("---")

#--- JOB 1
st.write("🚧", "**Virtual Experience at Accenture developer program**")
st.write(
    """
- ► I have completed the Virtual Accenture developer program and gained some skills.
"""
)


# --- Projects  ---
st.write("#")
st.subheader("Projects")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")

st.write("#")
st.subheader("ACHIEVEMENTS")
st.write("• Student Coordinator at OSS (Open Source Society)")
st.write("• Student member at Google Student Developer Club")
st.write("• 5-star python coder at hackerrank.")


