from flask_app import app
from flask_app.controllers import users, dashboard, functions, convos, profile, projects, skills, networks, save_pic, comments, collabs, rsvps, inbox, professions

if __name__ == '__main__':
    app.run(debug=True)

