import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', '44056c242169e92244116b3c59055e28')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgres://iameych77:Zkic3xh6o6rNpxqetnb78xdVh3uxG16y@dpg-cp7mv4md3nmc73buv780-a/cocktail_database_lw3l')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
