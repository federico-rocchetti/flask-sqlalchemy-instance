from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Length

class TeamForm(FlaskForm):
    
    team_name = StringField("Team Name", validators=[DataRequired(), Length(min=4, max=255)])
    submit = SubmitField("Submit")

class ProjectForm(FlaskForm):

    project_name = StringField("Project Name", validators=[DataRequired(), Length(min=4, max=255)])
    description = TextAreaField("Description", validators=[Length(min=4, max=255)])
    completed = BooleanField("Completed?")
    team_selection = SelectField("Team")
    submit = SubmitField("Submit")

    def update_teams(self, teams):
        self.team_selection.choices = [ (team.id, team.team_name) for team in teams ]