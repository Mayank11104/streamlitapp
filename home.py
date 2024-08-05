
import json
import requests
import streamlit as st
from streamlit_lottie import st_lottie
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def run():
    st.markdown(
        """
        <div style='text-align: left;'>
            <h1>Home Page</h1>
        </div>
        <style>
        @media (max-width: 768px) {
            .animation {
                max-width: 300px;
            }
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    lottie_code = load_lottiefile("homeanimation.json")
    col1, col2 = st.columns([0.8,0.2])
    with col1:
            st_lottie(
            lottie_code,
            speed=1,
            reverse=False,
            loop=True,
            quality='high',
            height=None,  # Adjust height
            width=None,   # Adjust width
            key=None,
        )
   

if __name__ == "__main__":
    run()
