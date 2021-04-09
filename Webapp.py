from flask import Flask, render_template, redirect, request
from Finanical_Functions import EAR, HPR, APR

# Configure the Flask Object
app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['DEBUG'] = True

# Index of the website
@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('Index.html')

@app.route('/hpr', methods=['POST', 'GET'])
def hpr():
    hpr = 5

    if request.method == 'POST':
        form = request.form
        purchasePrice = int(form['purchasePrice'])
        salePrice = int(form['salePrice'])
        dividends = int(form['dividends'])

        hpr = HPR(Beginning_Price=purchasePrice, End_Value=salePrice, Dividend=dividends)

    return render_template('hpr.html', hpr=hpr)

@app.route('/apr', methods=['POST', 'GET'])
def apr():
    apr = 5

    if request.method == 'POST':
        form = request.form
        number_of_periods = int(form['number_of_periods'])
        per_period_rate = int(form['per_period_rate'])

        apr = APR(Number_Periods=number_of_periods, Per_Period_Rate=per_period_rate)

    return render_template('apr.html', apr=apr)

# Main function
if __name__ == "__main__":
    app.run()