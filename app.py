import streamlit as st
from langchain.llms import CTransformers

def getLLamaresponse(input_text, no_words, blog_style):
    # Corrected LLama model initialization
    model_path = r'C:\Users\shubh\OneDrive\Pictures\Blog_generationapp\model\llama-2-7b-chat.ggmlv3.q8_0.bin'
    llm = CTransformers(model=model_path, model_type='llama', config={'max_new_tokens': 256, 'temperature': 0.01})
    
    # Construct prompt template
    prompt_template = f"Write a blog for {blog_style} job profile for a topic {input_text} within {no_words} words."
    
    # Generate the response from LLama 2 model
    response = llm(prompt_template)
    return response

st.set_page_config(page_title="Generate Blogs", layout='centered', initial_sidebar_state='collapsed')

st.header("Generate Blogs")

input_text = st.text_input("Enter the Blog topic")

col1, col2 = st.columns([5, 5])

with col1:
    no_words = st.text_input('No of Words')

with col2:
    blog_style = st.selectbox('Writing the blog for', ('Researchers', 'Data Scientist', 'Common people'), index=0)

submit = st.button("Generate")

if submit:
    st.write(getLLamaresponse(input_text, no_words, blog_style))
