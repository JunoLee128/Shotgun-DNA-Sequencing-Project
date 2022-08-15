import subprocess
import pandas as pd
import os

cwd = os.getcwd()

for x in os.listdir(cwd):
    if len(x) == 10 and x[:3] == 'ERR':
        print('handling', x)
        subprocess.run(['sh', '/mnt/m/SA/shotmod.sh', x, 'EzWGSServiceBac'])

