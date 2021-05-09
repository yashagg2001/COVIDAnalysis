import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def pmf(L,caption):
    D={}
    for i in L:        
        if str(i.days)!='nan':
            if i.days in D:
                D[(i.days)]+=1
            else:
                D.update({(i.days):1})
    X=[]
    Y=[]
    n=sum(D.values())
    for i in sorted(D.keys()):
        X.append(i)
        Y.append(D[i]/n)
    exp=0
    for i in range(len(X)):
        exp+=X[i]*Y[i]
    var=0
    for i in range(len(X)):
        var+=((X[i]-exp)**2)*Y[i]
    print(f'Expectation of {caption}: {exp} days')
    print(f'Variance of {caption}: {var} squared days')
    plt.bar(X,Y)
    plt.title(caption)
    plt.xlabel("No. of days")
    plt.ylabel("Probability")
    plt.show()
    #return sum(np.array(X)*np.array(Y))
    
xl=pd.ExcelFile("linton_supp_tableS1_S2_8Feb2020.xlsx")
surv=xl.parse("TableS1", header = 1, index_col=0)
dece=xl.parse("TableS2", header = 1, index_col=0)

expl=surv["ExposureL"]
expr=surv["ExposureR"]
expt=surv["ExposureType"]
onse=surv["Onset"]
hosp=surv["DateHospitalizedIsolated"]
l=len(expl)

print("Analysis 2 (i):")
IncP=[]
for i in range(l):
    if str(onse[i])!="NaT":
        if str(expl[i])!="NaT":
            IncP.append(onse[i]-expl[i])
pmf(IncP,"PMF of Incubation period")

print("Analysis 2 (ii):")

IncPnW=[]            
for i in range(l):
    if str(expt[i])!="Lives-works-studies in Wuhan" and str(onse[i])!="NaT" and str(expl[i])!="NaT":
        IncPnW.append(onse[i]-expl[i])

pmf(IncPnW,"PMF of Incubation period for non-Wuhan residents")

print("Analysis 2 (iii):")
X=dece["Death"]
O=dece["Onset"]
H=dece["Hospitalization/Isolation"]

pmf(H-O,"PMF of onset to hospitalization for deceased.")
pmf(X-O,"PMF of onset to death")
pmf(X-H,"PMF of hospitalization to death")
print("\nHence, we see a similar form of distribution in all three graphs, that they rise till a point, and then fall down towards zero, like a normal distribution.")

pmf(hosp-onse,"PMF of onset to hospitalization for survivors")
print("\nWe can see that the most survivors were hospitalized soon after the onset of symptoms, while most of the deceased got hospitalized after some days. Hence, we can say that late treatment can lead to death by COVID-19.")

