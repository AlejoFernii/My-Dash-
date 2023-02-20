from flask_app import app
from flask import render_template, redirect, request, session, flash, jsonify, url_for
from flask_app.models import user,convo,comment
import requests

@app.route('/create/convo', methods = ['POST'])
def createConvo():
    if not convo.Convo.validate_convo(request.form):
        return redirect(request.referrer)
    convo.Convo.save(request.form)
    return redirect(request.referrer)

@app.route('/show/convo/<int:id>')
def show_convo(id):
    if 'user_id' not in session:
        return redirect('/')

    convo_data = {'id':id}
    one_convo = convo.Convo.get_one_with_comments(convo_data)

    for c in one_convo.comments:
        pic = url_for('static', filename = f'uploads/{c.creator.pic_url}')
        c.creator.pic_url = pic

    

    pic = url_for('static',filename=f'/uploads/{one_convo.creator.pic_url}')
    one_convo.creator.pic_url = pic
    user_data = {'id':session['user_id']}
    current_user = user.User.get_one(user_data)

    return render_template('conversation.html', one_convo=one_convo, current_user=current_user)

@app.route('/update/convo/<int:id>')
def update_convo(id):
    if 'user_id' not in session:
        return redirect('/')

    convo_data = {'id':id}
    one_convo = convo.Convo.get_one_with_comments(convo_data)

    for c in one_convo.comments:
        pic = url_for('static', filename = f'uploads/{c.creator.pic_url}')
        c.creator.pic_url = pic

    

    pic = url_for('static',filename=f'/uploads/{one_convo.creator.pic_url}')
    one_convo.creator.pic_url = pic
    user_data = {'id':session['user_id']}
    current_user = user.User.get_one(user_data)

    return render_template('edit_convo.html', one_convo=one_convo, current_user=current_user)

@app.route('/edit/convo', methods = ['POST'])
def edit_convo():
    convo.Convo.update_convo(request.form)

    return redirect(request.referrer)






