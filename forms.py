from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length

class QuestionForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(min=1, max=100)])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Submit')

class FeedbackForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=1, max=50)])
    email = StringField('Email', validators=[DataRequired(), Length(min=6, max=50)])
    message = TextAreaField('Message', validators=[DataRequired()])
    submit = SubmitField('Submit')