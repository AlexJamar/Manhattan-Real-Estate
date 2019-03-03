import pandas as pd
import os

for filename in os.listdir('sales_data'):
    file = os.path.join('sales_data', filename)
    new_filename = filename.replace(".xls", ".csv")
    sales_data_clean = pd.read_excel(file, skiprows=[0,1,2], header=1)
    sales_data_clean.to_csv(new_filename, index=False)