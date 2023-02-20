from flask import redirect, render_template,session,url_for
from flask_app import app
from flask_app.models import user,function,convo


@app.route('/home')
def home():

    if 'user_id' not in session:
        redirect('/')
    
    user_data = {'id': session['user_id']}
    current_user = user.User.get_one(user_data)

    all_functions = function.Function.get_all_with_user()

    all_convos = convo.Convo.get_all_with_comments()
    new_convos = []
    for c in all_convos:
        if c.creator.pic_url == 'None':
            pic = url_for('static',filename = 'img/user-circle.png')
        else:

            pic = url_for('static',filename=f'uploads/{c.creator.pic_url}')

        c.creator.pic_url = pic

        new_convos.append(c) 

    return render_template('home.html', current_user=current_user, all_functions=all_functions, all_convos=new_convos)