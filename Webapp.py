from flask import Flask, render_template, redirect, request
from flask.helpers import flash
from numpy import ERR_CALL
from Finanical_Functions import EAR, HPR, APR, HarmonicMean, Period_Rate, Sharpe, GeoMean

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
    number_of_periods, per_period_rate = 0, 0
    apr = -1
    isPost = False
    isCalculated = False

    if request.method == 'POST':
        isPost = True
        form = request.form
        number_of_periods = form['number_of_periods']
        per_period_rate = form['per_period_rate']

        if check_float(number_of_periods) and check_float(per_period_rate):
            number_of_periods, per_period_rate = float(number_of_periods), float(per_period_rate)
            apr = APR(Per_Period_Rate=per_period_rate, Number_Periods=number_of_periods)
            isCalculated = True

    apr = "{:.2f}".format(apr)

    return render_template('apr.html', apr=apr, number_of_periods=number_of_periods, per_period_rate=per_period_rate, isPost=isPost, isCalculated=isCalculated)

@app.route('/ear', methods=['POST', 'GET'])
def ear():
    number_of_periods, per_period_rate = 0, 0
    ear = -1
    isPost = False
    isCalculated = False

    if request.method == 'POST':
        isPost = True
        form = request.form
        number_of_periods = form['number_of_periods']
        per_period_rate = form['per_period_rate']

        if check_float(number_of_periods) and check_float(per_period_rate):
            number_of_periods, per_period_rate = float(number_of_periods), float(per_period_rate)
            ear = EAR(Number_Periods=number_of_periods, Per_Period_Rate=per_period_rate)
            isCalculated = True

    ear = "{:.2f}".format(ear)

    return render_template('ear.html', ear=ear, number_of_periods=number_of_periods, per_period_rate=per_period_rate, isPost=isPost, isCalculated=isCalculated)

@app.route('/PerPeriod', methods=['POST', 'GET'])
def perPeriod():
    apr_val, number_of_periods = 0, 0
    perPeriodRate = -1
    isPost = False
    isCalculated = False

    if request.method == 'POST':
        isPost = True
        form = request.form
        apr_val = form['apr']
        number_of_periods = form['number_of_periods']

        if check_float(apr_val) and check_float(number_of_periods):
            apr_val, number_of_periods = float(apr_val), float(number_of_periods)
            if (number_of_periods != 0):
                perPeriodRate = Period_Rate(A=apr_val, P=number_of_periods)
                isCalculated = True

    perPeriodRate = "{:.2f}".format(perPeriodRate)

    return render_template('PPR.html', perPeriodRate=perPeriodRate, apr=apr_val, number_of_periods=number_of_periods, isPost=isPost, isCalculated=isCalculated)

@app.route('/sharpe', methods=['POST', 'GET'])
def sharpe():
    return_on_portfolio, risk_free_rate, risk_of_portfolio = 0, 0, 0
    sharpe = -1
    isPost = False
    isCalculated = False

    if request.method == 'POST':
        isPost = True
        form = request.form
        return_on_portfolio = form['return_on_portfolio']
        risk_free_rate = form['risk_free_rate']
        risk_of_portfolio = form['risk_of_portfolio']

        if check_float(return_on_portfolio) and check_float(risk_free_rate) and check_float(risk_of_portfolio):
            return_on_portfolio, risk_free_rate, risk_of_portfolio = float(return_on_portfolio), float(risk_free_rate), float(risk_of_portfolio)
            if risk_of_portfolio != 0:
                sharpe = Sharpe(ReturnOnPortfolio=return_on_portfolio, RiskFreeRate=risk_free_rate, RiskOfPortfolio=risk_of_portfolio)
                isCalculated = True

    sharpe = "{:.2f}".format(sharpe / 100)

    return render_template('sharpe.html', return_on_portfolio=return_on_portfolio, risk_free_rate=risk_free_rate, risk_of_portfolio=risk_of_portfolio, sharpe=sharpe, isPost=isPost, isCalculated=isCalculated)

@app.route('/harmonicMean', methods=['POST', 'GET'])
def harmonic_mean():
    harmonic_data, harmonic_mean_result = 0, 0
    dataString = ""
    isPost = False

    if request.method == 'POST':
        isPost = True
        dataString = request.form['harmonic_data']
        splitData = dataString.split(',')
        
        if len(splitData) > 0:
            harmonic_data = [x.strip() for x in splitData]

            for i, ele in enumerate(harmonic_data):
                if check_float(ele):
                    harmonic_data[i] = float(ele)
                else:
                    return render_template('harmonicMean.html', harmonic_data=dataString, harmonic_mean_result=-1, isPost=isPost)
        
            harmonic_mean_result = HarmonicMean(harmonic_data)

    harmonic_mean_result = "{:.2f}".format(harmonic_mean_result)

    return render_template('harmonicMean.html', harmonic_data=dataString, harmonic_mean_result=harmonic_mean_result, isPost=isPost)


@app.route('/geometricMean', methods=['POST', 'GET'])
def geometricMean():
    geo_data, geo_mean_result = 0, 0
    dataString = ""
    isPost = False
    
    if request.method == 'POST':
        isPost = True
        dataString = request.form['geo_data']
        splitData = dataString.split(',')

        if len(splitData) > 0:
            geo_data = [x.strip() for x in splitData]

            for i, ele in enumerate(geo_data):
                if check_float(ele):
                    geo_data[i] = float(ele)
                else:
                    return render_template('geometricMean.html', geo_data=dataString, geo_mean_result=-1, isPost=isPost)

            geo_mean_result = GeoMean(geo_data)
    
    geo_mean_result = "{:.2f}".format(geo_mean_result)

    return render_template('geometricMean.html', geo_data=dataString, geo_mean_result=geo_mean_result, isPost=isPost)


# Main function
if __name__ == "__main__":
    app.run()