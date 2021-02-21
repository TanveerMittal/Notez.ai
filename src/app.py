import re
import streamlit as st
import streamlit.components.v1 as stc
import pandas as pd
from nlp import nlp_pipeline, get_teacher_text, filter_vtt, init_models

def dummy():
   return eval(open('example_output.txt', "r").read())

def parse(model_dict):
   #model_dict = dummy()
   for i, key in enumerate(model_dict.keys()):
      st.markdown("# Section %d:" % (i+1))

      cur_val = model_dict[key]
      questions = cur_val['questions']
      summary = cur_val['summaries']

      st.markdown('### Summary:')
      st.markdown(summary)

      for j, qa in enumerate(questions):
         question = qa['question']
         ans = qa['answer']
         a_markdown = """Answer: %s"""
         q_markdown = """
         Question %d: %s"""
         with st.beta_expander(q_markdown % (j+1, question)):
            #st.markdown(a_markdown % (ans))
            st.write(a_markdown %(ans))




def main():
   global toggle
   st.title("Notez.ai")
   st.subheader("Created by Team Beeg Data")
   st.subheader("Team Members: Tanveer Mittal, George Pu, Rudy Thurston, and Jonathan Xiong")
   st.subheader("Upload a Zoom lecture transcript to get a personalized study guide created by artifical intelligence!")
   st.subheader("")
   #menu = ["Upload", "Data", "About"]
   #choice = st.sidebar.selectbox("Menu", menu)

   #if choice == "Upload":
   file = st.file_uploader("Upload File", type=['txt', 'vtt'])
   sli1, sli2 = st.beta_columns(2)
   with sli1:
      n_topics = st.slider('# of Topics to Extract', min_value=1, max_value=15)
   with sli2:
      n_questions = st.slider('# of Questions per Topic', min_value=1, max_value=10)
   #st.markdown('cringe')
   if st.button("Process"):
      if file is not None:
         #file_details = {"Filename": file.name, "FileType": file.type, "FileSize": file.size}
         #st.write(file_details)

         doc = None
         # Check File Type
         if file.type == "text/plain":
            raw_text = str(file.read(), "utf-8")  
            if len(re.findall(r"[a-zA-Z]:", raw_text)) > 0:
               doc = get_teacher_text(raw_text)

         elif file.type == "text/vtt":
            raw_text = str(file.read(), "utf-8") 
            doc = filter_vtt(raw_text)

         else:
            st.text("ERROR: INVALID FILE FORMAT")
      
         if doc is not None:
            model_output = nlp_pipeline(doc, n_topics, n_questions)
            parse(model_output)



if __name__ == '__main__':
   #init_models()
   main()
