from flask import Flask, render_template, request, redirect
from discrete_functions import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/euclidean_algorithum', methods = ['post'])
def euclidean_algorithum():
    if request.method == 'POST':
        num1 = request.form['num1']
        num2 = request.form['num2']
        try:
            num1 = int(num1)
            num2 = int(num2)
        except ValueError:
            return redirect('/') # TODO Error screen for invalid inputs
        table, gcd, s, t = euclideanAlgorithum(num1, num2)
    return render_template("euclidean_solution.html", num1=num1, num2=num2, table=table, solution_idx=0)

@app.route('/convert_bases', methods = ['post'])
def convert_bases():
    if request.method == 'POST':
        num1 = request.form['num1']
        fromBase = request.form['base1']
        toBase = request.form['base2']
        try:
            num1 = int(num1)
            num1 = str(num1)
            fromBase = int(fromBase)
            toBase = int(toBase)
        except ValueError:
            return redirect('/') # TODO Error screen for invalid inputs
        output = convertBases(fromBase, toBase, num1)
    return render_template("convert_bases_solution.html", num1=num1, fromBase=fromBase, toBase=toBase, output=output, solution_idx=1)
if __name__ == '__main__':
    app.run()
