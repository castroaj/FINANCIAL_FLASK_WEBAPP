from flask import Flask, render_template, redirect, request
from Finanical_Functions import EAR, HPR, APR

# Configure the Flask Object
app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['DEBUG'] = True

def check_float(f):
    try:
        float(f)
        return True
    except ValueError:
        return False


# Index of the website
@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('Index.html')

@app.route('/hpr', methods=['POST', 'GET'])
def hpr():
    purchasePrice , salePrice, dividends = 0, 0, 0
    hpr, cg, dy = -1, -1, -1
    isCalculated = False;
    isPost = False

    if request.method == 'POST':
        isPost = True
        form = request.form
        purchasePrice = form['purchasePrice']
        salePrice = form['salePrice']
        dividends = form['dividends']

        if check_float(purchasePrice) and check_float(salePrice) and check_float(dividends):
            purchasePrice, salePrice, dividends = float(purchasePrice), float(salePrice), float(dividends)
            hpr, cg, dy = HPR(Beginning_Price=purchasePrice, End_Value=salePrice, Dividend=dividends)

            if hpr != -1 and cg != -1 and dy != 1:
                isCalculated = True
        else:
            purchasePrice , salePrice, dividends = 0, 0, 0
        
    hpr = "{:.2f}".format(hpr)
    cg = "{:.2f}".format(cg)
    dy = "{:.2f}".format(dy)

    return render_template('hpr.html', hpr=hpr, capitalGain=cg, dividendYield=dy, purchasePrice=purchasePrice, salePrice=salePrice, dividends=dividends, isCalculated=isCalculated, isPost=isPost)

@app.route('/apr', methods=['POST', 'GET'])
def apr():
    number_of_periods = 0
    per_period_rate = 0
    apr = 0

    if request.method == 'POST':
        form = request.form
        number_of_periods = int(form['number_of_periods'])
        per_period_rate = int(form['per_period_rate'])

        apr = APR(Per_Period_Rate=per_period_rate, Number_Periods=number_of_periods)

    return render_template('apr.html', apr=apr, number_of_periods=number_of_periods, per_period_rate=per_period_rate)

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

    return render_template('ear.html', ear=ear, number_of_periods=number_of_periods, per_period_rate=per_period_rate)

# Main function
if __name__ == "__main__":
    app.run()