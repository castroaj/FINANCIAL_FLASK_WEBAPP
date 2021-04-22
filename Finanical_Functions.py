import matplotlib.pyplot as plt
import numpy.financial as np
import statistics
from pandas import DataFrame
from scipy.stats.mstats import gmean

def HPR(Beginning_Price, End_Value, Dividend):

    if Beginning_Price == 0 and End_Value == 0 and Dividend == 0:
        return -1, -1, -1

#Holding Period Return Variables
    B = Beginning_Price
    if B < 0:
        B = abs(B)
    E = End_Value
    if E < 0:
        E = abs(E)
    D = Dividend
    if D < 0:
        D = abs(D)
#Holding Period Return math
    HPR= ((E-B+D)/B)
    HPR= HPR*100
#Capital Gains Calculation
    CG=((E-B)/B)*100
#Dividend Yield Calculation
    DY=(D/B)*100
#Data to pie plot
    labels='Capital Gains','Dividend Yield'
    sizes=[CG,DY]
    colors=['purple','yellow']
    # plt.pie(sizes,labels=labels,colors=colors,autopct='%1.1f%%',shadow=True)
    # plt.axis('equal')
    # plt.show()
    return HPR, CG, DY

##########################################

def Period_Rate(Number_Of_Payments,Payment_Amount,Amount_Barrowed):
#Per Period Rate Variables
    #N = Number_Of_Payments
    #PMT = Payment_Amount
    #PV = Amount_Barrowed
    #FV = 0
#math
    #Period_Rate_Percent = np.rate(N,-PMT,PV,FV)
    #return Period_Rate_Percent*100

#########################################
#new period rate
#finds effective interest rate for each compoiunding period
#to find EAR you need the per period rate, however you might only have APR and Num of periods
def Period_Rate(A,P):
    A = APR
    P = num_periods
    per_period_rate = (A/P)
return per_period_rate*100
#########################################

def APR(Per_Period_Rate, Number_Periods):
#APR Formula Variables
    P1 = Per_Period_Rate
    N1 = Number_Periods
#APR Math
    APR = (P1*N1)
    return APR

##########################################

def EAR(Per_Period_Rate, Number_Periods):
#EAR Formula Variables
    P2 = Per_Period_Rate / 100
    N2 = Number_Periods
#EAR Math
    EAR =((((1+P2)**(N2))-1))
    return EAR * 100

##########################################

def Sharpe(ReturnOnPortfolio,RiskFreeRate,RiskOfPortfolio):
 #Sharpe Ratio
 #Variables
    R = ReturnOnPortfolio/100
    T = RiskFreeRate/100
    S = RiskOfPortfolio/100
 #Formula
    Sharpe_Ratio = ((R-T)/S)
    return Sharpe_Ratio

##########################################

def HarmonicMean(data):
    return statistics.harmonic_mean(data)

##########################################

def GeoMean(data):
    df = DataFrame({'values' : data})
    return gmean(df.loc[:,'values'])

##########################################