from flask import Flask, request
import re
from Transcript_Filter import filter_vtt, filter_txt
from waitress import serve
from firebase_communicator import get_transcript, put_transcript
from nlp import run_pipeline

backend = Flask(__name__)
backend.config.from_object("config")

# For Rudy: should be translated to localhost:5000/receive-transcript
# can be tested on windows cmd with command:
# curl -X POST -H "Content-Type:application/json" -d "{\"transcript_data\":\"Hello\",\"file_extension\":\"World\"}" 47.155.248.89:8080/receive-transcript
@backend.route('/receive-transcript')
def receive_transcript():
    with open("temp.txt",'w') as file:
        file.write(request.headers["transcript_data"])
    put_transcript(request.headers["user"],"temp.txt")
    return "Received"

@backend.route("/generate-questions")
def generate_questions():
    get_transcript(request.headers["user"],"temp.txt")
    data = ''
    with open("temp.txt",'r') as file:
        data=file.read()
    return run_pipeline(data,request.headers["topics"],request.headers["questions"])

def filter_transcript(transcript_data, file_extension):
    if file_extension == "vtt":
        transcript_data = filter_vtt(transcript_data)

    elif file_extension == "txt":
        pass




if __name__ == '__main__':
    if backend.config['DEBUG']:
        backend.debug = True
        backend.run()
    else:
        serve(backend, host='0.0.0.0',port=8080,threads=1)