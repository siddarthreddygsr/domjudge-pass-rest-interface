from flask import Flask, jsonify, request
import uuid
from passlib.hash import pbkdf2_sha256
from app import db

class User():

    def sign_up(self):
        user = {
            "_id": uuid.uuid4().hex,
            "username": request.form.get('username'),
            "email": request.form.get('email'),
            "password": request.form.get('password')
           
        }
        
        confirm_password = request.form.get('confirm-password')
        if user['password'] != confirm_password:
            return jsonify({'error': 'Passwords do not match'}), 400
        user['password'] = pbkdf2_sha256.hash(user['password'])

        if db.users.find_one({'email': user['email']}):
            return jsonify({'error': 'email already exists'}), 400

        if db.users.insert_one(user):
            return jsonify(user), 200
        return jsonify({"error":"Sign up Failed"}) , 400
