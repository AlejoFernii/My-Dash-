from flask_app import app
from flask import render_template, redirect, request, session, flash, jsonify
from flask_app.models import skill, user

@app.route('/add/skill', methods = ['POST'])
def add_skill():
    one_skill = {'skill': request.form['skill']}
    if not skill.Skill.validate_skill(one_skill):
        return redirect(request.referrer)
    skill.Skill.save(one_skill)
    skill_data = skill.Skill.get_skill_by_name(one_skill)
    
    data = {
        'skill_id': skill_data.id,
        'user_id': request.form['user_id']
    }
    skill.Skill.add_skill_to_user(data)

    return redirect(request.referrer)
