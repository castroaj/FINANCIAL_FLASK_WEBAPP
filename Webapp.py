from flask import Flask, render_template, redirect, request
from Finanical_Functions import EAR, HPR, APR, harmonic_mean, Period_Rate, Sharpe, GeoMean

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
    isCalculated = False
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

@app.route('/PerPeriod', methods=['POST', 'GET'])
def perPeriod():
    number_of_payments, payment_amount, amount_borrowed = 0, 0, 0

    if request.method == 'POST':
        form = request.form
        number_of_payments = form['number_of_payments']
        payment_amount = form['payment_amount']
        amount_borrowed = form['amount_borrowed']

        if check_float(number_of_payments) and check_float(payment_amount) and check_float(amount_borrowed):
            number_of_payments, payment_amount, amount_borrowed = float(number_of_payments), float(payment_amount), float(amount_borrowed)
            perPeriodRate = Period_Rate(Number_Of_Payments=number_of_payments, Payment_Amount=payment_amount, Amount_Barrowed=amount_borrowed)

    perPeriodRate = "{:.2f}".format(perPeriodRate)

    return render_template('perPeriod.html', number_of_payments=number_of_payments, payment_amount=payment_amount, amount_borrowed=amount_borrowed, perPeriodRate=perPeriodRate)

@app.route('/sharpe', methods=['POST', 'GET'])
def sharpe():
    return_on_portfolio, risk_free_rate, risk_of_portfolio = 0, 0, 0

    if request.method == 'POST':
        form = request.form
        return_on_portfolio = form['return_on_portfolio']
        risk_free_rate = form['risk_free_rate']
        risk_of_portfolio = form['risk_of_portfolio']

        if check_float(return_on_portfolio) and check_float(risk_free_rate) and check_float(risk_of_portfolio):
            return_on_portfolio, risk_free_rate, risk_of_portfolio = float(return_on_portfolio), float(risk_free_rate), float(risk_of_portfolio)
            sharpe = Sharpe(ReturnOnPortfolio=return_on_portfolio, RiskFreeRate=risk_free_rate, RiskOfPortfolio=risk_of_portfolio)

    sharpe = "{:.2f}".format(sharpe)

    return render_template('sharpe.html', return_on_portfolio=return_on_portfolio, risk_free_rate=risk_free_rate, risk_of_portfolio=risk_of_portfolio, sharpe=sharpe)

@app.route('/harmonicMean', methods=['POST', 'GET'])
def harmonic_mean():
    harmonic_data = 0

    if request.method == 'POST':
        dataString = request.form['harmonic_data']
        splitData = dataString.split(',').strip()
        harmonic_data = [int(x) for x in splitData]
        harmonic_mean_result = harmonic_mean(harmonic_data)

    return render_template('sharpe.html', harmonic_data=harmonic_data, harmonic_mean_result=harmonic_mean_result)


@app.route('/geometricMean', methods=['POST', 'GET'])
def geometricMean():
    geo_data = 0

    if request.method == 'POST':
        dataString = request.form['geo_data']
        splitData = dataString.split(',').strip()
        geo_data = [int(x) for x in splitData]
        geo_mean_result = GeoMean(geo_data)

    return render_template('sharpe.html', geo_data=geo_data, geo_mean_result=geo_mean_result)


# Main function
if __name__ == "__main__":
    app.run()