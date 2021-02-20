from flask import Flask, request


backend = Flask(__name__)
backend.config.from_object("config")

# For Rudy: should be translated to localhost:5000/receive-transcript
# can be tested on windows cmd with command:
# curl -X POST -H "Content-Type:application/json" -d "{\"transcript_data\":\"Hello\",\"file_extension\":\"World\"}" localhost:5000/receive-transcript
@backend.route('/receive-transcript',methods=['POST'])
def get_transcript():
    print(request.json["transcript_data"])
    print("\n\n\n")
    print(request.json["file_extension"])
    return "Success"



if __name__ == '__main__':
    if backend.config['DEBUG']:
        backend.debug = True
        backend.run()