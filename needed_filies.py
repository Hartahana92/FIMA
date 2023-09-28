import pandas as pd
import shutil


met = pd.read_csv("D:\\Work\LABWORKS\\breast_cancer_met.csv", sep=",")


for i in range(len(met)):
    name = met.iloc[i][2].lower()
    name = name[:name.find('(') - 1]
    if met.loc[i]['Metabolite'][0] == 'H':
        shutil.copyfile(f"D:\\Work\LABWORKS\script for htmls\_{name}.html", f"D:\Work\LABWORKS\LFIMA\browse\templates\browse\_{name}.html")
