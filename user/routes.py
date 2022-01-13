from flask import Flask
from app import app
from user.models import User

@app.route('/user/signup/', methods=['POST'])
def signup():
	return User().signup()

@app.route('/user/signout/')
def signout():
	return User().signout()

@app.route('/user/login', methods=['POST'])
def login():
	return User().login()

@app.route('/user/sign_up/')
def sign_up():
	return User().sign_up()


@app.route('/confirm_email/<token>')
def confirm_email(token):
	return User().confirm_email(token)

@app.route('/email_verification/')
def email_verification():
	return User().email_verification()