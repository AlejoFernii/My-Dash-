from flask_app import app
from flask import render_template, redirect, request, session, flash, url_for
from flask_app.models import project,user,collab 

@app.route('/create/project', methods = ['POST'])
def create_project():
    if not project.Project.validate_project(request.form):
        return redirect(request.referrer)
    project.Project.save(request.form)

    return redirect(request.referrer)

@app.route('/delete/project/<int:id>')
def delete_project(id):
    profile_data ={'id': id}
    project.Project.destroy(profile_data)
    user_data = session['user_id']
    return redirect(f'/profile/{user_data}')


@app.route('/view/project/<int:id>')
def show_project(id):

    if 'user_id' not in session:
        return redirect('/')

    project_data = {'id':id}

    one_project = project.Project.get_one(project_data)

    

    user_data = {
        'id': session['user_id']
    }
    current_user = user.User.get_one(user_data)

    collabs = collab.Collab.get_collaborators(project_data)
    all_collabs = []
    for u in collabs:
        pic = url_for('static', filename = f'uploads/{u.pic_url}')
        u.pic_url = pic
        all_collabs.append(u)
    print(all_collabs)

    return render_template('project.html',one_project=one_project, current_user=current_user, collabs=all_collabs)


@app.route('/update/project/<int:id>')
def show_edit_project(id):

    if 'user_id' not in session:
        return redirect('/')

    project_data = {'id':id}

    one_project = project.Project.get_one(project_data)

    

    user_data = {
        'id': session['user_id']
    }
    current_user = user.User.get_one(user_data)

    collabs = collab.Collab.get_collaborators(project_data)
    all_collabs = []
    for u in collabs:
        pic = url_for('static', filename = f'uploads/{u.pic_url}')
        u.pic_url = pic
        all_collabs.append(u)
    print(all_collabs)

    return render_template('edit_project.html',one_project=one_project, current_user=current_user, collabs=all_collabs)

@app.route('/edit/project', methods = ['POST'])
def edit_project():
    project.Project.update_project(request.form)

    profile_data = request.form['id']
    
    return redirect(f'/view/project/{profile_data}')
