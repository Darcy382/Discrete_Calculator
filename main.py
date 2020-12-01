from flask import Flask, render_template, request, redirect
from discrete_functions import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/euclideanAlgo', methods = ['post'])
def euclideanAlgo():
    if request.method == 'POST':
        num1 = request.form['num1']
        num2 = request.form['num2']
        try:
            num1 = int(num1)
            num2 = int(num2)
        except ValueError:
            return redirect('/') # TODO Error screen for invalid inputs
        table, gcd, s, t = eucleanAlgorithum(num1, num2)
    return render_template("euclean_display.html", table=table)

if __name__ == '__main__':
    app.run()
