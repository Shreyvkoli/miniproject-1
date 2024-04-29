from app import app
from flask_mail import Mail, Message
import os

app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'milksonmark88@gmail.com'

app.config['MAIL_PASSWORD'] =  'jzop lakj cfqt khgz'
mail = Mail(app)


def send_otp(email, otp):
    msg = Message('OTP for your account', sender='milksonmark88@gmail.com', recipients=[email])
    msg.body = f'Your OTP is {otp}'
    
    mail.send(msg)
