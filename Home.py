import streamlit as st
import pandas as pd
from pymongo import MongoClient, DESCENDING
from difflib import unified_diff
from hashlib import sha256
from difflib import ndiff
import re
import streamlit_authenticator as stauth

st.set_page_config(layout="wide", page_title="News Monitor App")

# The connection string, database name, and collection name
connection_string = "mongodb+srv://" + st.secrets["DB_USERNAME"] + ":" + st.secrets["DB_PASSWORD"] + "@" + st.secrets["DB_CLUSTER"] + ".lppvfjw.mongodb.net/"
database_name = st.secrets["DB_NAME"]
collection_name = st.secrets["DB_COLLECTION"]

# Create a MongoClient
client = MongoClient(connection_string)

# Access the specified database and collection
db = client[database_name]
collection = db[collection_name]

with st.sidebar:
    st.title("News Monitor :memo:")
    st.caption("""The News Monitor is a cutting-edge platform designed to continuously monitor and analyze content from news media platforms. 
               It automatically detects updates in articles, highlighting any additions or deletions made to the content. Moreover, 
               it utilizes Generative AI technology to generate insights and facilitate interactive Q&A sessions based on the articles.""")

st.title("News Monitor :memo:")
# st.image("scrape.jpg")
st.write("The News Monitor is a cutting-edge platform designed to continuously monitor and analyze content from news media platforms. It automatically detects updates in articles, highlighting any additions or deletions made to the content. Moreover, it utilizes Generative AI technology to generate insights and facilitate interactive Q&A sessions based on the articles.")

# Function to split text into paragraphs of up to 5 lines
def split_into_paragraphs(text):
    sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', text)
    paragraphs = [' '.join(sentences[i:i+5]) for i in range(0, len(sentences), 5)]
    return paragraphs


news_source = st.selectbox("Choose the news source", ("The Wire", "BBC", "Alt News", "India Today"), help="Pick the news source of the data you want")

input_option = st.radio("Choose the number of articles to display.", [2, 10, 20, 50], help="Number of articles you want to see")
submit_button = st.button("Submit")
st.divider()

if submit_button:
    # Database query to fetch all the links of Global Times
    articles = collection.find({"source": news_source}).sort("counter", DESCENDING).limit(input_option)
    # print(result)
    documents_list = list(articles)
    
    for fc_no, document in enumerate(documents_list, 1):
        st.header(document['title'])
        try:
            st.caption(document['description'])
        except:
            pass
        col1, col2 = st.columns(2)
        try:
            if len(document['author']) != 0:
                author = document['author']
            else:
                author = document['source']
        except:
            author = document['source']
            
        try:
            counter = int(document['counter'])
        except:
            counter = 0
        
        with col1:
            st.write("By: " + author)
            # st.write(document['link'])
            st.link_button("Article Link", document['link'])
        with col2:
            st.write("Date: " + document['date'].strftime("%d-%m-%Y"))

        if counter > 0:
            # Display the articles in two columns
            tab1, tab2 = st.tabs(['Old version', 'New version'])

            with tab1:
                for paragraph in split_into_paragraphs(document['content']):
                    st.write(paragraph)
            
            try:
                with tab2:
                    updated_paragraphs = []
                    diff = ndiff(document['content'].split(), document['updated_content'].split())
                    for word in diff:
                        if word.startswith('+'):
                            updated_paragraphs.append(f'<span style="color: green;">{word[2:]}</span>')
                        elif word.startswith('-'):
                            updated_paragraphs.append(f'<span style="color: red;">{word[2:]}</span>')
                        else:
                            updated_paragraphs.append(word[2:])
                    updated_article_with_color = ' '.join(updated_paragraphs)
                    for paragraph in split_into_paragraphs(updated_article_with_color):
                        st.write(paragraph, unsafe_allow_html=True)
            except:
                pass
        else:
            for paragraph in split_into_paragraphs(document['content']):
                st.write(paragraph)

        st.divider()

