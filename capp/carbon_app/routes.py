from flask import render_template, Blueprint, request, redirect, url_for, flash
from capp.models import Transport
from capp import db
from datetime import timedelta, datetime
from flask_login import login_required, current_user
from capp.carbon_app.forms import BusForm, CarForm, PlaneForm, FerryForm, MotorbikeForm, BicycleForm, WalkForm, TrainForm, ElectricScooterForm

carbon_app=Blueprint('carbon_app',__name__)


#These are the emissions per passenger and per transport (kg CO2 / km)
efco2 = {
    'Bus': {'Electric': 0.00115, 'Diesel': 0.03},
    'Car': {
        'Petrol': {'Small': 0.150, 'Medium': 0.198, 'Big': 0.261},
        'Diesel': {'Small': 0.174, 'Medium': 0.229, 'Big': 0.302},
        'Electric': {'Small': 0.0045, 'Medium': 0.0059, 'Big': 0.0078}
    },
    'Plane': {'Economy': 0.127, 'Economy Premium': 0.155, 'Business': 0.285},
    'Ferry': {'Diesel': 0.186, 'Electric': 0.084},
    'Motorbike': {'Petrol': 0.08156},
    'Electricscooter': {'Electric': 0},
    'Bicycle': {'No Fossil Fuel': 0},
    'Walk': {'No Fossil Fuel': 0},
    'Train': {'Electric': 0.007, 'Diesel': 0.091}
}


#carbon app
@carbon_app.route('/carbon_app')
@login_required
def carbon_app_home():
    return render_template('carbon_app/carbon_app.html', title='carbon_app')

#New entry bus
@carbon_app.route('/carbon_app/new_entry_bus', methods=['GET','POST'])
@login_required
def new_entry_bus():
    form = BusForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        transport = 'Bus'
        # kms = request.form['kms']
        # fuel = request.form['fuel_type']

        co2 = float(kms) * efco2[transport][fuel]
        co2 = float("{:.2f}".format(co2))
        emissions = Transport(kms=kms, transport=transport, fuel=fuel, co2=co2, total=co2, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('carbon_app.your_data'))
    return render_template('carbon_app/new_entry_bus.html', title='new entry bus', form=form)

#New entry car
@carbon_app.route('/carbon_app/new_entry_car', methods=['GET','POST'])
@login_required
def new_entry_car():
    form = CarForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        car_size = form.car_size.data
        transport_key = 'Car'

        co2_factor = efco2[transport_key][fuel][car_size]
        co2 = float(kms) * co2_factor
        co2 = float("{:.2f}".format(co2))
        transport_label = f"{car_size} Car"
        emissions = Transport(kms=kms, transport=transport_label, fuel=fuel, co2=co2, total=co2, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('carbon_app.your_data'))
    return render_template('carbon_app/new_entry_car.html', title='new entry car', form=form)    

#New entry plane
@carbon_app.route('/carbon_app/new_entry_plane', methods=['GET','POST'])
@login_required
def new_entry_plane():
    form = PlaneForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        transport = 'Plane'
        # kms = request.form['kms']
        # fuel = request.form['fuel_type']

        co2 = float(kms) * efco2[transport][fuel]
        co2 = float("{:.2f}".format(co2))
        emissions = Transport(kms=kms, transport=transport, fuel=fuel, co2=co2, total=co2, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('carbon_app.your_data'))
    return render_template('carbon_app/new_entry_plane.html', title='new entry plane', form=form)  

#New entry ferry
@carbon_app.route('/carbon_app/new_entry_ferry', methods=['GET','POST'])
@login_required
def new_entry_ferry():
    form = FerryForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        transport = 'Ferry'
        # kms = request.form['kms']
        # fuel = request.form['fuel_type']

        co2 = float(kms) * efco2[transport][fuel]
        co2 = float("{:.2f}".format(co2))
        emissions = Transport(kms=kms, transport=transport, fuel=fuel, co2=co2, total=co2, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('carbon_app.your_data'))
    return render_template('carbon_app/new_entry_ferry.html', title='new entry ferry', form=form)     

#New entry motorbike
@carbon_app.route('/carbon_app/new_entry_motorbike', methods=['GET','POST'])
@login_required
def new_entry_motorbike():
    form = MotorbikeForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        transport = 'Motorbike'
        # kms = request.form['kms']
        # fuel = request.form['fuel_type']

        co2 = float(kms) * efco2[transport][fuel]
        co2 = float("{:.2f}".format(co2))
        emissions = Transport(kms=kms, transport=transport, fuel=fuel, co2=co2, total=co2, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('carbon_app.your_data'))
    return render_template('carbon_app/new_entry_motorbike.html', title='new entry motorbike', form=form) 

#New entry bicycle
@carbon_app.route('/carbon_app/new_entry_bicycle', methods=['GET','POST'])
@login_required
def new_entry_bicycle():
    form = BicycleForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        transport = 'Bicycle'
        # kms = request.form['kms']
        # fuel = request.form['fuel_type']

        co2 = float(kms) * efco2[transport][fuel]
        co2 = float("{:.2f}".format(co2))
        emissions = Transport(kms=kms, transport=transport, fuel=fuel, co2=co2, total=co2, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('carbon_app.your_data'))
    return render_template('carbon_app/new_entry_bicycle.html', title='new entry bicycle', form=form)

#New entry walk
@carbon_app.route('/carbon_app/new_entry_walk', methods=['GET','POST'])
@login_required
def new_entry_walk():
    form = WalkForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        transport = 'Walk'
        # kms = request.form['kms']
        # fuel = request.form['fuel_type']

        co2 = float(kms) * efco2[transport][fuel]
        co2 = float("{:.2f}".format(co2))
        emissions = Transport(kms=kms, transport=transport, fuel=fuel, co2=co2, total=co2, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('carbon_app.your_data'))
    return render_template('carbon_app/new_entry_walk.html', title='new entry walk', form=form)

#New entry train
@carbon_app.route('/carbon_app/new_entry_train', methods=['GET','POST'])
@login_required
def new_entry_train():
    form = TrainForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        transport = 'Train'
        co2 = float(kms) * efco2[transport][fuel]
        co2 = float("{:.2f}".format(co2))
        emissions = Transport(kms=kms, transport=transport, fuel=fuel, co2=co2, total=co2, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('carbon_app.your_data'))
    return render_template('carbon_app/new_entry_train.html', title='new entry train', form=form)

#New entry electricscooter
@carbon_app.route('/carbon_app/new_entry_electricscooter', methods=['GET','POST'])
@login_required
def new_entry_electricscooter():
    form = ElectricScooterForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        transport = 'Electricscooter'
        # kms = request.form['kms']
        # fuel = request.form['fuel_type']

        co2 = float(kms) * efco2[transport][fuel]
        co2 = float("{:.2f}".format(co2))
        emissions = Transport(kms=kms, transport=transport, fuel=fuel, co2=co2, total=co2, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('carbon_app.your_data'))
    return render_template('carbon_app/new_entry_electricscooter.html', title='new entry electricscooter', form=form)


#Your data
@carbon_app.route('/carbon_app/your_data')
@login_required
def your_data():
    #Table
    entries = Transport.query.filter_by(author=current_user). \
        filter(Transport.date> (datetime.now() - timedelta(days=5))).\
        order_by(Transport.date.desc()).order_by(Transport.transport.asc()).all()
    return render_template('carbon_app/your_data.html', title='your_data', entries=entries)

#Delete emission
@carbon_app.route('/carbon_app/delete-emission/<int:entry_id>')
def delete_emission(entry_id):
    entry = Transport.query.get_or_404(int(entry_id))
    db.session.delete(entry)
    db.session.commit()
    flash("Entry deleted", "success")
    return redirect(url_for('carbon_app.your_data'))
    
  
