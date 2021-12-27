from app import app, db
from flask import render_template, request, redirect, url_for
from models import Plant, Employee, Salon


@app.route('/')
def main():
    plants = Plant.query.all()
    employees = Employee.query.all()
    salons = Salon.query.all()

    return render_template('index.html', plants=plants, employees=employees, salons=salons)


@app.route('/plants')
def plants():
    plants = Plant.query.all()
    employees = Employee.query.all()
    return render_template('plants.html', plants=plants, employees=employees)


@app.route('/plant/<int:id>')
def plant(id):
    plant = Plant.query.get(id)
    return render_template('plant.html', plant=plant)


@app.route('/plant/<int:id>/edit')
def plant_edit_page(id):
    plant = Plant.query.get(id)
    employees = Employee.query.all()
    return render_template('forms/edit-plant.html', plant=plant, employees=employees)


@app.route('/plant/<int:id>/update', methods=['POST'])
def plant_update(id):
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
    return render_template('employees.html')


@app.route('/employee/<int:id>')
def employee(id):
    employee = Employee.query.get(id)
    return render_template('employee.html', employee=employee)


@app.route('/employee/<int:id>/edit')
def employee_edit_page(id):
    employee = Employee.query.get(id)
    plants = Plant.query.all()
    salons = Salon.query.all()
    return render_template('forms/edit-employee.html', employee=employee, plants=plants, salons=salons)


@app.route('/employee/<int:id>/update', methods=['POST'])
def employee_update(id):
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
    return render_template('salons.html', salon=salon)


@app.route('/salons')
def salons():
    return render_template('salons.html')


@app.route('/salon/<int:id>')
def salon(id):
    salon = Salon.query.get(id)
    return render_template('salon.html', salon=salon)


@app.route('/salon/<int:id>/edit')
def salon_edit_page(id):
    salon = Salon.query.get(id)
    employees = Employee.query.all()
    return render_template('forms/edit-salon.html', salon=salon, employees=employees)


@app.route('/salon/<int:id>/update', methods=['POST'])
def salon_update(id):
    salon = Salon.query.get(id)
    form_data = request.form
    salon.name = form_data.get('name')
    salon.city = form_data.get('city')
    salon.address = form_data.get('address')
    salon.director_id = form_data.get('director_id')
    db.session.add(salon)
    db.session.commit()
    return redirect(url_for('salon', id=id))
