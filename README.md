## LLM Powered YouTue Assistant App

The YouTube Assistant created using LangChain Framework allows resolving queries related to the YouTube Video by finding the similarity between the query and the Transcript documents created using the FAISS (Facebook AI Similarity Search) and OpenAI embeddings. 
This project employs OpenAI (text-davinci-003) LLM model. Prompt Templates module are used to train the LLM model using a set template and Youtube Loader Module from LangChain is used to fetch YouTube Transcript. Transcript is split into chunks using Recursive Character Text Splitter module.
The User Interface of App is made using Streamlit.

Step 1: Copy Youtube URL for Any video Available on YouTube.com
![image](https://github.com/rutujakokate430/LLM-Powered-Youtube-Assistant-App-Using-LangChain-Framework-/assets/111034043/05cefaf4-2db2-4c00-a26b-ebd1f43d9c33)

Step 2: Go to the YouTube Assist App and paste the URL and your query related to the Video in appropriate fields and hit Submit Button.
![image](https://github.com/rutujakokate430/LLM-Powered-Youtube-Assistant-App-Using-LangChain-Framework-/assets/111034043/277c8e4d-7e18-42e6-b1df-20be46266a5c)


