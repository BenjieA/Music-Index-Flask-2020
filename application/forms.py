from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class SongForm(FlaskForm):
    user_name = StringField('User Name',
            validators = [
                DataRequired(),
                Length(min=2, max=30)
            ]
    )
    title = StringField('Title',
            validators = [
                DataRequired(),
                Length(min=1, max=100)
            ]
    )

    lyrics = StringField('Lyrics',
            validators = [
                DataRequired(),
                Length(min=4, max=100)
            ]
    )

   password = StringField('Password',
            validators = [
	       DataRequired(),
	       Length(min=8, max=30)
	    ]
   )
    submit = SubmitField('Post Song')


