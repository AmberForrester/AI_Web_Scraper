import streamlit as st 


st.title("AI Web Scraper")
url = st.text_input("Enter a website URL: ")

if st.button("Scrape Site"):
    st.write("Scraping the website...")