"""41.Write a Flask route that accepts a parameter in the URL and displays it on the page."""

from flask import Flask, render_template, request

api = Flask(__name__)
@api.route('/',methods=['GET', 'POST']) # method defined to get input through home page.
def home_page():
    return render_template('index.html') # input page initiated.
@api.route('/math',methods = ['POST']) # output page route defined through 'POST' method
def operate(): # function defined to be operated.
    if request.method == 'POST':
        ops = request.form['operation'] # taking inputs from the form.
        n1 = request.form['num1']
        n2 = request.form['num2']
        if ops == 'add':
            return render_template('results.html', result = f"Sum of {n1} and {n2} is {int(n1) + int(n2)}.") 
        if ops == 'subtract':
            return render_template('results.html', result = f"Subtraction of {n2} from {n1} is {int(n1) - int(n2)}.")
        if ops == 'multiply':
            return render_template('results.html', result = f"Product of {n1} and {n2} is {int(n1) * int(n2)}.")
        if ops == 'divide':
            return render_template('results.html', result = f"Quotient of {n1} divided by {n2} is {int(n1) / int(n2)}.")

if __name__ == '__main__':
    api.run(host='0.0.0.0')