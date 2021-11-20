from app import app
from flask import render_template


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/plants')
def plants():
    return render_template('plants.html')


@app.route('/employees')
def employees():
    return render_template('employees.html')


@app.route('/salons')
def salons():
    return render_template('salons.html')
