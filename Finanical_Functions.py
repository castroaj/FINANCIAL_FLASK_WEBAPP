def HPR(Beginning_Price, End_Value, Dividend):
#Holding Period Return Variables
    # Beginning_Price = float(input("What was the purchase price of the security? "))
    # End_Value = float(input("what was the sale price of the security? "))
    # Dividend = float(input("How much in dividend payments were recieved? "))
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
    #return print("Holding Period Return is ","%6.2f" % HPR,"%")
    return HPR

##########################################
def APR(Per_Period_Rate, Number_Periods):
#APR Formula Variables
    # Per_Period_Rate = float(input("What is the rate per period? "))
    # Number_Periods= float(input("How many periods are there? "))
    P1 = Per_Period_Rate
    N1 = Number_Periods
#APR Math
    APR = (P1*N1)
    #return print("The APR is ","%6.2f" % APR,"%")
    return APR

##########################################

def EAR(Per_Period_Rate, Number_Periods):
#EAR Formula Variables
    # Per_Period_Rate = float(input("What is the rate per period? "))
    # Number_Periods = float(input("How many periods are there? "))
    P2 = Per_Period_Rate / 100
    N2 = Number_Periods
#EAR Math
    EAR =((((1+P2)**(N2))-1))
    #return print("%6.2f" % EAR,"%")
    return EAR * 100