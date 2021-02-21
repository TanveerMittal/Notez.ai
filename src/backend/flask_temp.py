from flask import Flask
from flask_cors import CORS

app = Flask("__main__")
CORS(app)

@app.route("/receive-transcript/<data>/<extension>")
def compile(data, extension):
    print(data)
    print(extension)
    return 'Success'

app.run(debug=True)