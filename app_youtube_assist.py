#from key import openai_api_key
import os
os.environ['OPENAI_API_KEY']="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"

import streamlit as st
from langchain.document_loaders import YoutubeLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings  #Embeddings are a measure of the relatedness of text strings, and are represented with a vector (list) of floating point numbers.
from langchain.vectorstores import FAISS 
from langchain.llms import OpenAI # Meta's FAISS for vector similarity search. A vector store takes care of storing embedded data and performing vector search for you.
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import textwrap
embeddings=OpenAIEmbeddings()

#video_url= "https://www.youtube.com/watch?v=1p6P471PBx0"
def create_db_from_youtube_video_url(video_url: str) -> FAISS:
     loader=YoutubeLoader.from_youtube_url(video_url)
     transcript=loader.load()

     text_splitter= RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
     docs=text_splitter.split_documents(transcript)

     db = FAISS.from_documents(docs, embeddings)
     return db


def get_response_from_query(db, query, k=4):
     # text-devinci can handle only 4097 tokens
     docs = db.similarity_search(query, k=k)
     docs_page_content=" ".join([d.page_content for d in docs])

     llm=OpenAI(model_name="text-davinci-003")

     prompt= PromptTemplate(input_variables=["question", "docs"],
                             template="""
                             You are a helpful Youtube Assistant that can answer questions about videos based on the video's transcript.
                             Answer the following question: {question}
                             By searching the following video transcript: {docs}
                             Only use the factual information from the transcript to answer the question.
                             If you feel like you dont have enough information to answer the question, say "I dont know".
                             Your answers should be detailed.""",
                            )
     chain= LLMChain(llm=llm, prompt=prompt) 
     response= chain.run(question=query, docs=docs_page_content)
     response= response.replace("\n", " ")
     return response, docs
     
st.title("🎥📜🔎YouTube Assistant")

with st.sidebar:
    with st.form(key='my_form'):
        youtube_url = st.sidebar.text_area(
            label="What is the YouTube video URL?",
            max_chars=50
            )
        query = st.sidebar.text_area(
            label="Ask me about the video?",
            max_chars=50,
            key="query"
            )
        submit_button= st.form_submit_button(label="Submit")
        

if query and youtube_url:
        db = create_db_from_youtube_video_url(youtube_url)
        response, docs = get_response_from_query(db, query)
        st.subheader("Answer:")
        st.text(textwrap.fill(response, width=85))


