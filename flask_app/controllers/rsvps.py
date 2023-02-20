from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models import user,function,rsvp

@app.route('/add/rsvp', methods=['POST'])
def add_attendee():
    rsvp.RSVP.save(request.form)

    return redirect(request.referrer)