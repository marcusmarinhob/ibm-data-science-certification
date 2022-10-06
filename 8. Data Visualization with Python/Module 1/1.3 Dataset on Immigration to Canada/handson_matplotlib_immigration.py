import numpy as np # useful for many scientific computing in Python
import pandas as pd # primary data structure library
# from __future__ import print_function # adds compatibility to python 2

df_can = pd.read_excel(
    './Canada.xlsx', 
    sheet_name="Regions by Citizenship",
    skiprows=range(20),
    skipfooter=2
)

print(df_can.head())