from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField, FloatField
from wtforms.validators import InputRequired

class BusForm(FlaskForm):
  kms = FloatField('Kilometers', [InputRequired()])
  fuel_type = SelectField('Energy Type', [InputRequired()],
    choices=[('Electric', 'Electric'), ('Diesel', 'Diesel')])
  submit = SubmitField('Submit')

class CarForm(FlaskForm):
  kms = FloatField('Kilometers', [InputRequired()])
  car_size = SelectField('Car Size', [InputRequired()],
    choices=[('Small', 'Small'), ('Medium', 'Medium'), ('Big', 'Big')])
  fuel_type = SelectField('Type of Fuel', [InputRequired()],
    choices=[('Petrol', 'Petrol'), ('Diesel', 'Diesel'), ('Electric', 'Electric')])
  submit = SubmitField('Submit')

class PlaneForm(FlaskForm):
  kms = FloatField('Kilometers', [InputRequired()])
  fuel_type = SelectField('Travel Class', [InputRequired()],
    choices=[('Economy', 'Economy'), ('Economy Premium', 'Economy Premium'), ('Business', 'Business')])
  submit = SubmitField('Submit')
  
class FerryForm(FlaskForm):
  kms = FloatField('Kilometers', [InputRequired()])
  fuel_type = SelectField('Energy Type', [InputRequired()],
    choices=[('Diesel', 'Diesel'), ('Electric', 'Electric')])
  submit = SubmitField('Submit')

class MotorbikeForm(FlaskForm):
  kms = FloatField('Kilometers', [InputRequired()])
  fuel_type = SelectField('Type of Fuel', [InputRequired()],
    choices=[('Petrol', 'Petrol')])
  submit = SubmitField('Submit')

class BicycleForm(FlaskForm):
  kms = FloatField('Kilometers', [InputRequired()])
  fuel_type = SelectField('Type of Fuel', [InputRequired()],
    choices=[('No Fossil Fuel', 'No Fossil Fuel')])
  submit = SubmitField('Submit')  

class WalkForm(FlaskForm):
  kms = FloatField('Kilometers', [InputRequired()])
  fuel_type = SelectField('Type of Fuel', [InputRequired()],
    choices=[('No Fossil Fuel', 'No Fossil Fuel')])
  submit = SubmitField('Submit')  

class TrainForm(FlaskForm):
  kms = FloatField('Kilometers', [InputRequired()])
  fuel_type = SelectField('Energy Type', [InputRequired()],
    choices=[('Electric', 'Electric'), ('Diesel', 'Diesel')])
  submit = SubmitField('Submit')  

class ElectricScooterForm(FlaskForm):
  kms = FloatField('Kilometers', [InputRequired()])
  fuel_type = SelectField('Energy Source', [InputRequired()],
    choices=[('Electric', 'Electric')])
  submit = SubmitField('Submit') 
