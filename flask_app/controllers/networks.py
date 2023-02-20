from flask_app import app
from flask import render_template, redirect, request, session, flash, jsonify
from flask_app.models import network, user

@app.route('/add/network', methods = ['POST'])
def add_network():
    if not network.Network.validate_network(request.form):
        return redirect(request.referrer)
    network.Network.save(request.form)

    return redirect(request.referrer)