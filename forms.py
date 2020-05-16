from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SubmitField
from wtforms.validators import NumberRange, DataRequired

class Adjust(FlaskForm):
    # pwm = IntegerField('PWM',
    #                    default=0,
    #                    validators=[ NumberRange(0, 100, "Out of range") ])

    speed = IntegerField('speed', validators=[NumberRange(-255,255)])
    submit = SubmitField('Set Speed')
