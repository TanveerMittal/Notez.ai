from flask import Flask
from flask_cors import CORS

app = Flask("__main__")
CORS(app)

@app.route("/receive-transcript/<data>/<extension>/<user>")
def compile(data, extension, user):
    print(data)
    print(extension)
    print(user)
    return 'Success'

app.run(debug=True)