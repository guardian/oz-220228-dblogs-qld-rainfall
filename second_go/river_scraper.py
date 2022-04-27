import pandas as pd
import requests
import time  
# from modules.syncData import syncData

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}



def grabber(name, linko, min, mod, maj):
    print(f"\n\nTrying {name}\n\n")
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

        # old = pd.read_csv(f'input/{name}.csv')

        # combo = old.append(tableau)

        # combo.drop_duplicates(subset=['date'], inplace=True, keep='last')

        combo = tableau.copy()

        # combo['date'] = pd.to_datetime(combo['date'])
        # combo['date'] = combo['date'].dt.strftime("%Y-%m-%d")

        with open(f'second_go/input/{name}.csv', 'w') as f:
            combo.to_csv(f, index=False, header=True)
        with open(f'second_go/oz-rainfall-charts-cumulative-master/assets/{name}.csv', 'w') as f:
            combo.to_csv(f, index=False, header=True)

        # syncData(combo.to_json(orient='records'),'2022/02/river-heights', f"{name}")
        
        time.sleep(1)
    except Exception as e:
        print(e)
        pass

grabber("wilsons", 'http://www.bom.gov.au/fwo/IDN60231/IDN60231.058176.tbl.shtml', 4.2, 7.2, 9.7)

grabber("tweed", 'http://www.bom.gov.au/fwo/IDN60231/IDN60231.058186.tbl.shtml', 3, 4, 4.8)

grabber("richmond", 'http://www.bom.gov.au/fwo/IDN60231/IDN60231.558002.tbl.shtml', 12, 14.4, 16)


# willy = pd.read_csv('input/wilsons.csv')
# syncData(willy.to_json(orient='records'),'2022/02/river-heights', f"wilsons")