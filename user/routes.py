from flask import Flask
from app import app
from user.models import User

@app.route('/user/sign_up/',methods=['POST'])
def sign_up():
    user = User()
    return user.sign_up()
