from flask_app import app
from flask import render_template, session, redirect
from flask_app.models import user

@app.route('/inbox')
def inbox():
    if 'user_id' not in session:
        return redirect('/')
    user_data = {'id':session['user_id']}
    current_user = user.User.get_one(user_data)
    return render_template('inbox.html', current_user=current_user)