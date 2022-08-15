import subprocess
import pandas as pd
import os

df = pd.read_csv('agp.csv')
wgs = df.loc[df['LibraryStrategy'] == 'WGS']
overweight = wgs.loc[wgs['bmi_cat'] == 'Overweight']
normal = wgs.loc[wgs['bmi_cat'] == 'Normal']
'''
print('OVERWEIGHT')
ovw20 = overweight.head(20)['Run'].tolist()
print(ovw20)
for x in ovw20:
    print('downloading {}'.format(x))
    fasterq = 'fasterq-dump ' + x + ' -O ovw'
    subprocess.call(fasterq, shell=True)
'''
print('NORMAL')
nor = normal.head(20)['Run'].tolist()
print(nor)
for x in nor:
    print('downloading {}'.format(x))
    fasterq = 'fasterq-dump ' + x + ' -O ovw'
    subprocess.call(fasterq, shell=True)