from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    username = db.Column(db.String(255), unique = True, nullable = False)
    password = db.Column(db.String(255), nullable = True)

class Team(db.Model):

    __tablename__ = "teams"

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    team_name = db.Column(db.String(255), unique = True, nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable = False)

class Project(db.Model):

    __tablename__ = "projects"

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    project_name = db.Column(db.String(255), nullable = False)
    description = db.Column(db.String(255), nullable = False)
    completed = db.Column(db.Boolean, default = False)
    team_id = db.Column(db.Integer, db.ForeignKey("teams.id"), nullable = False)