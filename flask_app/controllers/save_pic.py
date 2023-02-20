from flask_app import app
from flask_app.models import user, network, project, convo, skill
from flask import  flash, request, redirect, url_for, render_template, session
import urllib.request
import os
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'flask_app/static/uploads/'

app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS



@app.route('/picture', methods=['POST'])
def upload_image():

    if 'user_id' not in session:
        return redirect('/')

    user_data = {'id': session['user_id']}
    user_id = {'user_id':session['user_id']}

    current_user = user.User.get_one(user_data)

    profile_data = {
        'id': session['user_id']
    }
    profile_user = user.User.get_one(profile_data)

    pic = url_for('static',filename=f'uploads/{profile_user.pic_url}')

    all_convos = convo.Convo.get_all_from_user(user_data)

    all_projects = project.Project.get_all_from_user(user_data)

    skill_data = {'user_id': session['user_id']}
    all_skills = skill.Skill.get_all_from_user(skill_data)

    network_data = {'user_id': session['user_id']}
    all_links = network.Network.get_all_from_user(network_data)

    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        flash('No image selected for uploading')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        upload = {'pic_url': filename,'id':request.form['id']}
        pic = url_for('static',filename = f'/uploads/{filename}')
        current_user.pic_url = pic
        user.User.save_user_pic(upload)
        #print('upload_image filename: ' + filename)
        flash('Image successfully uploaded and displayed above')
        return render_template('profile.html', filename=filename, current_user=current_user, profile_user=profile_user, all_convos=all_convos, all_projects=all_projects, all_skills=all_skills, all_links=all_links, pic=pic)
    else:
        flash('Allowed image types are - png, jpg, jpeg, gif')
        return redirect(request.url)

# @app.route('/display/<filename>')
# def display_image(filename):
#     #print('display_image filename: ' + filename)
#     return redirect(url_for('static', filename='uploads/' + filename), code=301)


