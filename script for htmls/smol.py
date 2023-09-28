import pandas as pd

met = pd.read_csv("Metabolite_inf.csv", sep=";")

u = open ('fake_urls.txt', 'w+')
print(met.keys())
for i in range(len(met)):

    if met.loc[i]['HMDB ID'][0] == 'H':
        u.write(f"path('browse_metabolites/{met.iloc[i][2]}/', views.empty_met, name='empty_met'),")
        u.write('\n')
