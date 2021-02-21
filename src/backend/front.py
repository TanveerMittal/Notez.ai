import re
import streamlit as st
import streamlit.components.v1 as stc
import pandas as pd
from nlp import run_pipeline, get_teacher_text, filter_vtt, init_models

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
         qa_markdown = """
         * **Question %d**: %s
            * **Answer:** %s"""

         st.markdown(qa_markdown % (j+1, question, ans))




def main():
   st.title("Working Title")

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
         file_details = {"Filename": file.name, "FileType": file.type, "FileSize": file.size}
         st.write(file_details)

         doc = None
         # Check File Type
         if file.type == "text/plain":
            st.text(str(file.read(), "utf-8"))
            raw_text = str(file.read(), "utf-8")  
            st.write(raw_text)
            if len(re.findall(r"[a-zA-Z]:", raw_text)) > 0:
               doc = get_teacher_text(raw_text)

         elif file.type == "text/vtt":
            st.text(str(file.read(), "utf-8")) 
            raw_text = str(file.read(), "utf-8") 
            doc = filter_vtt(raw_text)

         else:
            st.text("ERROR: INVALID FILE FORMAT")
      
         print(raw_text)
         parse(dummy())


if __name__ == '__main__':
   init_models()
   main()
