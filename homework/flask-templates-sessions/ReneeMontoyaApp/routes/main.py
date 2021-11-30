from app import app, db
from flask import render_template, request, redirect, url_for, session
from models import Plant, Employee, Salon
from utils.helpers import encrypt_string


@app.route('/')
def main():
    plants = Plant.query.all()
    employees = Employee.query.all()
    salons = Salon.query.all()
    return render_template('index.html', plants=plants, employees=employees, salons=salons, session=session)


@app.route('/login')
def login():
    return render_template('login.html', session=session)


@app.route('/auth', methods=['POST'])
def auth():
    error = None
    form = request.form
    user = Employee.query.filter(Employee.email == form['login']).filter(
        Employee.password == encrypt_string(form['password'])).first()
    if user is not None:
        session['user'] = user.serialize
        return redirect(url_for('main'))  # This is redirect doesn't work ==> FIXED in nginx.conf
    else:
        error = "Invalid email or password"
        return render_template('login.html', session=session, error=error)


@app.route('/logout')
def logout():
    session.pop('user')
    # return redirect("http://localhost:8082/")
    return redirect(url_for('main'))  # This is redirect doesn't work ==> FIXED in nginx.conf


@app.route('/plants')
def plants():
    plants = Plant.query.all()
    employees = Employee.query.all()
    return render_template('plants.html', plants=plants, employees=employees, session=session)


@app.route('/plant/<int:id>')
def plant(id):
    plant = Plant.query.get(id)
    return render_template('plant.html', plant=plant, session=session)


@app.route('/plant/<int:id>/edit')
def plant_edit_page(id):
    error = None
    plant = Plant.query.get(id)
    if session.get('user') is None:
        error = "Only authorized users can edit"
        return render_template('plant.html', plant=plant, session=session, error=error)

    employees = Employee.query.all()
    return render_template('forms/edit-plant.html', plant=plant, employees=employees, session=session)


@app.route('/plant/<int:id>/update', methods=['POST'])
def plant_update(id):
    if session.get('user') is None:
        return redirect(url_for('plant', id=id))
    plant = Plant.query.get(id)
    form_data = request.form
    plant.name = form_data.get('name')
    plant.location = form_data.get('location')
    plant.director_id = form_data.get('director_id')
    db.session.add(plant)
    db.session.commit()
    return redirect(url_for('plant', id=id))


@app.route('/employees')
def employees():
    return render_template('employees.html', session=session)


@app.route('/employee/<int:id>')
def employee(id):
    employee = Employee.query.get(id)
    return render_template('employee.html', employee=employee, session=session)


@app.route('/employee/<int:id>/edit')
def employee_edit_page(id):
    error = None
    employee = Employee.query.get(id)
    if session.get('user') is None:
        error = "Only authorized users can edit"
        return render_template('employee.html', employee=employee, error=error)
    plants = Plant.query.all()
    salons = Salon.query.all()
    return render_template('forms/edit-employee.html', employee=employee, plants=plants, salons=salons, session=session)


@app.route('/employee/<int:id>/update', methods=['POST'])
def employee_update(id):
    if session.get('user') is None:
        return redirect(url_for('employee', id=id))
    employee = Employee.query.get(id)
    form_data = request.form
    employee.name = form_data.get('name')
    employee.email = form_data.get('email')
    employee.department_type = form_data.get('department_type')
    employee.department_id = form_data.get('department_id')
    db.session.add(employee)
    db.session.commit()
    return redirect(url_for('employee', id=id))


@app.route('/salons/<int:id>')
def salon_(id):
    salon = Salon.query.get(id)
    return render_template('salons.html', salon=salon, session=session)


@app.route('/salons')
def salons():
    return render_template('salons.html', session=session)


@app.route('/salon/<int:id>')
def salon(id):
    salon = Salon.query.get(id)
    return render_template('salon.html', salon=salon, session=session)


@app.route('/salon/<int:id>/edit')
def salon_edit_page(id):
    error = None
    salon = Salon.query.get(id)
    if session.get('user') is None:
        error = "Only authorized users can edit"
        return render_template('salon.html', salon=salon, error=error)
    employees = Employee.query.all()
    return render_template('forms/edit-salon.html', salon=salon, employees=employees, session=session)


@app.route('/salon/<int:id>/update', methods=['POST'])
def salon_update(id):
    if session.get('user') is None:
        return redirect(url_for('salon', id=id))
    salon = Salon.query.get(id)
    form_data = request.form
    salon.name = form_data.get('name')
    salon.city = form_data.get('city')
    salon.address = form_data.get('address')
    salon.director_id = form_data.get('director_id')
    db.session.add(salon)
    db.session.commit()
    return redirect(url_for('salon', id=id))
