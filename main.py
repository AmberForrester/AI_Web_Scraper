import streamlit as st 

st.set_page_config(
    page_title = "AI Web Scraper",
    page_icon = "images/favicon.ico"
)


from scrape import (
    scrape_website, 
    split_dom_content, 
    clean_body_content, 
    extract_body_content
)



st.title("AI Web Scraper")
url = st.text_input("Enter a website URL: ")

# Step 1: Scrape the Website:
if st.button("Scrape Website"):
    if url:
        st.write("Scraping the website...")
    
        dom_content = scrape_website(url)
        body_content = extract_body_content(dom_content)
        cleaned_content = clean_body_content(body_content)
        
        # Store DOM content in Streamlit session state:
        st.session_state.dom_content = cleaned_content
        
        # Display the DOM content in an expandable text box to toggle content: 
        with st.expander("View DOM Content"):
            st.text_area("DOM Content", cleaned_content, height=300)    