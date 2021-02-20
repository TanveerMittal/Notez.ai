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

def get_model(user):
    if user in get_Users():
        firebase=pyrebase.initialize_app(config.FIREBASE)
        storage=firebase.storage()
        model_path="Users/"+user+"_model"
        local_path=""
        storage.child(model_path).download(local_path)
        return local_path

def put_model(user,model_local_path):
    firebase = pyrebase.initialize_app(config.FIREBASE)
    storage = firebase.storage()
    model_path="Users/"+user+"_model"
    storage.child(model_path).put(model_local_path)

put_model("Rudy")




