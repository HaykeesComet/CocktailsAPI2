import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'your_secret_key')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgres://gfrjfrokrvkzli:a97dfdf6741050752abe67fbf77db45bcb0d7ee5f5be61ff1dc6b473e1c29623@ec2-54-144-112-84.compute-1.amazonaws.com:5432/d80985on3d68kp')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
