# How to run this analysis in your local machine
<b>1. Clone This Project:</b> `git clone https://github.com/yashagg2001/COVIDAnalysis.git`<br>
<b>2. Go to Project Directory:</b>`cd COVIDAnalysis`<br>
<b>3. Create a Virtual Environment:</b>  `python -m venv covanalysis` (for windows)<br>
<b>4. Activate Virtual Environment:</b> `covanalysis\Scripts\activate.bat` (for windows)<br>
<b>5. Install Requirements Package:</b> `pip install -r requirements.txt`<br>
<b>6. Run Analysis 1:</b> `python Analysis1.py`<br>
<b>7. Run Analysis 2:</b> `python Analysis2.py`<br>
<b> Now, to deactivate virtual environment:</b> `deactivate` or `covanalysis\Scripts\deactivate`<br>
<b> Now, to delete virtual environment (simply delete folder `covanalysis`):</b> `rmdir covanalysis /s`<br>


# COVIDAnalysis
<b>In this project I analysed Coronavirus disease 2019 (COVID-19)
data from various data sources including data from India and around the world using python libraries `Pandas,Matplotlib and Numpy.`</b><br><br>
<b>Analysis 1 (in analysis1.py): </b>The data file `Covid19IndiaData_30032020.xlsx` presents the Indian patientlevel data until 30th March 2020. Source for latest Indian COVID-19 data: https://api.rootnet.in/. <br>
<b>(i)</b> I calculated and plot the probability mass function (pmf) of the age of infected patients
— this includes Hospitalized, Recovered and Dead. Then evaluated the expected age of an
infected patient from this pmf and the variance of the pmf. Then gave the conclusion.<br>
<b>(ii)</b> I calculated and plot the pmfs of the age of Recovered and Dead patients. Then calculated the
expectation and variance of the pmfs.Then gave conclusion about COVID-19 by comparing the expectation values.<br>
<b>(iii)</b>  Calculated the conditional pmf of the age of all infected patients conditional to the gender
of the patient. Then, I compare the expectations and gave comment of the possible reasons for any difference.<br><br>

<b>Analysis 2 (in analysis2.py):</b> The data file `linton_supp_tableS1_S2_8Feb2020.xlsx` presents patient-level case
data from China and other parts of the world. This includes the following information —
Exposure date (E), Symptoms onset date (O), Hospitalisation date (H), and Date of death
(X) in case of deceased patients. The data also includes whether the patient is/was a
resident of Wuhan (China). Please note that details of surviving and deceased patients
(until 31st January 2020) are included as different Sheets. The data can be downloaded
from http://www.mdpi.com/2077-0383/9/2/538/s1 <br>
<b>(i)</b>  I calculated and plot the pmf of the incubation period (the duration
between the date of infection exposure (E) and the date of onset of symptoms (O)). Then, calculated the mean incubation period and the variance of the distribution.<br>
<b>Note:</b> Use the left exposure data as the date of infection.<br>
<b>(ii)</b> Calculated the expected incubation period by excluding Wuhan residents and compare the values with part (i) and then provided the comment based on this comparison.<br>
<b>(iii)</b> Calculated the pmfs of the onset to hospitalization (H − O) for dead patients, onset
to death (X − O) and hospitalization to death (X − H). Then, commented on the similarity in the distribution. Also compared the H − O pmf for surviving and dead
patients and commented on the difference.<br>

