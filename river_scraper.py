import pandas as pd
import requests

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}



def grabber(name, linko):
    r = requests.get(linko, headers=headers)
    tableau = pd.read_html(r.text)[0]

    if name == 'brisbane':
        tableau['Minor flood'] = 1.7
        tableau['Moderate flood'] = 2.6
        tableau['Major flood'] = 3.5

    if name == 'mary':
        tableau['Minor flood'] = 6
        tableau['Moderate flood'] = 12
        tableau['Major flood'] = 17

    if name == 'wilsons':
        tableau['Minor flood'] = 4.2
        tableau['Moderate flood'] = 7.2
        tableau['Major flood'] = 9.7

    if name == 'hawkesbury':
        tableau['Minor flood'] = 3.8
        tableau['Moderate flood'] = 7.9
        tableau['Major flood'] = 10.5

    if name == 'nepean':
        tableau['Minor flood'] = 5.2
        tableau['Moderate flood'] = 9.2
        tableau['Major flood'] = 12.2

    tableau.rename(columns={'Station Date/Time': 'date', 'Water Level(m)': 'Water Level (m)'}, inplace=True)
    # tableau['date'] = pd.to_datetime(tableau['date'])
    # tableau['date'] = tableau['date'].dt.strftime("%Y-%m-%d")
    # ### Get max values for each date:

    # tableau['Date'] = pd.to_datetime(tableau['Station Date/Time'])
    # tableau['Date'] = tableau['Date'].dt.strftime("%Y-%m-%d")
    # tableau['count_max'] =tableau.groupby(['Date'])['Water Level(m)'].transform(max)

    # tableau.drop_duplicates(subset=['Date', 'Water Level(m)'], keep='last', inplace=True)
    # tableau = tableau.loc[tableau['Water Level(m)'] == tableau['count_max']]

    # tableau = tableau.groupby('Station Date/Time')['Water Level(m)'].max().reset_index()

    print(name)
    print(tableau)
    with open(f'input/{name}.csv', 'w') as f:
        tableau.to_csv(f, index=False, header=True)
    with open(f'oz-rainfall-charts-cumulative-master/assets/{name}.csv', 'w') as f:
        tableau.to_csv(f, index=False, header=True)


# grabber("wilsons", 'http://www.bom.gov.au/fwo/IDN60231/IDN60231.058176.tbl.shtml')

grabber("mary", 'http://www.bom.gov.au/fwo/IDQ65390/IDQ65390.040993.tbl.shtml')

grabber("brisbane", 'http://www.bom.gov.au/fwo/IDQ65389/IDQ65389.540684.tbl.shtml')

grabber("hawkesbury", 'http://www.bom.gov.au/fwo/IDN60233/IDN60233.567098.tbl.shtml')

grabber("nepean", 'http://www.bom.gov.au/fwo/IDN60233/IDN60233.068216.tbl.shtml')
