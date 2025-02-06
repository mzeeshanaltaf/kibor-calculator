# Import libraries
import streamlit as st

# --- PAGE SETUP ---
main_page = st.Page(
    "main.py",
    title="AutoCompensate",
    icon=":material/directions_car:",
    default=True,
)

faq_page = st.Page(
    "faqs.py",
    title="FAQs",
    icon=":material/help:",
)


pg = st.navigation({
    "Home": [main_page],
    "About": [faq_page],
                    })

pg.run()