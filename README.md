# Notez.ai
## SDHacks 2021 Notable Hack Award Winner
**Team Members:** Tanveer Mittal, George Pu, Rudy Thurston, and Jonathan Xiong

[**App Demo**](https://youtu.be/bXeEiYyqSSU)
[**Elevator Pitch**](https://youtu.be/sqAoBTxJLAM)

## Inspiration
The transition to online classes has, contrary to expectations, increased the average time spent for classes. Professors tend to increase course material since it’s easier to create and upload everything online. To improve studying efficiency, we decided to tackle a major part of our long study times and comprehension ability: Zoom lectures. We thought it’d be nice if we could somehow condense lecture material without losing comprehension and possibly even increasing our understanding. Thus, we decided to create an AI that can precisely condense our lectures and generate supplementary content.

## What it does
Notez.ai takes in a lecture transcript and generates topic questions, answers, and summaries. First, Notez.ai accepts transcript files in text or vtt (video text tracks) form and performs some preprocessing to remove unimportant details, such as greetings and pleasantries, as these details have no impact on course content. Then, we apply our machine learning algorithms to the preprocessed text to generate questions and answers while segmenting the text into topics for further summarization with other models. We allow the user to specify any number of topics and questions to generate for view.

## How We Built it
To create our web app we used the Streamlit framework. Despite making steady progress with our React frontend implementation, pivoting to Streamlit and building from scratch proved to be better than continuing with React. Doing so, shortened our program size, made our data visualization more user-friendly, and allowed our implementation to be Flask-free. Our backend and ML pipeline was built through a combination of open-source libraries on Python. We used a Latent Dirichlet Allocation (LDA) model implemented in the Gensim library to perform topic modeling and cluster sentences from a lecture transcript by topics detected by the model. We then took the top k sentences from each topic cluster and used a Bi-Directional Encoding Representation (BERT) model to generate question and answer pairs. We found that many of the generated questions were also not coherent, so we also used a GPT-2 language model to score the coherence of each question-answer pair and filter out incoherent questions and answers. Finally, for each cluster, we took the top 10 sentences and summarized them using another BERT model implemented in the HuggingFace Transformers library. These summaries and questions are passed to our front-end built-in Streamlit and parsed for final presentation.

## Challenges We Ran Into
At first, we tried building the user interface with JavaScript React and making the machine learning models with Python Tensorflow, communicating with Python Flask as the server. However, we ran into a couple of walls, such as cross-origin resource sharing errors when sending HTML requests between JavaScript and Python Flask. From this and additional overhead, we ended up transitioning to using Python and Streamlit for the user interface. Other challenges on the backend were our NLP pipeline and models, which faced issues due to the limited and unstructured data. We circumvented these challenges by leveraging topic-level structure through modeling the text data and other forms. 

## Accomplishments
We were able to integrate the raw lecture transcripts, preprocess the text, and create structured output for several tasks. In particular, we organized the text into the user indicated amount of topics and used natural language processing models to probabilistically output the most relevant summary. Additionally, our model generated several question and answer pairs from the text, which we integrated within our frontend to act as custom quizzes on relevant concepts.

## What We learned
Although machine learning isn’t perfect, it has progressed to the point of being able to accomplish great tasks. For instance, we were able to demonstrate the capability to meaningfully use the transcript data and create a model to think and act like a tutor. In addition, we were able to pick up several python libraries like Streamlit and deploy our application.

## Whats next for Notez.ai
From the current performance of our ML models, we saw that there were several areas that we could improve on for better accuracy and generation. For example, we can train our models on a larger corpus for a similar subject, which can supplement the limitations of using our current data. In addition, we want to create a better organizational structure for our summaries, which involves further models to better structure and represent the topics within the text. We can also improve visual components for a more interactive and iterative question and answering workflow. 
