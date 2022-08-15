import pandas as pd
import re
import glob
import shutil

ovw_files = glob.glob('../ovw/*/*.tab')
nor_files = glob.glob('../nor/*/*.tab')

for file in ovw_files:
    print(file)
    print(type(file))
    #shutil.copy2(file, '../ovw1/