import streamlit as st
import home
import login
import toml
from streamlit_option_menu import option_menu
import os

# This must be the first Streamlit command in your script
st.set_page_config(layout="wide", menu_items={
    'About': "# This is a header. This is an *extremely* cool app!"
})
config_path = os.path.join('.streamlit', 'config.toml')
config = toml.load(config_path)

def main():
    # Initialize page and show_animation in session state if not already present
    if 'page' not in st.session_state:
        st.session_state.page = 'home'
    if 'show_home_button' not in st.session_state:
        st.session_state.show_home_button = True
    if 'show_account_button' not in st.session_state:
        st.session_state.show_account_button = True

   
    # Sidebar buttons
    with st.sidebar:
        st.title('DASHBOARD')
        selected = option_menu(
            menu_title=None,
            options=["Home", "Account","About us"],
            icons=["house", "person"],
            menu_icon="cast",
            default_index=0,
        )
        
        
    if selected == "Home":
        st.session_state.page = 'home'
    elif selected == "Account":
        st.session_state.page = 'login'
    elif selected=="About us":
        st.session_state.page='aboutus'

    # Page content
    if st.session_state.page == 'home':
            home.run()
    elif st.session_state.page == 'login':
            login.run()
    elif st.session_state.page == 'aboutus':
            aboutus.run()
    
if __name__ == "__main__":
    main()
