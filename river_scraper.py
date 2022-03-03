import pandas as pd
import requests
import time  
from modules.syncData import syncData

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}



def grabber(name, linko, min, mod, maj):
    try:
        r = requests.get(linko, headers=headers)
        tableau = pd.read_html(r.text)[0]


        tableau.rename(columns={'Station Date/Time': 'date', 'Water Level(m)': 'Water Level (m)'}, inplace=True)


        tableau['Minor flood'] = min
        tableau['Moderate flood'] = mod
        tableau['Major flood'] = maj

        # tableau['date'] = pd.to_datetime(tableau['date'])
        # tableau['date'] = tableau['date'].dt.strftime("%Y-%m-%d")
        # ### Get max values for each date:

        # tableau['Date'] = pd.to_datetime(tableau['Station Date/Time'])
        # tableau['Date'] = tableau['Date'].dt.strftime("%Y-%m-%d")
        # tableau['count_max'] =tableau.groupby(['Date'])['Water Level(m)'].transform(max)

        # tableau.drop_duplicates(subset=['Date', 'Water Level(m)'], keep='last', inplace=True)
        # tableau = tableau.loc[tableau['Water Level(m)'] == tableau['count_max']]

        # tableau = tableau.groupby('Station Date/Time')['Water Level(m)'].max().reset_index()

        old = pd.read_csv(f'input/{name}.csv')

        combo = old.append(tableau)

        combo.drop_duplicates(subset=['date'], inplace=True, keep='last')

        # combo['date'] = pd.to_datetime(combo['date'])
        # combo['date'] = combo['date'].dt.strftime("%Y-%m-%d")

        with open(f'input/{name}.csv', 'w') as f:
            combo.to_csv(f, index=False, header=True)
        with open(f'oz-rainfall-charts-cumulative-master/assets/{name}.csv', 'w') as f:
            combo.to_csv(f, index=False, header=True)

        syncData(combo.to_json(orient='records'),'2022/02/river-heights', f"{name}")
        
        time.sleep(1)
    except:
        pass

# grabber("wilsons", 'http://www.bom.gov.au/fwo/IDN60231/IDN60231.058176.tbl.shtml', 4.2, 7.2, 9.7)

grabber("mary", 'http://www.bom.gov.au/fwo/IDQ65390/IDQ65390.040993.tbl.shtml', 6, 12, 17)

grabber("brisbane", 'http://www.bom.gov.au/fwo/IDQ65389/IDQ65389.540684.tbl.shtml', 1.7, 2.6, 3.5)

grabber("hawkesbury", 'http://www.bom.gov.au/fwo/IDN60233/IDN60233.567098.tbl.shtml', 3.8, 7.9, 10.5)

grabber("nepean", 'http://www.bom.gov.au/fwo/IDN60233/IDN60233.068216.tbl.shtml', 5.2, 9.2, 12.2)

willy = pd.read_csv('input/wilsons.csv')
syncData(willy.to_json(orient='records'),'2022/02/river-heights', f"wilsons")