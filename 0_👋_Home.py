import streamlit as st
import base64

    
# ----- Page configs (tab title, favicon) -----
st.set_page_config(
    page_title="Kyle Palm Portfolio",
    page_icon="📊",
)


# ----- Left menu -----
with st.sidebar:
    st.image("eae_img.png", width=200)
    st.header("Introduction to Programming Languages for Data")
    st.write("###")
    st.write("***Final Project - Feb 2025***")
    st.write("**Author:** Kyle Palm")
    st.write("**Instructor:** [Enric Domingo](https://github.com/enricd)")


# ----- Top title -----
st.write(f"""<div style="text-align: center;"><h1 style="text-align: center;">👋 Hi! My name is Kyle Palm</h1></div>""", unsafe_allow_html=True)  # TODO: Add your name


# ----- Profile image file -----
profile_image_file_path = "dffo.jpg"       # TODO: Upload your profile image to the same folder as this script and update this if it has a different name

with open(profile_image_file_path, "rb") as img_file:
    img = "data:image/png;base64," + base64.b64encode(img_file.read()).decode()


# ----- Your Profile Image -----
st.write(f"""
<div style="display: flex; justify-content: center;">
    <img src="{img}" alt="Your Name" width="300" height="300" style="border-radius: 50%; object-fit: cover; margin-top: 40px; margin-bottom: 40px;">
</div>
""", unsafe_allow_html=True)


# ----- Personal title or short description -----
current_role = "Master’s student at EAE Business School in Barcelona, specializing in Big Data Analytics"   # TODO: Change this

st.write(f"""<div style="text-align: center;"><h4><i>{current_role}</i></h4></div>""", unsafe_allow_html=True)

st.write("##")    # Adding some space


# ----- About me section -----
st.subheader("About Me")

# TODO: Modify and adapt the following lines to your info, you can add or remove some details if you want
st.write("""
- 🧑‍💻 I am a Student 

- 🛩️ prev: Graduated in 2018 with a Bachelor of Business Administration in Finance and International Business from the University of Cincinnati. Most previously a Senior Consultant at NewGen Strategies and Solutions, specializing in cost-of-service analysis, rate design, and data-driven forecasting for utility clients. Previously served as a Business Manager at Kiewit Corporation, overseeing financial management for multimillion-dollar wastewater projects and leveraging tools like Excel and Power BI to communicate insights effectively.

- ❤️ Interests: Tennis, Travel, Pineapple

- 🤖 Personal Projects: Creating webpages swayingpalms.net

- 📫 How to reach me: kyle.a.palm@gmail.com

- 🏠 Barcelona
""")

# Feel free to add other points like your Linkedin, Github, Social Media, etc.
