import streamlit as st
import mysql.connector
import json
import requests
from streamlit_lottie import st_lottie
import time

def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
def animsucc():
    msg = st.toast('Gathering information')
    time.sleep(2)
    msg.toast('Login successfull', icon = "🥳")
    time.sleep(1)
    st.balloons()

def animunsucc():
    msg = st.toast('Gathering information')
    time.sleep(2)
    msg.toast('Oops! Something went wrong...', icon = "🥞")
    time.sleep(1)


def create_connection():
    return mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="Shreeji@sql2024",
        database="accountdata"
    )

def save_user(email, password, username):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO userdata (email, pass, username) VALUES (%s, %s, %s)", (email, password, username))
    conn.commit()
    cursor.close()
    conn.close()

def authenticate_user(username, password):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM userdata WHERE username = %s AND pass = %s", (username , password))
    user = cursor.fetchone()
    cursor.close()
    conn.close()
    return user is not None

def run():
    lottie_code = load_lottiefile("loginanimation.json")
    st.markdown(
        """
        <style>
        .header {
            position: absolute;
            top: 10px;
            width: 100%;
            text-align: left;
            z-index: 0;
        }
        .animation {
            display: block;
            margin-left: auto;
            margin-right: auto;
            margin-top: 10px;
            width: 50%;
            z-index: 0;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    st.markdown(
        """
        <div style='text-align: left;'>
            <h1>Welcome! Please log in or sign up to continue.</h1>
        </div>
        """, 
        unsafe_allow_html=True
    )
    
    @st.dialog("Sign in to your account", width="large")
    def signin():
        st.write("Sign in")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        if st.button("Login"):
            if username and password:
                if authenticate_user(username, password):
                    animsucc()
                    st.success("Login successful!")
                    time.sleep(2)
                    st.session_state.user = {"username": username, "password": password}
                    st.rerun()
                else:
                    animunsucc()
                    st.error("Invalid username or password")
            else:
                animunsucc()
                st.error("Please enter both username and password")

    @st.dialog("Sign up for a new account", width="large")
    def signup():
        st.write("Sign Up")
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        username = st.text_input("Username")
        
        
        if st.button("Sign Up"):
            if username and email and password:
                save_user(email, password, username)
                st.success("Sign up successful!")
                st.rerun()
            else:
                st.error("Please fill in all fields")

    col1, col2 = st.columns([0.7, 0.3])
    with col1:
        st_lottie(
            lottie_code,
            speed=1,
            reverse=False,
            loop=True,
            quality='high',
            height=550,  # Adjust height
            width=550,   # Adjust width
            key=None,
        )
    
    with col2:
        if "user" not in st.session_state:
            if st.button("Sign in",):
                signin()
            st.write("Already have an account? Please sign in")
            if st.button("Sign up"):
                signup()
            st.write("Don't have an account? Please sign up")

if __name__ == "__main__":
    run()
