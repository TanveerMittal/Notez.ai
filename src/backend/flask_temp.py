<<<<<<< HEAD
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

=======
from flask import Flask
from flask_cors import CORS

app = Flask("__main__")
CORS(app)

@app.route("/receive-transcript/<data>/<extension>")
def compile(data, extension):
    print(data)
    print(extension)
    return 'Success'

>>>>>>> 7c5b7195fd7a45176a7d74b112ba061f8b0864f0
app.run(debug=True)