from flask import redirect, render_template, session, request, jsonify, url_for, flash
from flask_app import app
from flask_app.models import user





@app.route('/update/profession', methods=['POST'])
def add_profession():
    data = {
        'id': session['user_id'],
        'profession': request.form['profession']    
    }
    if len(request.form['profession']) < 1:
        flash("Profession Min 2 Characters.", 'prof')
        error = {'Invalid': request.form['profession']}
        print(error)
        return redirect(request.referrer)
    user.User.update_Profession(data)

    return jsonify(request.form['profession'])