The YouTube Assistant created using LangChain Framework allows resolving queries related to the YouTube Video by finding the similarity between the query and the Transcript documents created using the FAISS (Facebook AI Similarity Search) and OpenAI embeddings. 
This project employs OpenAI (text-davinci-003) LLM model. Prompt Templates module are used to train the LLM model using a set template and Youtube Loader Module from LangChain is used to fetch YouTube Transcript. Transcript is split into chunks using Recursive Character Text Splitter module.
The User Interface of App is made using Streamlit.

![image](https://github.com/rutujakokate430/LLM-Powered-Youtube-Assistant-App-Using-LangChain-Framework-/assets/111034043/bdba7d6f-64aa-4867-929e-6bf7f2791c02)

