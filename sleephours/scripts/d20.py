import subprocess
import pandas as pd
import os

os.chdir('M:/EZB/agp')

df = pd.read_csv('agp.csv')
wgs = df.loc[df['LibraryStrategy'] == 'WGS']
wgs = wgs.loc[wgs['bmi_cat'] == 'Normal']
slp = wgs.loc[wgs['sleep_duration'] == '7-8 hours']
noslp = wgs.loc[wgs['sleep_duration'] == '6-7 hours']
print('slp')
slp20 = slp.head(20)['Run'].tolist()
print(slp20)
for x in slp20:
    print('downloading {}'.format(x))
    fasterq = 'fasterq-dump ' + x + ' -O sleep/slp'
    subprocess.call(fasterq, shell=True)
print('noslp')
noslp20 = noslp.head(20)['Run'].tolist()
print(noslp20)
for x in noslp20:
    print('downloading {}'.format(x))
    fasterq = 'fasterq-dump ' + x + ' -O sleep/noslp'
    subprocess.call(fasterq, shell=True)