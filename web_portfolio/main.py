import streamlit as st
import read_csv as rcsv

projects = rcsv.read_projects_file()

st.set_page_config(layout="wide")
col1, col2 = st.columns(2)
with col1:
    st.image("static/photo.webp", width=300)

with col2:
    st.title("Riccardo Inojosa")
    content = """
        I am a dedicated Python developer with a strong passion for coding and problem-solving. With expertise in building robust and scalable applications, I have experience in various domains including web development, data analysis, and automation. My skill set includes proficiency in frameworks like Django and Flask, as well as a solid understanding of libraries such as Pandas and NumPy. I am committed to writing clean, efficient code and continuously improving my skills to stay updated with the latest industry trends.
    """
    st.write(content)

st.write("Feel free to contact me if you need a developer for your project.")

col3, col4 = st.columns(2)

def projectLayout(col):
    with col:
        st.header(project["title"])
        st.write(project["description"])

for index, project in enumerate(projects):
    if (index + 1) % 2 == 0:
        projectLayout(col4)
    else:
        projectLayout(col3)
            