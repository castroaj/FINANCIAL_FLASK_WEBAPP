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
    purchasePrice = 0
    salePrice = 0
    dividends = 0
    hpr = 0

    if request.method == 'POST':
        form = request.form
        purchasePrice = int(form['purchasePrice'])
        salePrice = int(form['salePrice'])
        dividends = int(form['dividends'])

        hpr = HPR(Beginning_Price=purchasePrice, End_Value=salePrice, Dividend=dividends)

    return render_template('hpr.html', hpr=hpr, purchasePrice=purchasePrice, salePrice=salePrice, dividends=dividends)

@app.route('/apr', methods=['POST', 'GET'])
def apr():
    number_of_periods = 0
    per_period_rate = 0
    apr = 0

    if request.method == 'POST':
        form = request.form
        number_of_periods = int(form['number_of_periods'])
        per_period_rate = int(form['per_period_rate'])

        apr = APR(Number_Periods=number_of_periods, Per_Period_Rate=per_period_rate)

    return render_template('apr.html', apr=apr)

@app.route('/ear', methods=['POST', 'GET'])
def ear():
    ear = 0
    number_of_periods = 0
    per_period_rate = 0

    if request.method == 'POST':
        form = request.form
        number_of_periods = int(form['number_of_periods'])
        per_period_rate = int(form['per_period_rate'])

        print(number_of_periods)
        print(per_period_rate)

        ear = EAR(Number_Periods=number_of_periods, Per_Period_Rate=per_period_rate)

        print(ear)


    return render_template('ear.html', ear=ear, number_of_periods=number_of_periods, per_period_rate=per_period_rate)

# Main function
if __name__ == "__main__":
    app.run()