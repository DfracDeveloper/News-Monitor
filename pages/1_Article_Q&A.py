import streamlit as st
import pandas as pd
from pymongo import MongoClient, DESCENDING
from difflib import unified_diff
from hashlib import sha256
from difflib import ndiff
import re
import streamlit_authenticator as stauth
from datetime import datetime

st.set_page_config(layout="wide", page_title="News Monitor App")

# The connection string, database name, and collection name
connection_string = "mongodb+srv://admin:Newsscraper123@newsscraper.lppvfjw.mongodb.net/"
database_name = "NewsScrapper"
collection_name = "Articles"

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
st.write("The News Monitor is a cutting-edge platform designed to continuously monitor and analyze content from news media platforms. It automatically detects updates in articles, highlighting any additions or deletions made to the content. Moreover, it utilizes Generative AI technology to generate insights and facilitate interactive Q&A sessions based on the articles.")

st.header("Article Question and Answers")
st.text("Coming Soon...")
# left, right = st.columns(2)
# with left:
#     news_source = st.radio("Choose the news source", ("The Wire", "Alt News", "India Today"), help="Pick the news source of the data you want")
# with right:
#     published_date = st.date_input("Date of the Published News", max_value=datetime.today(), format="DD/MM/YYYY", help="Choose the published date of the News")

# if published_date:
#     # Convert the date object to datetime object
#     date_obj_with_time = datetime.combine(published_date, datetime.min.time())
#     query = {"source": news_source, "date": date_obj_with_time}
#     results = collection.find(query, {"title": 1})
#     article_titles = [doc["title"] for doc in results]
#     if article_titles:
#         st.selectbox("Pick the news", article_titles)
#         st.text_input("Ask something about the article", placeholder="Can you give me a short summary?")
#     else:
#         st.error("No article published in the selected date")

# if st.button("Submit"):
#     st.write("slider", "checkbox")





        
    # query = {"source": news_source, "date": published_date}
    # print(query)
    # result = collection.find_one(query)
    # st.write(query)

    # news_title = st.selectbox("Pick the news", ["Bye", "Hello"])