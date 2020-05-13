import os
import secrets
from PIL import Image
from flask import url_for, current_app
from flask_mail import Message
from flaskblog import mail



def save_profilepic(form_profilepic):
	random_hex = secrets.token_hex(8)
	_, f_ext = os.path.splitext(form_profilepic.filename)
	profilepic_fn = random_hex + f_ext
	profilepic_path = os.path.join(current_app.root_path, 'static/profile_pics', profilepic_fn )
	output_size =(125,125)
	i = Image.open(form_profilepic)
	i.thumbnail(output_size)
	i.save(profilepic_path)

	return profilepic_fn

def send_reset_email(user):
	token = user.get_reset_token()
	msg =Message('Password reset request', sender ='noreply@demo.com', recipients=[user.email])
	msg.body = f''' To reset your password visit the following link - 
{url_for('users.reset_token', token = token, _external=True)}

If you did not make this request, please contact contact@flaskdemo.com.
'''
	mail.send(msg)