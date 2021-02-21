import pyrebase
import config

def get_Users():
    firebase=pyrebase.initialize_app(config.FIREBASE)
    db = firebase.database()
    users = db.child("Users").get()
    return dict(users.val())

def update_Users(user):
    firebase = pyrebase.initialize_app(config.FIREBASE)
    db = firebase.database()
    db.child("Users").update({user: 0})

def get_transcript(user,model_local_path):
    if user in get_Users():
        firebase=pyrebase.initialize_app(config.FIREBASE)
        storage=firebase.storage()
        model_path="Users/"+user+"_transcript"
        storage.child(model_path).download(model_local_path)

def put_transcript(user,model_local_path):
    update_Users(user)
    firebase = pyrebase.initialize_app(config.FIREBASE)
    storage = firebase.storage()
    model_path="Users/"+user+"_transcript"
    storage.child(model_path).put(model_local_path)





