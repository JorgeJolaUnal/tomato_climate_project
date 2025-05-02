from flask import Blueprint, Flask, render_template,request, redirect, url_for, flash

main=Blueprint('main',__name__)

@main.route("/")
def index():
    return render_template('main_interface.html')
# Temperatura
@main.route("/summ")
def summ():
    return render_template('summary.html')
# Temperatura
@main.route("/temp")
def temp():
    return render_template('temperature.html')
# Radiación
@main.route("/rad")
def rad():
    return render_template('radiation.html')
# Humedad
@main.route("/hum")
def hum():
    return render_template('humidity.html')
# Viento
@main.route("/wind")
def wind():
    return render_template('wind.html')