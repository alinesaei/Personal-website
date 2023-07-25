import streamlit as st
from PIL import Image


# Set up the webpage
st.set_page_config(page_title="Ali Nesaei's Webpage", page_icon=":memo:", layout="wide")


# Header section
with st.container():
    st.subheader("Hello, I am Ali Nesaei :wave:")
    st.title("A Computer Engineering Graduate From Iran")
    st.write(
        "I am passionate about Natural Language Processing (NLP), Machine Learning, and Data Mining. "
        "Keenly interested in further academic exploration in Computer Science, including Master's or potential Ph.D. programs."
    )
    st.write("[LinkedIn](https://www.linkedin.com/in/alinesaei/) [GitHub](https://github.com/alinesaei)")

# What I do
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Research Interests")
        st.write("##")
        st.write(
            """
            - Natural Language Processing (NLP)
            - Machine Learning
            - Data Mining
            - Computer Vision
            - Medical Imaging
            """
        )
    with right_column:
        st.header("Skills")
        st.write("##")
        st.write(
            """
            - Programming Languages: Python
            - Libraries and Frameworks: Pandas, Numpy, Matplotlib, scikit-learn, OpenCV, Keras, TensorFlow, NLTK, spaCy
            - Databases: SQL Server, MySQL
            - Dev Tools: Visual Studio Code, Git, Docker
            - Mathematical and Statistical Skills: Statistics, Algebra, Calculus
            - Operating Systems: Linux, Windows
            """
        )

# Projects
with st.container():
    st.write("---")
    st.header("Academic Projects")
    st.write("##")
    with st.container():
        st.subheader("Smart Presentation Generator and Summarizer")
        st.write(
            """
            A project that utilizes GPT-3.5 to generate content for user input and converts it into a PowerPoint presentation.
            Users can select templates and customize the content's difficulty level (Hard, Medium, Easy).
            """
        )
        st.markdown("[GitHub Repo](https://github.com/alinesaei/ppt-generator)")
    with st.container():
        st.subheader("Gold Price Prediction using ARIMA model")
        st.write(
            """
            Developed a small project for predicting gold prices using the ARIMA model.
            """
        )
        st.markdown("[GitHub Repo](https://github.com/alinesaei/gold-price-arima-prediction)")

# Contact
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/nesaeialii@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
