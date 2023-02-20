
from flask import redirect, render_template, session, request, jsonify, url_for
from flask_app import app
from flask_app.models import user, function, convo, project, skill, network



@app.route('/profile/<int:id>')
def profile(id):

    if 'user_id' not in session:
        return redirect('/')

    user_data = {
        'id': session['user_id']
    }
    current_user = user.User.get_one(user_data)

    profile_data = {
        'id': id
    }
    profile_user = user.User.get_one(profile_data)

    pic = url_for('static',filename=f'uploads/{profile_user.pic_url}')
    print(profile_user.pic_url)

    all_convos = convo.Convo.get_all_from_user(profile_data)

    all_projects = project.Project.get_all_from_user(profile_data)

    skill_data = {'user_id': id}
    all_skills = skill.Skill.get_all_from_user(skill_data)

    network_data = {'user_id': id}
    all_links = network.Network.get_all_from_user(network_data)

    return render_template('profile.html', profile_user=profile_user, current_user=current_user, all_convos=all_convos, all_projects=all_projects, all_skills=all_skills, all_links=all_links, pic=pic)




