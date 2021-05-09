print('Analysis 1 (i) infected patients')
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data=pd.read_excel('Covid19IndiaData_30032020.xlsx')
#let age of infected patients be our random variable
age=list(data['Age'])
age_values=list(set(age))
#print(age_values)
prob=[]
for i in age_values:
    req_prob=float('%0.6f'%((age.count(i))/(len(age))))
    prob.append(req_prob)
#print(prob)
x={'Sr.No.':list(np.arange(1,len(age_values)+1)),'Age':age_values, 'Req. Prob.':prob}
PMF_Table=pd.DataFrame(x)
PMF_Table=PMF_Table.set_index('Sr.No.')
print(PMF_Table)
plt.style.use('ggplot')
plt.title('PMF of age of infected patients')
plt.xlabel('Ages')
plt.ylabel('Probabilites of infected patients age wise')
plt.stem(age_values,prob,use_line_collection=True)
plt.show()

#calcultion of expected age and variance of an infected patient from this pmf 
ex=0
var=0
for i in range(len(age_values)):
    XmulPX=age_values[i]*prob[i]
    ex+=XmulPX
for i in range(len(age_values)):
    varcal=((age_values[i]-ex)**2)*prob[i]
    var+=varcal
print('Expected Age:','%0.3f'%ex,' yrs')
print('Variance:','%0.3f'%var,' yrs squared')
print('''
As we can see that the spread of this graph is more and variance=127.629
so variance is high
Thus, in light of this high value of variance, we can deduce that COVID-19 disease is quite independent of the age of the patients.


 ''')

print('Analysis 1 (ii) recovered patients')
data=pd.read_excel('Covid19IndiaData_30032020.xlsx')
#let age of recovered patients be our random variable
A=data[(data['StatusCode']=='Recovered')]
age_recovered=list(A['Age'])
#print(age_recovered)
ageR_values=list(set(age_recovered))
#print(ageR_values)
prob=[]
for i in ageR_values:
    req_prob=float('%0.6f'%((age_recovered.count(i))/(len(age_recovered))))
    prob.append(req_prob)
#print(prob)
B={'Sr.No.':list(np.arange(1,len(ageR_values)+1)),'Age':ageR_values, 'Prob. recovered':prob}
PMF_Table=pd.DataFrame(B)
PMF_Table=PMF_Table.set_index('Sr.No.')
print(PMF_Table)
plt.style.use('ggplot')
plt.title('PMF of age of recovered patients')
plt.xticks(np.arange(0,91,10))
plt.xlabel('Ages')
plt.ylabel('Probabilites of recovered patients age wise')
plt.stem(ageR_values,prob,use_line_collection=True)
plt.show()

#calcultion of expected age and variance of an recovered patients from this pmf 
ex=0
var=0
for i in range(len(ageR_values)):
    XmulPX=ageR_values[i]*prob[i]
    ex+=XmulPX
for i in range(len(ageR_values)):
    varcal=((ageR_values[i]-ex)**2)*prob[i]
    var+=varcal
print('Expected Age of recovered patients:','%0.3f'%ex,' yrs')
print('Variance of recovered patients:','%0.3f'%var,' yrs squared')
print(' ')
print(' ')

print('Analysis 1 (ii) dead patients')
data=pd.read_excel('Covid19IndiaData_30032020.xlsx')
#let age of dead patients be our random variable
C=data[(data['StatusCode']=='Dead')]
age_dead=list(C['Age'])
#print(age_dead)
ageD_values=list(set(age_dead))
#print(ageD_values)
prob2=[]
for i in ageD_values:
    req_prob2=float('%0.6f'%((age_dead.count(i))/(len(age_dead))))
    prob2.append(req_prob2)
#print(prob2)
D={'Sr.No.':list(np.arange(1,len(ageD_values)+1)),'Age':ageD_values, 'Prob. dead':prob2}
PMF_Table2=pd.DataFrame(D)
PMF_Table2=PMF_Table2.set_index('Sr.No.')
print(PMF_Table2)
plt.style.use('ggplot')
plt.title('PMF of age of dead patients')
plt.xlabel('Ages')
plt.ylabel('Probabilites of dead patients age wise')
plt.stem(ageD_values,prob2,use_line_collection=True)
plt.show()

#calcultion of expected age and variance of an dead patients from this pmf 
ex2=0
var2=0
for i in range(len(ageD_values)):
    XmulPX=ageD_values[i]*prob2[i]
    ex2+=XmulPX
for i in range(len(ageD_values)):
    varcal=((ageD_values[i]-ex2)**2)*prob2[i]
    var2+=varcal
print('Expected Age of dead patients:','%0.3f'%ex2,' yrs')
print('Variance of dead patients:','%0.3f'%var2,' yrs squared')

print('''
Expected ages are different from expected age in case(i) 

By analysing the expected ages we can say that mostly old age people (age more than 60)
are dead due to covid-19 because of their weak immune system
Mostly infected patients are of age 40, means people of age about 40 are not staying at their homes,
but due to their comparably strong immune system, they got recovered from the disease.
So stayhome, stayfit and make your immune system strong by yoga to prevent yourself from covid19.. 


''')
print('Analysis 1 (iii) male patients')
data=pd.read_excel('Covid19IndiaData_30032020.xlsx')
#let age of male patients be our random variable
A=data[(data['GenderCode0F1M']==1)]
age_male=list(A['Age'])
#print(age_male)
ageM_values=list(set(age_male))
#print(ageM_values)
prob=[]
for i in ageM_values:
    req_prob=float('%0.6f'%((age_male.count(i))/(len(age_male))))
    prob.append(req_prob)
#print(prob)
B={'Sr.No.':list(np.arange(1,len(ageM_values)+1)),'Age':ageM_values, 'Prob. male':prob}
PMF_Table=pd.DataFrame(B)
PMF_Table=PMF_Table.set_index('Sr.No.')
print(PMF_Table)
plt.style.use('ggplot')
plt.title('PMF of age of male patients')
plt.xticks(np.arange(0,91,10))
plt.xlabel('Ages')
plt.ylabel('Probabilites of male patients age wise')
plt.stem(ageM_values,prob,use_line_collection=True)
plt.show()

#calcultion of expected age of an male patients from this pmf 
ex=0
var=0
for i in range(len(ageM_values)):
    XmulPX=ageM_values[i]*prob[i]
    ex+=XmulPX

print('Expected Age of male patients:','%0.3f'%ex,' yrs')
print('''
      
      ''')

print('Analysis 1 (iii) female patients')
data=pd.read_excel('Covid19IndiaData_30032020.xlsx')
#let age of female patients be our random variable
A=data[(data['GenderCode0F1M']==0)]
age_female=list(A['Age'])
#print(age_female)
ageF_values=list(set(age_female))
#print(ageF_values)
prob=[]
for i in ageF_values:
    req_prob=float('%0.6f'%((age_female.count(i))/(len(age_female))))
    prob.append(req_prob)
#print(prob)
B={'Sr.No.':list(np.arange(1,len(ageF_values)+1)),'Age':ageF_values, 'Prob. female':prob}
PMF_Table=pd.DataFrame(B)
PMF_Table=PMF_Table.set_index('Sr.No.')
print(PMF_Table)
plt.style.use('ggplot')
plt.title('PMF of age of female patients')
plt.xticks(np.arange(0,91,10))
plt.xlabel('Ages')
plt.ylabel('Probabilites of female patients age wise')
plt.stem(ageF_values,prob,use_line_collection=True)
plt.show()

#calcultion of expected age of an female patients from this pmf 
ex=0
var=0
for i in range(len(ageF_values)):
    XmulPX=ageF_values[i]*prob[i]
    ex+=XmulPX

print('Expected Age of female patients:','%0.3f'%ex,' yrs')
print('''
Plot for male and female infected patients are not identically distributed
But the expected age of male and female infected patients are approximately same...
Hence, we can't infer any practical or proper conclusion from the analysis of this data, as it has too many females of the same age (38) infected.
As real studies are concerned, there is hardly any difference between no. of infected patients of both genders. 
It is to be noted however, that some studies have shown a higher fatality rate for males.    
      ''')

