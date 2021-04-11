
def HPR(Beginning_Price, End_Value, Dividend):
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
    CG=((E-B)/B)
#Dividend Yield Calculation
    DY=(D/B)
    #Data to pie plot
    labels='Capital Gains','Dividend Yield'
    sizes=[CG,DY]
    colors=['purple','yellow']
    plt.pie(sizes,labels=labels,colors=colors,autopct='%1.1f%%',shadow=True)
    plt.axis('equal')
    #plt.show()
    return HPR, CG, DY

##########################################
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
