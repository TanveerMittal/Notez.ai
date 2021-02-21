import streamlit as st
import streamlit.components.v1 as stc
import pandas as pd

def dummy():
   return eval(open('example.txt', "r").read())

def parse():
   model_dict = dummy()
   i = 1
   for key in model_dict.keys():
      st.markdown("# Section %d:"%i)

      cur_val = model_dict[key]
      questions = cur_val['questions']

      summary = cur_val['summaries']
      st.markdown('### Summary:')
      st.markdown(summary)
      for question in questions:
         ques = question['question']
         ans = question['answer']
         print(ques, ans)




def main():
   st.title("CoolScript")

   #menu = ["Upload", "Data", "About"]
   #choice = st.sidebar.selectbox("Menu", menu)

   #if choice == "Upload":
   file = st.file_uploader("Upload File", type=['txt', 'vtt'])
   st.markdown('cringe')
   if st.button("Process"):
      if docx_file is not None:
         file_details = {"Filename": file.name, "FileType": file.type, "FileSize": file.size}
         st.write(file_details)
         # Check File Type
         if file.type == "text/plain":
            # raw_text = docx_file.read() # read as bytes
            # st.write(raw_text)
            # st.text(raw_text) # fails
            st.text(str(file.read(), "utf-8"))  # empty
            raw_text = str(file.read(), "utf-8")  # works with st.text and st.write,used for futher processing
            # st.text(raw_text) # Works
            st.write(raw_text)  # works
         elif file.type == "text/vtt":
            st.text(str(file.read(), "utf-8"))  # empty
            raw_text = str(file.read(), "utf-8")  # works with st.text and st.write,used for futher processing
   df = dummy()
   st.dataframe(df)




if __name__ == '__main__':
   main()
