from flask_app import app
from flask import render_template, redirect, request, session, flash, url_for
from flask_app.models import user,function,rsvp

@app.route('/create/function', methods = ['POST'])
def create_function():
    if not function.Function.validate_function(request.form):
        return redirect(request.referrer)
    function.Function.save(request.form)
    return redirect('/home')


@app.route('/show/function/<int:id>')
def show_function(id):

    user_data = {'id': session['user_id']}

    current_user = user.User.get_one(user_data)

    data = {'id':id}

    one_function = function.Function.get_one_with_user(data)

    rsvp_data = {'function_id':id}

    rsvps = rsvp.RSVP.get_all_rsvps(rsvp_data)
    all_rsvps = []
    for r in rsvps:
        pic = url_for('static', filename = f'uploads/{r.pic_url}')
        r.pic_url = pic
        all_rsvps.append(r)
    print(all_rsvps)

    return render_template('function.html', one_function=one_function, current_user=current_user, all_rsvps=all_rsvps)


@app.route('/update/function/<int:id>')
def update_function(id):
    
    user_data = {'id': session['user_id']}

    current_user = user.User.get_one(user_data)

    data = {'id':id}

    one_function = function.Function.get_one_with_user(data)

    rsvp_data = {'function_id':id}

    rsvps = rsvp.RSVP.get_all_rsvps(rsvp_data)
    all_rsvps = []
    for r in rsvps:
        pic = url_for('static', filename = f'uploads/{r.pic_url}')
        r.pic_url = pic
        all_rsvps.append(r)
    print(all_rsvps)

    return render_template('edit_function.html', one_function=one_function, current_user=current_user, all_rsvps=all_rsvps)

@app.route('/edit/function', methods=['POST'])
def edit_function():
    function.Function.update_function(request.form)

    function_data = request.form['id']
    return redirect(f'/show/function/{function_data}')



@app.route('/delete/function/<int:id>')
def destroy_function(id):

    data = {'id':id}

    function.Function.destroy(data)

    return redirect('/home')



