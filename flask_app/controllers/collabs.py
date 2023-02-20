from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models import collab, user, project 

@app.route('/add/collab', methods = ['POST'])
def addCollab():
    collab.Collab.save(request.form)

    return redirect(request.referrer)

