import streamlit as st 

st.set_page_config(
    page_title = "AI Web Scraper",
    page_icon = "images/favicon.ico"
)


from scrape import scrape_website


st.title("AI Web Scraper")
url = st.text_input("Enter a website URL: ")

if st.button("Scrape Site"):
    st.write("Scraping the website...")
    result = scrape_website(url)
    print(result)